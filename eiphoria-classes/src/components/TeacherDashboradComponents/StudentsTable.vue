<!-- StudentsTable.vue -->
<template>
  <div class="students-section">
    <div class="section-header">
      <div class="title-badge">
        <span class="badge-icon">📚</span>
        <h2>Students Management</h2>
      </div>
      
      <div class="search-filter">
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input 
            v-model="searchQuery" 
            placeholder="Search students..." 
            class="search-input"
          />
        </div>
        <select v-model="selectedClass" class="class-filter">
          <option value="">All Classes</option>
          <option 
            v-for="classOption in uniqueClasses" 
            :key="classOption"
            :value="classOption"
          >
            {{ classOption }}
          </option>
        </select>
        <button @click="openAttendanceModal" class="desktop-attendance-btn btn btn-mark-attendance">
          <span>✓</span> Mark Attendance
        </button>
      </div>
    </div>

    <div class="table-container">
      <!-- Desktop table header controls -->
      <div class="table-header-with-controls desktop-only">
        <div class="table-count">
          Showing {{ studentsToShow.length }} of {{ filteredStudents.length }} students
        </div>
        <button 
          v-if="filteredStudents.length > 5" 
          @click="toggleStudentsView" 
          class="toggle-students-btn"
        >
          {{ showAllStudents ? 'Show Less' : 'Show All' }}
          <span class="toggle-icon" :class="{ 'expanded': showAllStudents }">▼</span>
        </button>
      </div>

      <!-- Desktop Table View -->
      <table class="students-table">
        <thead>
          <tr>
            <th>Student</th>
            <th>Class</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="student in studentsToShow" 
            :key="student.id"
            class="student-row"
          >
            <td class="student-info">
              <div class="student-avatar">{{ student.name[0] }}</div>
              <div class="student-details">
                <div class="student-name">{{ student.name }}</div>
                <div class="student-id">ID: {{ student.id }}</div>
              </div>
            </td>
            <td class="class-cell">{{ student.class_section__name }}</td>
            <td class="actions-cell">
              <div class="action-buttons">
                <button 
                  @click="$emit('add-test', student)"
                  class="btn btn-primary"
                >
                  <span>📝</span> Add Test
                </button>
                <button 
                  @click="$emit('view-results', student)"
                  class="btn btn-secondary"
                >
                  <span>👁️</span> View
                </button>
                <button 
                  @click="$emit('manage-fees', student)"
                  class="btn btn-tertiary"
                >
                  <span>💰</span> Fees
                </button>
                <button 
                  @click="$emit('manage-attendance', student)"
                  class="btn btn-attendance"
                >
                  <span>📊</span> Attendance
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Mobile Card View for Students -->
      <div class="mobile-student-cards">
        <!-- Mobile table header controls -->
        <div class="mobile-table-controls mobile-only">
          <div class="table-count">
            Showing {{ studentsToShow.length }} of {{ filteredStudents.length }} students
          </div>
          <button 
            v-if="filteredStudents.length > 5" 
            @click="toggleStudentsView" 
            class="toggle-students-btn"
          >
            {{ showAllStudents ? 'Show Less' : 'Show All' }}
            <span class="toggle-icon" :class="{ 'expanded': showAllStudents }">▼</span>
          </button>
        </div>
        
        <div 
          v-for="student in studentsToShow" 
          :key="student.id"
          class="student-card"
        >
          <div class="card-header">
            <div class="student-info">
              <div class="student-avatar">{{ student.name[0] }}</div>
              <div class="student-details">
                <div class="student-name">{{ student.name }}</div>
                <div class="student-class">{{ student.class_section__name }}</div>
                <div class="student-id">ID: {{ student.id }}</div>
              </div>
            </div>
            
            <!-- Mobile Actions Menu (3 dots) -->
            <div class="mobile-actions-menu">
              <button 
                @click="toggleActionsMenu(student.id)" 
                class="actions-toggle-btn"
              >
                <span>⋮</span>
              </button>
              <div 
                v-if="openActionMenuId === student.id" 
                class="actions-dropdown"
              >
                <button 
                  @click="$emit('add-test', student); closeActionsMenu()"
                  class="action-item"
                >
                  <span>📝</span> Add Test
                </button>
                <button 
                  @click="$emit('view-results', student); closeActionsMenu()"
                  class="action-item"
                >
                  <span>👁️</span> View Results
                </button>
                <button 
                  @click="$emit('manage-fees', student); closeActionsMenu()"
                  class="action-item"
                >
                  <span>💰</span> Manage Fees
                </button>
                <button 
                  @click="$emit('manage-attendance', student); closeActionsMenu()"
                  class="action-item"
                >
                  <span>📊</span> Attendance
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Mobile Mark Attendance Button - Fixed position -->
      <div class="mobile-attendance-button mobile-only">
        <button @click="openAttendanceModal" class="btn btn-mark-attendance">
          <span>✓</span> Mark
        </button>
      </div>

      <div v-if="filteredStudents.length === 0" class="no-results">
        <div class="no-results-icon">🔍</div>
        <p>No students found</p>
      </div>
      
      <!-- Show More/Less Students Button (Desktop) -->
      <div v-if="filteredStudents.length > 5" class="view-more-container desktop-only">
        <button 
          @click="toggleStudentsView" 
          class="view-more-btn"
        >
          {{ showAllStudents ? 'Show Less Students' : `Show ${filteredStudents.length - 5} More Students` }}
        </button>
      </div>
    </div>

    <!-- Attendance Modal -->
    <div v-if="showAttendanceModal" class="modal-overlay" @click.self="closeAttendanceModal">
      <div class="attendance-modal">
        <div class="modal-header">
          <h3>Mark Attendance</h3>
          <button @click="closeAttendanceModal" class="close-btn">&times;</button>
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
            <button @click="closeAttendanceModal" class="btn btn-cancel">Cancel</button>
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
    
    <!-- Click overlay for closing mobile action menus -->
    <div 
      v-if="openActionMenuId !== null" 
      class="overlay-close-menu" 
      @click="closeActionsMenu"
    ></div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps, defineEmits, onMounted } from 'vue';
