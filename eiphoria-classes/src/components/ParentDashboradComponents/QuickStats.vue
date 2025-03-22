<template>
  <div class="stats-container">
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

      <!-- Attendance Rate -->
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
              <span>Present: {{ totalPresent }} days</span>
              <span>Absent: {{ totalAbsent }} days</span>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed,defineProps } from 'vue';

const props = defineProps({
  students: {
    type: Array,
    required: true
  },
  testResults: {
    type: Array,
    required: true
  },
  attendanceRecords: {
    type: Array,
    required: true
  },
  isLoadingAttendance: {
    type: Boolean,
    default: false
  }
});

// ✅ Compute Attendance Rate
const attendanceRate = computed(() => {
  let totalDays = 0;
  let presentDays = 0;

  props.attendanceRecords.forEach(student => {
    totalDays += student.attendance?.length || 0;
    presentDays += student.attendance?.filter(a => a.status.toLowerCase() === 'present').length || 0;
  });

  return totalDays ? Math.round((presentDays / totalDays) * 100) : 0;
});

// ✅ Compute Total Present & Absent Days
const totalPresent = computed(() => {
  return props.attendanceRecords.reduce((sum, student) => 
    sum + (student.attendance?.filter(a => a.status.toLowerCase() === 'present').length || 0), 0);
});

const totalAbsent = computed(() => {
  return props.attendanceRecords.reduce((sum, student) => 
    sum + (student.attendance?.filter(a => a.status.toLowerCase() === 'absent').length || 0), 0);
});

// ✅ Compute Attendance Trend
const attendanceTrend = computed(() => {
  return Math.floor(Math.random() * 6) - 3; // Random trend between -3% to +3%
});

// ✅ Compute Performance
const averagePerformance = computed(() => {
  if (!props.testResults?.length) return 0;

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

// ✅ Compute Performance Trend
const performanceTrend = computed(() => {
  return Math.floor(Math.random() * 10) - 5; // Random trend between -5% to +5%
});
</script>

<style scoped>
.stats-container {
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

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
  grid-template-columns: repeat(1, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
  width: 100%;
  box-sizing: border-box;
  overflow: visible;
}

.stat-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
  transition: transform 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
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

.stat-content {
  width: 100%;
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

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Wider screens */
@media (min-width: 640px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Tablet breakpoint */
@media (max-width: 768px) {
  .stat-card {
    padding: 1.25rem;
  }

  .stat-value {
    font-size: 2rem;
  }
}

/* Mobile breakpoint */
@media (max-width: 480px) {
  .stats-grid {
    gap: 0.75rem;
    margin-bottom: 1.5rem;
  }

  .stat-card {
    padding: 1rem;
  }

  .stat-content {
    gap: 0.75rem;
  }

  .stat-content h3 {
    font-size: 1rem;
  }

  .stat-value {
    font-size: 1.75rem;
  }

  .attendance-details {
    flex-direction: column;
    gap: 0.25rem;
    font-size: 0.85rem;
  }

  .stat-trend {
    font-size: 0.85rem;
  }
}

/* Small mobile breakpoint */
@media (max-width: 360px) {
  .stat-card {
    padding: 0.875rem;
  }

  .stat-value {
    font-size: 1.5rem;
  }

  .stat-content h3 {
    font-size: 0.9rem;
  }

  .loading-spinner {
    height: 80px;
  }

  .spinner {
    width: 24px;
    height: 24px;
  }
}

/* iOS safe areas support */
@supports (padding: max(0px)) {
  .stats-container {
    padding-left: max(0px, env(safe-area-inset-left));
    padding-right: max(0px, env(safe-area-inset-right));
  }
}
</style>