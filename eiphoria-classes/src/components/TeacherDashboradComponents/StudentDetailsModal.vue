# components/StudentDetailsModal.vue
<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <!-- Student Header -->
      <div class="student-header">
        <div class="student-profile">
          <div class="student-avatar">{{ student.name[0] }}</div>
          <div class="student-info">
            <h2>{{ student.name }}</h2>
            <p class="student-class">{{ student.class_section__name }}</p>
          </div>
        </div>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>

      <!-- Performance Overview -->
      <div class="performance-overview">
        <div class="overview-card">
          <div class="overview-label">Average Score</div>
          <div class="overview-value" :class="getPerformanceClass(student.average_score)">
            {{ student.average_score ? student.average_score.toFixed(1) + '%' : 'N/A' }}
          </div>
          <div class="progress-bar" v-if="student.average_score">
            <div 
              class="progress" 
              :style="{ 
                width: `${student.average_score}%`,
                backgroundColor: getProgressColor(student.average_score)
              }"
            ></div>
          </div>
        </div>

        <div class="overview-card">
          <div class="overview-label">Total Tests</div>
          <div class="overview-value">
            {{ student.test_results?.length || 0 }}
          </div>
        </div>

        <div class="overview-card">
          <div class="overview-label">Highest Score</div>
          <div class="overview-value excellent">
            {{ highestScore }}%
          </div>
        </div>
      </div>

      <!-- Test Results -->
      <div class="test-results">
        <h3>Test History</h3>
        
        <div v-if="student.test_results && student.test_results.length" class="results-list">
          <div 
            v-for="result in sortedTestResults" 
            :key="result.id"
            class="result-card"
          >
            <div class="result-header">
              <div class="subject">{{ result.subject }}</div>
              <div class="date">{{ formatDate(result.created_at) }}</div>
            </div>
            
            <div class="score-details">
              <div class="marks">
                {{ result.marks_obtained }} / {{ result.total_marks }}
              </div>
              <div 
                class="percentage" 
                :class="getPerformanceClass(calculatePercentage(result))"
              >
                {{ calculatePercentage(result) }}%
              </div>
            </div>

            <div class="progress-bar">
              <div 
                class="progress" 
                :style="{ 
                  width: `${calculatePercentage(result)}%`,
                  backgroundColor: getProgressColor(calculatePercentage(result))
                }"
              ></div>
            </div>
          </div>
        </div>

        <div v-else class="no-results">
          <div class="no-results-icon">📝</div>
          <p>No test results available yet</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed,defineProps } from 'vue';

const props = defineProps({
  student: {
    type: Object,
    required: true
  }
});

const sortedTestResults = computed(() => {
  if (!props.student.test_results) return [];
  return [...props.student.test_results].sort((a, b) => 
    new Date(b.created_at) - new Date(a.created_at)
  );
});

const highestScore = computed(() => {
  if (!props.student.test_results?.length) return 0;
  return Math.max(...props.student.test_results.map(result => 
    calculatePercentage(result)
  ));
});

const calculatePercentage = (result) => {
  return Math.round((result.marks_obtained / result.total_marks) * 100);
};

const getPerformanceClass = (score) => {
  if (!score && score !== 0) return '';
  if (score >= 80) return 'excellent';
  if (score >= 60) return 'good';
  if (score >= 40) return 'average';
  return 'poor';
};

const getProgressColor = (score) => {
  if (score >= 80) return '#10b981';
  if (score >= 60) return '#3b82f6';
  if (score >= 40) return '#f59e0b';
  return '#ef4444';
};

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  });
};
</script>

# components/StudentDetailsModal.vue (continued with styles)

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 24px;
  width: 90%;
  max-width: 600px;
  max-height: 85vh;
  overflow-y: auto;
  position: relative;
  animation: modalSlide 0.3s ease;
}

@keyframes modalSlide {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.student-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(139, 92, 246, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(135deg, rgba(124, 58, 237, 0.1), rgba(139, 92, 246, 0.1));
}

.student-profile {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: 600;
}

.student-info h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  color: #1e293b;
  margin: 0;
}

.student-class {
  color: #64748b;
  margin: 0.25rem 0 0 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #64748b;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(139, 92, 246, 0.1);
  color: #7c3aed;
}

.performance-overview {
  padding: 1.5rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.overview-card {
  background: rgba(139, 92, 246, 0.05);
  padding: 1rem;
  border-radius: 16px;
  text-align: center;
}

.overview-label {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.overview-value {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
}

.overview-value.excellent { color: #10b981; }
.overview-value.good { color: #3b82f6; }
.overview-value.average { color: #f59e0b; }
.overview-value.poor { color: #ef4444; }

.progress-bar {
  width: 100%;
  height: 6px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 3px;
  overflow: hidden;
  margin-top: 0.75rem;
}

.progress {
  height: 100%;
  border-radius: 3px;
  transition: width 0.3s ease;
}

.test-results {
  padding: 1.5rem;
}

.test-results h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.25rem;
  color: #1e293b;
  margin: 0 0 1.5rem 0;
}

.results-list {
  display: grid;
  gap: 1rem;
}

.result-card {
  background: rgba(139, 92, 246, 0.05);
  padding: 1rem;
  border-radius: 16px;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.subject {
  font-weight: 600;
  color: #1e293b;
}

.date {
  color: #64748b;
  font-size: 0.9rem;
}

.score-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.marks {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  color: #1e293b;
}

.percentage {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
}

.percentage.excellent { color: #10b981; }
.percentage.good { color: #3b82f6; }
.percentage.average { color: #f59e0b; }
.percentage.poor { color: #ef4444; }

.no-results {
  text-align: center;
  padding: 3rem;
  color: #64748b;
}

.no-results-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

@media (max-width: 768px) {
  .modal-content {
    width: 95%;
    margin: 1rem;
    max-height: 80vh;
  }

  .performance-overview {
    grid-template-columns: 1fr;
  }

  .student-header {
    padding: 1rem;
  }

  .student-avatar {
    width: 48px;
    height: 48px;
    font-size: 1.25rem;
  }

  .student-info h2 {
    font-size: 1.25rem;
  }
}
</style>