# AttendanceModal.vue
<template>
  <div class="modal-backdrop">
    <div class="modal-content">
      <div class="modal-header">
        <div class="student-info">
          <div class="student-avatar">{{ student.name[0] }}</div>
          <div>
            <h3>Manage Attendance</h3>
            <p class="student-name">{{ student.name }}</p>
          </div>
        </div>
        <button @click="$emit('close')" class="close-btn">×</button>
      </div>

      <div class="modal-body">
        <!-- Success Message -->
        <div v-if="successMessage" class="success-message">
          {{ successMessage }}
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>

        <!-- Mark Attendance Form -->
        <div class="attendance-form">
          <h4>Mark Attendance</h4>
          
          <div class="form-group">
            <label for="attendance-date">Date</label>
            <input 
              id="attendance-date"
              type="date" 
              v-model="attendanceDate"
              class="date-input"
              :max="today"
            />
          </div>

          <div class="form-group">
            <label>Status</label>
            <div class="status-options">
              <button 
                type="button"
                class="status-btn present"
                :class="{ active: attendanceStatus === 'present' }"
                @click="attendanceStatus = 'present'"
              >
                <span class="status-icon">✓</span>
                <span>Present</span>
              </button>
              
              <button 
                type="button"
                class="status-btn absent"
                :class="{ active: attendanceStatus === 'absent' }"
                @click="attendanceStatus = 'absent'"
              >
                <span class="status-icon">✗</span>
                <span>Absent</span>
              </button>
              
            </div>
          </div>

          <div class="form-actions">
            <button 
              @click="markAttendance"
              :disabled="!isFormValid || isSubmitting"
              class="submit-btn"
            >
              <span v-if="isSubmitting">Processing...</span>
              <span v-else>Mark Attendance</span>
            </button>
          </div>
        </div>

        <!-- Attendance History -->
        <div class="attendance-history">
          <h4>Attendance History</h4>
          
          <div v-if="isLoadingHistory" class="loading-history">
            Loading attendance records...
          </div>
          
          <div v-else-if="attendanceHistory.length === 0" class="no-history">
            No attendance records found
          </div>
          
          <div v-else class="history-list">
            <div 
              v-for="record in attendanceHistory" 
              :key="record.date"
              class="history-item"
              :class="getStatusClass(record.status)"
            >
              <div class="history-date">
                {{ formatDate(record.date) }}
              </div>
              
              <div class="history-status">
                <span class="status-badge" :class="record.status">
                  {{ record.status.charAt(0).toUpperCase() + record.status.slice(1) }}
                </span>
              </div>
              
              <div class="history-actions">
                <button
                  @click="prepareUpdateAttendance(record)"
                  class="edit-btn"
                  title="Edit this attendance record"
                >
                  <span>Edit</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, defineProps, defineEmits } from 'vue';
import axios from 'axios';

