# components/ParentDashboardComponents/QuickStats.vue
<template>
  <div class="stats-grid">
    <!-- Overall Performance -->
    <div class="stat-card primary-gradient">
      <div class="stat-content">
        <h3>Overall Performance</h3>
        <div class="stat-value">{{ averagePerformance }}%</div>
        <div class="stat-trend" :class="{ 'positive': performanceTrend >= 0 }">
          <span class="trend-icon">{{ performanceTrend >= 0 ? '↑' : '↓' }}</span>
          <span>{{ Math.abs(performanceTrend) }}% from last term</span>
        </div>
      </div>
    </div>

    <!-- Attendance -->
    <div class="stat-card secondary-gradient">
      <div class="stat-content">
        <h3>Attendance Rate</h3>
        <div v-if="isLoadingAttendance" class="loading-spinner">
          <div class="spinner"></div>
        </div>
        <template v-else>
          <div class="stat-value">{{ attendanceRate }}%</div>
          <div class="stat-trend" :class="{ 'positive': attendanceTrend >= 0 }">
            <span class="trend-icon">{{ attendanceTrend >= 0 ? '↑' : '↓' }}</span>
            <span>{{ Math.abs(attendanceTrend) }}% this month</span>
          </div>
          <div class="attendance-details">
            <span>Present: {{ presentDays }} days</span>
            <span>Absent: {{ absentDays }} days</span>
          </div>
        </template>
      </div>
    </div>

    <!-- Completed Assignments -->
    <div class="stat-card tertiary-gradient">
      <div class="stat-content">
        <h3>Completed Assignments</h3>
        <div class="stat-value">45/48</div>
        <div class="progress-bar">
          <div class="progress" style="width: 94%"></div>
        </div>
      </div>
    </div>

    <!-- Next Assessment -->
    <div class="stat-card quaternary-gradient">
      <div class="stat-content">
        <h3>Next Assessment</h3>
        <div class="upcoming-test">
          <span class="test-icon">📝</span>
          <div class="test-info">
            <div class="test-name">Mathematics</div>
            <div class="test-date">March 15, 2025</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted ,defineProps} from 'vue';
import axios from 'axios';

const props = defineProps({
  students: {
    type: Array,
    required: true
  },
  testResults: {
    type: Array,
    required: true
  }
});

// Attendance Data State
const attendanceData = ref(null);
const isLoadingAttendance = ref(true);
const attendanceError = ref(null);

// Fetch Attendance Data
const fetchAttendanceData = async () => {
  try {
    isLoadingAttendance.value = true;
    const response = await axios.get('http://127.0.0.1:8000/api/parent/student-attendance/', {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` }
    });
    attendanceData.value = response.data;
    console.log('data',attendanceData.value);
  } catch (error) {
    console.error('Error fetching attendance:', error);
    attendanceError.value = error;
  } finally {
    isLoadingAttendance.value = false;
  }
};

// Computed Properties for Attendance
const attendanceRate = computed(() => {
  if (!attendanceData.value) return 0;
  const totalDays = attendanceData.value.present_days + attendanceData.value.absent_days;
  return totalDays ? Math.round((attendanceData.value.present_days / totalDays) * 100) : 0;
});

const presentDays = computed(() => {
  return attendanceData.value?.present_days || 0;
});

const absentDays = computed(() => {
  return attendanceData.value?.absent_days || 0;
});

const attendanceTrend = computed(() => {
  if (!attendanceData.value?.trend) return 0;
  return attendanceData.value.trend;
});

// Performance computations (from your existing code)
const averagePerformance = computed(() => {
  if (!props.testResults.length) return 0;
  
  let totalScore = 0;
  let totalTests = 0;
  
  props.testResults.forEach(student => {
    student.results?.forEach(result => {
      totalScore += (result.marks_obtained / result.total_marks) * 100;
      totalTests++;
    });
  });
  
  return totalTests ? Math.round(totalScore / totalTests) : 0;
});

const performanceTrend = computed(() => {
  const currentAvg = averagePerformance.value;
  const previousAvg = props.testResults.length ? 85 : currentAvg;
  return +(currentAvg - previousAvg).toFixed(1);
});

// Fetch data on component mount
onMounted(() => {
  fetchAttendanceData();
});
</script>

<style scoped>
.attendance-details {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
  color: #64748b;
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid rgba(139, 92, 246, 0.1);
}
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
.spinner {
  width: 30px;
  height: 30px;
  border: 3px solid rgba(139, 92, 246, 0.1);
  border-top-color: #7c3aed;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.primary-gradient {
  background: linear-gradient(135deg, rgba(124, 58, 237, 0.1), rgba(139, 92, 246, 0.1));
}

.secondary-gradient {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(96, 165, 250, 0.1));
}

.tertiary-gradient {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(52, 211, 153, 0.1));
}

.quaternary-gradient {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(251, 191, 36, 0.1));
}

.stat-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.stat-content h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.1rem;
  color: #1e293b;
  margin: 0;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  font-family: 'Space Grotesk', sans-serif;
  color: #1e293b;
}

.stat-trend {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: #ef4444;
}

.stat-trend.positive {
  color: #10b981;
}

.trend-icon {
  font-size: 1.2rem;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 4px;
  overflow: hidden;
}

.progress {
  height: 100%;
  background: linear-gradient(90deg, #7c3aed, #a855f7);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.upcoming-test {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(255, 255, 255, 0.5);
  padding: 1rem;
  border-radius: 12px;
}

.test-icon {
  font-size: 1.5rem;
}

.test-info {
  flex: 1;
}

.test-name {
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.test-date {
  font-size: 0.9rem;
  color: #64748b;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .stat-card {
    margin-bottom: 1rem;
  }

  .stat-value {
    font-size: 2rem;
  }
}
</style>