# components/TeacherStats.vue
<template>
  <div class="stats-grid">
    <!-- Total Students -->
    <div class="stat-card primary-gradient">
      <div class="stat-content">
        <h3>Total Students</h3>
        <div class="stat-value">{{ totalStudents }}</div>
        <div class="stat-icon">👥</div>
      </div>
    </div>

    <!-- Class Average -->
    <div class="stat-card secondary-gradient">
      <div class="stat-content">
        <h3>Class Average</h3>
        <div class="stat-value">{{ classAverage }}%</div>
        <div class="progress-bar">
          <div class="progress" :style="{ width: `${classAverage}%` }"></div>
        </div>
      </div>
    </div>

    <!-- Top Performers -->
    <div class="stat-card tertiary-gradient">
      <div class="stat-content">
        <h3>Top Performers</h3>
        <div class="stat-value">{{ topPerformers }}</div>
        <div class="performance-text">Above 80%</div>
      </div>
    </div>

    <!-- Needs Attention -->
    <div class="stat-card quaternary-gradient">
      <div class="stat-content">
        <h3>Needs Attention</h3>
        <div class="stat-value">{{ needsAttention }}</div>
        <div class="performance-text">Below 40%</div>
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
  }
});

const totalStudents = computed(() => props.students.length);

const classAverage = computed(() => {
  if (!props.students.length) return 0;
  const validScores = props.students.filter(s => s.average_score !== null);
  if (!validScores.length) return 0;
  const total = validScores.reduce((sum, student) => sum + student.average_score, 0);
  return Math.round(total / validScores.length);
});

const topPerformers = computed(() => {
  return props.students.filter(s => s.average_score >= 80).length;
});

const needsAttention = computed(() => {
  return props.students.filter(s => s.average_score < 40 && s.average_score !== null).length;
});
</script>

<style scoped>
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
  position: relative;
  height: 100%;
}

.stat-content h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.1rem;
  color: #1e293b;
  margin: 0 0 1rem 0;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  font-family: 'Space Grotesk', sans-serif;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.stat-icon {
  position: absolute;
  top: 0;
  right: 0;
  font-size: 2rem;
  opacity: 0.8;
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

.performance-text {
  color: #64748b;
  font-size: 0.9rem;
}
</style>