import axios from 'axios';

// Define props without assigning to a variable
const props = defineProps({
  students: {
    type: Array,
    required: true
  }
});

// Define emits for all the events
defineEmits(['add-test', 'view-details', 'view-results', 'manage-fees', 'manage-attendance']);

// Students table state
const searchQuery = ref('');
const selectedClass = ref('');

// Pagination/dropdown state
const showAllStudents = ref(false);
const studentsToShow = computed(() => {
  if (showAllStudents.value) {
    return filteredStudents.value;
  } else {
    return filteredStudents.value.slice(0, 5); // Show only first 5 students
  }
});

// Mobile actions menu state
const openActionMenuId = ref(null);

// Attendance modal state
const showAttendanceModal = ref(false);
const attendanceDate = ref(new Date().toISOString().split('T')[0]); // Default to today
const attendanceClass = ref('');
const selectedStudents = ref([]);
const studentStatus = ref({});
const bulkStatus = ref('Present');

// Computed properties for filtering
const uniqueClasses = computed(() => {
  return [...new Set(props.students.map(student => student.class_section__name))];
});

const filteredStudents = computed(() => {
  return props.students.filter(student => {
    const matchesSearch = student.name.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesClass = !selectedClass.value || student.class_section__name === selectedClass.value;
    return matchesSearch && matchesClass;
  });
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
  
  // Close action menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.mobile-actions-menu') && openActionMenuId.value !== null) {
      closeActionsMenu();
    }
  });
});

// Toggle between showing all students and just the first 5
const toggleStudentsView = () => {
  showAllStudents.value = !showAllStudents.value;
};

// Mobile actions menu functions
const toggleActionsMenu = (studentId) => {
  if (openActionMenuId.value === studentId) {
    openActionMenuId.value = null;
  } else {
    openActionMenuId.value = studentId;
  }
};

const closeActionsMenu = () => {
  openActionMenuId.value = null;
};

// Modal functions
const openAttendanceModal = () => {
  showAttendanceModal.value = true;
  // Reset selections when opening modal
  selectedStudents.value = [];
  attendanceClass.value = '';
};