const props = defineProps({
  student: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['close', 'update']);

const attendanceDate = ref(new Date().toISOString().slice(0, 10)); // Today's date in YYYY-MM-DD format
const attendanceStatus = ref('present');
const successMessage = ref('');
const errorMessage = ref('');
const isSubmitting = ref(false);
const attendanceHistory = ref([]);
const isLoadingHistory = ref(false);
const isEditing = ref(false);
const editingRecordDate = ref(null);

const today = computed(() => new Date().toISOString().slice(0, 10));

const isFormValid = computed(() => {
  return attendanceDate.value && attendanceStatus.value;
});

onMounted(() => {
  fetchAttendanceHistory();
});

const fetchAttendanceHistory = async () => {
  try {
    isLoadingHistory.value = true;
    const token = localStorage.getItem('access_token');
    
    if (!token) {
      console.error('No authentication token found in localStorage');
      errorMessage.value = 'Authentication error. Please try logging in again.';
      return;
    }
    
    console.log('Using token:', token);
    console.log('Fetching attendance for student ID:', props.student.id);
    
    // Updated API endpoint
    const response = await axios.get(`http://127.0.0.1:8000/api/parent/student-attendance/`, {
      params: { student_id: props.student.id },
      headers: { 
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });
    
    console.log('Attendance API response:', response.data);
    attendanceHistory.value = response.data.attendance || [];
  } catch (error) {
    console.error('Error fetching attendance history:', error);
    console.error('Error response:', error.response?.data);
    console.error('Error status:', error.response?.status);
    
    if (error.response?.status === 401) {
      errorMessage.value = 'Your session has expired. Please log in again.';
    } else {
      errorMessage.value = 'Failed to load attendance history.';
    }
  } finally {
    isLoadingHistory.value = false;
  }
};

const markAttendance = async () => {
  try {
    isSubmitting.value = true;
    errorMessage.value = '';
    
    const token = localStorage.getItem('access_token');
    const endpoint = isEditing.value 
  ? 'http://127.0.0.1:8000/api/teacher/update-attendance/'
  : 'http://127.0.0.1:8000/api/teacher/mark-attendance/';
    
    const payload = {
      student_id: props.student.id,
      date: attendanceDate.value,
      status: attendanceStatus.value
    };
    
    await axios.post(endpoint, payload, {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    successMessage.value = isEditing.value 
      ? "Attendance updated successfully!"
      : "Attendance marked successfully!";
    
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
    
    // Reset form
    if (!isEditing.value) {
      attendanceDate.value = today.value;
    }
    
    attendanceStatus.value = 'present';
    isEditing.value = false;
    editingRecordDate.value = null;
    
    // Refresh history
    await fetchAttendanceHistory();
    
    // Notify parent component
    emit('update');
  } catch (error) {
    console.error('Error marking attendance:', error);
    errorMessage.value = error.response?.data?.error || 
                          (isEditing.value ? "Failed to update attendance" : "Failed to mark attendance");
    
    setTimeout(() => {
      errorMessage.value = '';
    }, 3000);
  } finally {
    isSubmitting.value = false;
  }
};

const prepareUpdateAttendance = (record) => {
  attendanceDate.value = record.date;
  attendanceStatus.value = record.status;
  isEditing.value = true;
  editingRecordDate.value = record.date;
};

const getStatusClass = (status) => {
  return {
    'present-record': status === 'present',
    'absent-record': status === 'absent',
    'late-record': status === 'late'
  };
};

const formatDate = (dateString) => {
  const options = { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
  font-family: 'Inter', sans-serif;
}

.modal-header {
  padding: 1.25rem;
  border-bottom: 1px solid #E2E8F0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}

.student-avatar {
  width: 44px;
  height: 44px;
  background: #4B96F3;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.25rem;
  font-weight: 600;
  text-transform: uppercase;
}

.modal-header h3 {
  margin: 0;
  color: #4A5568;
  font-size: 1.25rem;
  font-weight: 600;
}

.student-name {
  color: #718096;
  margin: 0.25rem 0 0 0;
  font-size: 0.875rem;
  font-weight: 400;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #718096;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 0.75;
}

.modal-body {
  padding: 1.25rem;
}

.success-message {
  background-color: rgba(34, 197, 94, 0.15);
  color: rgb(22, 163, 74);
  padding: 0.75rem 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
  font-weight: 500;
  animation: fadeIn 0.3s;
  font-size: 0.95rem;
}

.error-message {
  background-color: rgba(239, 68, 68, 0.15);
  color: rgb(220, 38, 38);
  padding: 0.75rem 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
  font-weight: 500;
  animation: fadeIn 0.3s;
  font-size: 0.95rem;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.attendance-form, .attendance-history {
  background: #F8FAFC;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.25rem;
  border: 1px solid #E2E8F0;
}

h4 {
  color: #2D3748;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1rem;
  font-weight: 600;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #4A5568;
  font-size: 0.95rem;
}

.date-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 0.95rem;
  background-color: white;
  color: #4A5568;
  font-family: 'Inter', sans-serif;
}

.date-input:focus {
  outline: none;
  border-color: #4B96F3;
}

.status-options {
  display: flex;
  gap: 0.75rem;
}

.status-btn {
  flex: 1;
  padding: 0.75rem;
  border: 1px solid;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
  background: white;
  font-size: 0.9rem;
}

.status-btn.present {
  border-color: rgba(22, 163, 74, 0.3);
  color: #16a34a;
}

.status-btn.absent {
  border-color: rgba(220, 38, 38, 0.3);
  color: #dc2626;
}

.status-btn.late {
  border-color: rgba(234, 179, 8, 0.3);
  color: #eab308;
}

.status-btn.active {
  transform: scale(1.05);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.status-btn.present.active {
  background: rgba(22, 163, 74, 0.15);
}

.status-btn.absent.active {
  background: rgba(220, 38, 38, 0.15);
}

.status-btn.late.active {
  background: rgba(234, 179, 8, 0.15);
}

.status-icon {
  font-size: 1.25rem;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
}

.submit-btn {
  padding: 0.75rem 1.25rem;
  background: #4B96F3;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.95rem;
  font-family: 'Inter', sans-serif;
}

.submit-btn:hover:not(:disabled) {
  background: #3178E6;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.loading-history, .no-history {
  text-align: center;
  padding: 1rem;
  color: #718096;
  background: #F8FAFC;
  border-radius: 8px;
  border: 1px solid #E2E8F0;
  font-size: 0.95rem;
}

.history-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  background: white;
  border-left: 4px solid transparent;
  border: 1px solid #E2E8F0;
}

.present-record {
  border-left-color: #16a34a;
}

.absent-record {
  border-left-color: #dc2626;
}

.late-record {
  border-left-color: #eab308;
}

.history-date {
  font-weight: 500;
  color: #4A5568;
  font-size: 0.95rem;
}

.status-badge {
  padding: 0.35rem 0.75rem;
  border-radius: 100px;
  font-size: 0.8rem;
  font-weight: 500;
}

.status-badge.present {
  background: rgba(22, 163, 74, 0.15);
  color: #16a34a;
}

.status-badge.absent {
  background: rgba(220, 38, 38, 0.15);
  color: #dc2626;
}

.status-badge.late {
  background: rgba(234, 179, 8, 0.15);
  color: #eab308;
}

.edit-btn {
  background: rgba(75, 150, 243, 0.1);
  color: #4B96F3;
  border: none;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.edit-btn:hover {
  background: rgba(75, 150, 243, 0.2);
}

@media (max-width: 640px) {
  .status-options {
    flex-direction: column;
  }
  
  .history-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .history-actions {
    align-self: flex-end;
  }
}
</style>