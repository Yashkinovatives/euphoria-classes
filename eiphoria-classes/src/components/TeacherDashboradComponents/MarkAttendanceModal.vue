<!-- MarkAttendanceModal.vue -->
<template>
    <div v-if="show" class="modal-overlay" @click.self="close">
      <div class="attendance-modal">
        <div class="modal-header">
          <h3>Mark Attendance</h3>
          <button @click="close" class="close-btn">&times;</button>
        </div>
        
        <div class="modal-content">
          <div class="attendance-controls">
            <div class="date-selector">
              <label for="attendance-date">Date:</label>
              <input 
                type="date" 
                id="attendance-date" 
                v-model="attendanceDate" 
                class="date-input"
              />
            </div>
            
            <div class="class-filter-container">
              <label for="attendance-class">Filter by Class:</label>
              <select 
                id="attendance-class" 
                v-model="attendanceClass" 
                class="filter-select"
              >
                <option value="">All Classes</option>
                <option 
                  v-for="classOption in uniqueClasses" 
                  :key="classOption"
                  :value="classOption"
                >
                  {{ classOption }}
                </option>
              </select>
            </div>
            
            <div class="bulk-actions">
              <button @click="selectAllStudents" class="btn btn-secondary">Select All</button>
              <button @click="unselectAllStudents" class="btn btn-secondary">Unselect All</button>
              <select v-model="bulkStatus" class="status-select">
                <option value="Present">Present</option>
                <option value="Absent">Absent</option>
                <option value="Late">Late</option>
              </select>
              <button @click="applyBulkStatus" class="btn btn-primary">Apply to Selected</button>
            </div>
          </div>
          
          <div class="students-list">
            <div 
              v-for="student in filteredAttendanceStudents" 
              :key="student.id"
              class="student-attendance-item"
            >
              <div class="student-check">
                <input 
                  type="checkbox" 
                  :id="`student-${student.id}`" 
                  v-model="selectedStudents" 
                  :value="student.id"
                />
                <label :for="`student-${student.id}`" class="student-label">
                  <div class="student-info">
                    <div class="student-avatar-small">{{ student.name[0] }}</div>
                    <div class="student-details">
                      <div class="student-name">{{ student.name }}</div>
                      <div class="student-class-name">{{ student.class_section__name }}</div>
                    </div>
                  </div>
                </label>
              </div>
              
              <select v-model="studentStatus[student.id]" class="status-select">
                <option value="Present">Present</option>
                <option value="Absent">Absent</option>
                <option value="Late">Late</option>
              </select>
            </div>
          </div>
        </div>
        
        <div class="modal-footer">
          <span class="selection-count">{{ selectedStudents.length }} students selected</span>
          <div class="modal-actions">
            <button @click="close" class="btn btn-cancel">Cancel</button>
            <button 
              @click="submitAttendance" 
              class="btn btn-submit" 
              :disabled="selectedStudents.length === 0"
            >
              Submit Attendance
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, defineProps, defineEmits, onMounted } from 'vue';
  import axios from 'axios';
  
  const props = defineProps({
    show: {
      type: Boolean,
      default: false
    },
    students: {
      type: Array,
      required: true
    }
  });
  
  const emit = defineEmits(['close', 'attendance-marked']);
  
  // Modal state
  const attendanceDate = ref(new Date().toISOString().split('T')[0]); // Default to today
  const attendanceClass = ref('');
  const selectedStudents = ref([]);
  const studentStatus = ref({});
  const bulkStatus = ref('Present');
  
  // Computed properties for filtering
  const uniqueClasses = computed(() => {
    return [...new Set(props.students.map(student => student.class_section__name))];
  });
  
  const filteredAttendanceStudents = computed(() => {
    return props.students.filter(student => {
      return !attendanceClass.value || student.class_section__name === attendanceClass.value;
    });
  });
  
  // Initialize student status to "Present" for all students
  onMounted(() => {
    props.students.forEach(student => {
      studentStatus.value[student.id] = 'Present';
    });
    
    // Set today's date as default
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    attendanceDate.value = `${year}-${month}-${day}`;
  });
  
  // Close the modal
  const close = () => {
    emit('close');
  };
  
  // Selection functions
  const selectAllStudents = () => {
    selectedStudents.value = filteredAttendanceStudents.value.map(student => student.id);
  };
  
  const unselectAllStudents = () => {
    selectedStudents.value = [];
  };
  
  // Apply bulk status to all selected students
  const applyBulkStatus = () => {
    selectedStudents.value.forEach(studentId => {
      studentStatus.value[studentId] = bulkStatus.value;
    });
  };
  
  // Submit attendance to the API
  const submitAttendance = async () => {
    try {
      const token = localStorage.getItem('access_token');
      const submissionPromises = [];
      
      // Group students by status to make separate API calls
      const studentsByStatus = {};
      
      selectedStudents.value.forEach(studentId => {
        const status = studentStatus.value[studentId].toLowerCase();
        if (!studentsByStatus[status]) {
          studentsByStatus[status] = [];
        }
        studentsByStatus[status].push(studentId);
      });
      
      // Create API requests for each status group
      for (const [status, studentIds] of Object.entries(studentsByStatus)) {
        if (studentIds.length > 0) {
          const attendanceData = {
            student_ids: studentIds,
            date: attendanceDate.value,
            status: status
          };
          
          submissionPromises.push(
            axios.post(
              "http://127.0.0.1:8000/api/teacher/bulk-mark-attendance/",
              attendanceData,
              {
                headers: { Authorization: `Bearer ${token}` }
              }
            )
          );
        }
      }
      
      // Wait for all API calls to complete
      const results = await Promise.all(submissionPromises);
      
      // Check if all were successful
      const allSuccessful = results.every(response => response.status === 201);
      
      if (allSuccessful) {
        alert("Attendance marked successfully for all students!");
        emit('attendance-marked');
        close();
      } else {
        alert("Some attendance records may not have been saved correctly.");
      }
    } catch (error) {
      // Handle error
      console.error("Error marking attendance:", error);
      alert(`Error marking attendance: ${error.response?.data?.error || error.message}`);
    }
  };
  </script>
  
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap");
  
  /* Modal Styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    backdrop-filter: blur(5px);
    font-family: "Nunito", sans-serif;
  }
  
  .attendance-modal {
    background: white;
    border-radius: 16px;
    width: 90%;
    max-width: 800px;
    max-height: 90vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    animation: modalFadeIn 0.3s ease;
  }
  
  @keyframes modalFadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 1.5rem;
    border-bottom: 1px solid #e5e7eb;
  }
  
  .modal-header h3 {
    font-family: 'Quicksand', sans-serif;
    margin: 0;
    color: #2D3748;
    font-size: 1.25rem;
    font-weight: 700;
  }
  
  .close-btn {
    background: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
    line-height: 1;
    padding: 0;
  }
  
  .modal-content {
    padding: 1.5rem;
    overflow-y: auto;
    flex-grow: 1;
  }
  
  .attendance-controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.25rem;
    margin-bottom: 1.5rem;
    background: #f8fafc;
    padding: 1.25rem;
    border-radius: 12px;
  }
  
  .date-selector,
  .class-filter-container {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #4b5563;
  }
  
  .date-input {
    padding: 0.6rem 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    font-size: 0.9rem;
  }
  
  .filter-select {
    padding: 0.6rem 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background-color: white;
    font-size: 0.9rem;
  }
  
  .bulk-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    align-items: flex-end;
  }
  
  .status-select {
    padding: 0.6rem 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background-color: white;
    font-size: 0.9rem;
    min-width: 100px;
  }
  
  .students-list {
    display: grid;
    gap: 0.75rem;
    max-height: 350px;
    overflow-y: auto;
    margin-top: 1rem;
    border-radius: 8px;
    background: #f9fafb;
    padding: 1rem;
    border: 1px solid #e5e7eb;
  }
  
  .student-attendance-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 1rem;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }
  
  .student-check {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex: 1;
  }
  
  .student-label {
    cursor: pointer;
    padding-left: 0.5rem;
    display: flex;
    align-items: center;
    flex: 1;
  }
  
  .student-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .student-avatar-small {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #4B96F3, #3178E6);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 600;
    font-size: 0.9rem;
    flex-shrink: 0;
  }
  
  .student-details {
    display: flex;
    flex-direction: column;
  }
  
  .student-name {
    font-weight: 600;
    color: #2D3748;
  }
  
  .student-class-name {
    font-size: 0.85rem;
    color: #4B96F3;
  }
  
  .modal-footer {
    padding: 1.25rem 1.5rem;
    border-top: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .selection-count {
    font-size: 0.9rem;
    color: #4b5563;
  }
  
  .modal-actions {
    display: flex;
    gap: 1rem;
  }
  
  .btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    white-space: nowrap;
    text-align: center;
    touch-action: manipulation;
  }
  
  .btn-primary {
    background: linear-gradient(135deg, #4B96F3, #3178E6);
    color: white;
  }
  
  .btn-secondary {
    background: rgba(75, 150, 243, 0.1);
    color: #3178E6;
    border: 1px solid rgba(75, 150, 243, 0.2);
  }
  
  .btn-cancel {
    background: #f3f4f6;
    color: #4b5563;
    border: 1px solid #e5e7eb;
  }
  
  .btn-submit {
    background: linear-gradient(135deg, #10B981, #059669);
    color: white;
  }
  
  .btn-submit:disabled {
    background: #d1d5db;
    cursor: not-allowed;
  }
  
  .btn:hover:not(:disabled) {
    transform: translateY(-2px);
  }
  
  .btn:active:not(:disabled) {
    transform: translateY(0);
  }
  
  /* Responsive Adaptations */
  @media (max-width: 768px) {
    .attendance-modal {
      width: 95%;
      max-width: none;
      max-height: 95vh;
    }
    
    .attendance-controls {
      grid-template-columns: 1fr;
    }
    
    .student-attendance-item {
      flex-direction: column;
      align-items: stretch;
      gap: 0.75rem;
    }
    
    .student-check {
      margin-bottom: 0.5rem;
    }
    
    .modal-footer {
      flex-direction: column;
      gap: 1rem;
      align-items: stretch;
    }
    
    .modal-actions {
      flex-direction: column;
      gap: 0.75rem;
    }
  }
  
  @media (max-width: 480px) {
    .attendance-controls {
      padding: 1rem;
    }
    
    .bulk-actions {
      flex-direction: column;
      align-items: stretch;
    }
    
    .modal-header h3 {
      font-size: 1.1rem;
    }
  }
  </style>