const closeAttendanceModal = () => {
  showAttendanceModal.value = false;
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
      closeAttendanceModal();
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

.desktop-only {
  display: block;
}

.mobile-only {
  display: none;
}

.students-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(75, 150, 243, 0.15);
  border: 1px solid rgba(75, 150, 243, 0.1);
  font-family: "Nunito", sans-serif;
  box-sizing: border-box;
  position: relative; /* For modal positioning */
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.title-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.title-badge h2 {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.5rem;
  margin: 0;
  color: #2D3748;
  font-weight: 700;
}

.badge-icon {
  font-size: 1.5rem;
}

.search-filter {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  align-items: center;
}

.search-box {
  position: relative;
  width: 250px;
  max-width: 100%;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-input {
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  font-size: 0.9rem;
  width: 100%;
  transition: all 0.3s ease;
  font-size: 16px; /* Prevents iOS zoom on focus */
  -webkit-appearance: none; /* Better appearance on iOS */
  box-sizing: border-box;
}

.search-input:focus {
  outline: none;
  border-color: #3178E6;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
}

.class-filter {
  padding: 0.75rem 1.5rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  font-size: 0.9rem;
  color: #2D3748;
  background: white;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 16px; /* Prevents iOS zoom on focus */
  -webkit-appearance: none; /* Better appearance on iOS */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%234B96F3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 2.5rem;
  box-sizing: border-box;
}

.class-filter:focus {
  outline: none;
  border-color: #3178E6;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
}

.btn-mark-attendance {
  background: linear-gradient(135deg, #10B981, #059669);
  color: white;
}

.table-container {
  overflow-x: auto;
}

.table-header-with-controls,
.mobile-table-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border-radius: 8px;
}

.mobile-table-controls {
  flex-direction: column;
  align-items: stretch;
  gap: 0.75rem;
}

.table-count {
  font-size: 0.9rem;
  color: #4b5563;
}

.toggle-students-btn {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  background: transparent;
  border: none;
  color: #3178E6;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  transition: background 0.2s;
}

.toggle-students-btn:hover {
  background: rgba(49, 120, 230, 0.1);
}

.toggle-icon {
  font-size: 0.7rem;
  transition: transform 0.2s ease;
}

.toggle-icon.expanded {
  transform: rotate(180deg);
}

.view-more-container {
  display: flex;
  justify-content: center;
  margin-top: 1.5rem;
}

.view-more-btn {
  background: #f3f4f6;
  color: #3178E6;
  font-weight: 600;
  border: 1px solid #e5e7eb;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-more-btn:hover {
  background: #e5e7eb;
}

.students-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 0.5rem;
}

.students-table th {
  padding: 1rem;
  text-align: left;
  color: #64748b;
  font-weight: 600;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
}

.student-row {
  background: white;
  border-radius: 12px;
  transition: transform 0.3s ease;
  box-shadow: 0 2px 10px rgba(75, 150, 243, 0.05);
}

.student-row:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.1);
}

.student-row td {
  padding: 1rem;
  vertical-align: middle;
}

.student-row td:first-child {
  border-top-left-radius: 12px;
  border-bottom-left-radius: 12px;
}

.student-row td:last-child {
  border-top-right-radius: 12px;
  border-bottom-right-radius: 12px;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
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

.student-id {
  font-size: 0.85rem;
  color: #64748b;
}

.student-class {
  font-size: 0.9rem;
  color: #4B96F3;
  font-weight: 500;
}

.student-class-name {
  font-size: 0.85rem;
  color: #4B96F3;
}

.spacer {
  height: 10px;
}

.action-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
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

.btn-tertiary {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
  border: 1px solid rgba(245, 158, 11, 0.2);
}

.btn-attendance {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.2);
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

.no-results {
  text-align: center;
  padding: 3rem;
  color: #64748b;
}

.no-results-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

/* Mobile Card View Styling */
.mobile-student-cards {
  display: none;
}

.mobile-attendance-button {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 100;
}

.mobile-attendance-button .btn {
  height: 56px;
  width: 56px;
  border-radius: 50%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

.student-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

/* Mobile Actions Menu Styling */
.mobile-actions-menu {
  position: relative;
}

.actions-toggle-btn {
  background: transparent;
  border: none;
  color: #64748b;
  font-size: 1.5rem;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 50%;
}

.actions-toggle-btn:hover {
  background: #f1f5f9;
}

.actions-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  min-width: 180px;
  z-index: 10;
  overflow: hidden;
  animation: menuFadeIn 0.2s ease;
}

@keyframes menuFadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.action-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  width: 100%;
  border: none;
  background: transparent;
  text-align: left;
  cursor: pointer;
  color: #374151;
  font-size: 0.9rem;
}

.action-item:hover {
  background: #f1f5f9;
}

.overlay-close-menu {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 5;
}

/* Attendance Modal Styles */
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

