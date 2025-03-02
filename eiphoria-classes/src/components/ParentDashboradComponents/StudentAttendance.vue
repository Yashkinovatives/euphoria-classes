# components/ParentDashboradComponents/StudentAttendance.vue
<template>
  <div class="attendance-section">
    <div class="section-header">
      <div class="title-badge">
        <span class="badge-icon">📊</span>
        <h2>Attendance Records</h2>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <div class="loading-spinner"></div>
      <p>Loading attendance records...</p>
    </div>

    <div v-else-if="!studentsAttendance || studentsAttendance.length === 0" class="no-data">
      <p>No attendance records found</p>
    </div>

    <div v-else class="attendance-cards">
      <div v-for="studentData in studentsAttendance" :key="studentData.student_id" class="attendance-card">
        <div class="student-info">
          <div class="student-avatar">{{ studentData.student_name[0] }}</div>
          <div class="student-details">
            <h3>{{ studentData.student_name }}</h3>
            <p>{{ studentData.class_section }}</p>
          </div>
        </div>

        <div class="attendance-stats">
          <div class="stat-item">
            <span class="stat-value present">{{ getAttendanceCount(studentData.attendance, 'present') }}</span>
            <span class="stat-label">Present</span>
          </div>
          <div class="stat-item">
            <span class="stat-value absent">{{ getAttendanceCount(studentData.attendance, 'absent') }}</span>
            <span class="stat-label">Absent</span>
          </div>
          <div class="stat-item">
            <span class="stat-value late">{{ getAttendanceCount(studentData.attendance, 'late') }}</span>
            <span class="stat-label">Late</span>
          </div>
        </div>

        <div class="attendance-chart">
          <div class="attendance-rate">
            <span>{{ calculateAttendanceRate(studentData.attendance) }}%</span>
            <span class="rate-label">Attendance Rate</span>
          </div>
          <div class="chart-bar">
            <div 
              class="progress" 
              :style="{ width: calculateAttendanceRate(studentData.attendance) + '%' }"
            ></div>
          </div>
        </div>

        <div class="attendance-history">
          <h4>Recent Attendance</h4>
          <div class="history-list">
            <div v-if="studentData.attendance.length === 0" class="no-records">
              No attendance records yet
            </div>
            <div 
              v-else
              v-for="record in getRecentAttendance(studentData.attendance)" 
              :key="record.date"
              class="history-item"
            >
              <div class="record-date">
                {{ formatDate(record.date) }}
              </div>
              <div class="record-status">
                <span class="status-badge" :class="record.status">
                  {{ record.status.charAt(0).toUpperCase() + record.status.slice(1) }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  studentsAttendance: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  }
});

const getAttendanceCount = (attendance, status) => {
  if (!attendance || !Array.isArray(attendance)) return 0;
  return attendance.filter(record => record.status === status).length;
};

const getRecentAttendance = (attendance) => {
  if (!attendance || !Array.isArray(attendance)) return [];
  
  // Sort attendance by date (newest first) and take the 5 most recent
  return [...attendance]
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .slice(0, 5);
};

const calculateAttendanceRate = (attendance) => {
  if (!attendance || !Array.isArray(attendance) || attendance.length === 0) return 0;
  
  const presentDays = getAttendanceCount(attendance, 'present');
  const lateDays = getAttendanceCount(attendance, 'late');
  const totalDays = attendance.length;
  
  // Count late as half-present (customize as needed)
  return Math.round(((presentDays + (lateDays * 0.5)) / totalDays) * 100);
};

const formatDate = (dateString) => {
  const options = { weekday: 'short', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>

<style scoped>
.attendance-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
}

.section-header {
  margin-bottom: 1.5rem;
}

.title-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.badge-icon {
  font-size: 1.5rem;
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  margin: 0;
  color: #1e293b;
}

.loading, .no-data {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #64748b;
  text-align: center;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(139, 92, 246, 0.1);
  border-top-color: #7c3aed;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.attendance-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.attendance-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(139, 92, 246, 0.1);
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.25rem;
}

.student-details h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #1e293b;
}

.student-details p {
  margin: 0.25rem 0 0;
  font-size: 0.9rem;
  color: #64748b;
}

.attendance-stats {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  background: #f8f7ff;
  padding: 1rem;
  border-radius: 12px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
}

.stat-value.present { color: #16a34a; }
.stat-value.absent { color: #dc2626; }
.stat-value.late { color: #eab308; }

.stat-label {
  font-size: 0.85rem;
  color: #64748b;
}

.attendance-chart {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.attendance-rate {
  display: flex;
  flex-direction: column;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
}

.rate-label {
  font-size: 0.85rem;
  color: #64748b;
  font-weight: 400;
}

.chart-bar {
  flex: 1;
  height: 10px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 5px;
  overflow: hidden;
}

.progress {
  height: 100%;
  background: linear-gradient(90deg, #7c3aed, #a855f7);
  border-radius: 5px;
  transition: width 0.3s ease;
}

.attendance-history h4 {
  font-size: 1rem;
  color: #1e293b;
  margin: 0 0 1rem;
}

.history-list {
  display: grid;
  gap: 0.75rem;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 8px;
}

.record-date {
  font-weight: 500;
  color: #1e293b;
}

.status-badge {
  padding: 0.35rem 0.75rem;
  border-radius: 100px;
  font-size: 0.8rem;
  font-weight: 600;
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

.no-records {
  text-align: center;
  padding: 1rem;
  color: #64748b;
  font-size: 0.9rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 8px;
}

@media (max-width: 768px) {
  .attendance-section {
    padding: 1rem;
  }

  .attendance-card {
    padding: 1rem;
  }

  .attendance-stats {
    padding: 0.75rem;
  }

  .stat-value {
    font-size: 1.25rem;
  }

  .attendance-chart {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .chart-bar {
    width: 100%;
  }
}
</style>