/* Responsive Adaptations */
@media (max-width: 1200px) {
  .action-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    width: 100%;
  }
  
  .btn {
    width: 100%;
  }
  
  .attendance-controls {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 940px) {
  .search-filter {
    flex-direction: column;
    gap: 0.75rem;
    width: 100%;
    max-width: 300px;
  }
  
  .search-box {
    width: 100%;
  }
  
  .class-filter {
    width: 100%;
  }
}

@media (max-width: 768px) {
  /* Show/hide appropriate elements for mobile */
  .desktop-only {
    display: none !important;
  }
  
  .mobile-only {
    display: block;
  }
  
  .desktop-attendance-btn {
    display: none;
  }
  
  .section-header {
    flex-direction: column;
    gap: 1.25rem;
    align-items: flex-start;
  }

  .search-filter {
    width: 100%;
    max-width: 100%;
    flex-direction: column;
    gap: 0.75rem;
  }

  .search-box {
    width: 100%;
  }
  
  .search-input,
  .class-filter {
    width: 100%;
  }
  
  .students-table {
    display: none;
  }
  
  .mobile-student-cards {
    display: block;
  }
  
  .mobile-attendance-button {
    display: block;
  }

  .mobile-attendance-button .btn {
    font-size: 1rem;
    width: auto;
    height: auto;
    border-radius: 8px;
    padding: 0.75rem 1.25rem;
  }
  
  /* Mobile modal optimizations */
  .attendance-modal {
    width: 100%;
    height: 100%;
    max-width: none;
    max-height: none;
    border-radius: 0;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: 0;
    animation: mobileModalSlideUp 0.3s ease;
  }
  
  @keyframes mobileModalSlideUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
  }
  
  .modal-content {
    padding: 1rem;
  }
  
  .attendance-controls {
    padding: 0.75rem;
    gap: 0.75rem;
  }
  
  .students-list {
    max-height: none;
    height: calc(100vh - 350px);
  }
  
  .student-attendance-item {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }
  
  .student-check {
    margin-bottom: 0;
  }
  
  .status-select {
    width: 100%;
  }
  
  .modal-footer {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
    padding: 1rem;
  }
  
  .modal-actions {
    flex-direction: row;
    gap: 0.75rem;
  }
  
  .btn-cancel, .btn-submit {
    flex: 1;
  }
  
  .bulk-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
  }
  
  .bulk-actions .btn,
  .bulk-actions .status-select {
    grid-column: span 1;
  }
}

@media (max-width: 480px) {
  .students-section {
    padding: 1.25rem;
    border-radius: 12px;
  }
  
  .title-badge h2 {
    font-size: 1.25rem;
  }
  
  .badge-icon {
    font-size: 1.25rem;
  }
  
  .student-card {
    padding: 1rem;
  }
  
  .search-input, 
  .class-filter {
    padding: 0.7rem 1rem;
    font-size: 0.9rem;
  }
  
  .search-input {
    padding-left: 2.25rem;
  }
  
  .attendance-controls {
    padding: 0.75rem;
  }
  
  .modal-header h3 {
    font-size: 1.1rem;
  }
  
  .bulk-actions {
    grid-template-columns: 1fr;
  }
  
  .bulk-actions .btn,
  .bulk-actions .status-select {
    grid-column: span 1;
  }
  
  .modal-actions {
    flex-direction: column;
  }
  
  .students-list {
    padding: 0.75rem;
    height: calc(100vh - 380px);
  }
}

@media (max-width: 360px) {
  .students-section {
    padding: 1rem;
  }
  
  .section-header {
    margin-bottom: 1.25rem;
  }
  
  .student-card {
    padding: 0.875rem;
  }
  
  .student-avatar {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    font-size: 0.9rem;
  }
  
  .btn {
    padding: 0.5rem 0.75rem;
    font-size: 0.85rem;
  }
  
  .modal-header h3 {
    font-size: 1rem;
  }
  
  .students-list {
    height: calc(100vh - 400px);
  }
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .students-section {
    padding-left: max(1.5rem, env(safe-area-inset-left));
    padding-right: max(1.5rem, env(safe-area-inset-right));
  }
  
  .attendance-modal {
    padding-bottom: max(1.5rem, env(safe-area-inset-bottom));
  }
  
  .mobile-attendance-button {
    bottom: max(20px, env(safe-area-inset-bottom));
    right: max(20px, env(safe-area-inset-right));
  }
}
</style>