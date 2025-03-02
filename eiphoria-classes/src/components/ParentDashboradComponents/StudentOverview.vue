# components/StudentOverview.vue
<template>
  <div class="student-overview">
    <div v-for="student in studentActivities" :key="student.id" class="student-card">
        <div class="student-header">
        <div class="student-avatar">
          {{ student.name[0] }}
        </div>
        <div class="student-info">
          <h3>{{ student.name }}</h3>
          <p>{{ student.class_section }}</p>
        </div>
        <div class="status-badge">Active</div>
      </div>

      <div class="student-stats">
        <div class="stat-item">
          <div class="stat-label">Attendance</div>
          <div class="stat-ring">
            <svg width="60" height="60" viewBox="0 0 60 60">
              <circle cx="30" cy="30" r="25" class="stat-ring-bg"/>
              <circle cx="30" cy="30" r="25" class="stat-ring-progress" 
                      :style="{ 'stroke-dashoffset': calculateOffset(96) }"/>
              <text x="30" y="30" class="stat-text">96%</text>
            </svg>
          </div>
        </div>

        <div class="stat-item">
          <div class="stat-label">Assignments</div>
          <div class="stat-ring">
            <svg width="60" height="60" viewBox="0 0 60 60">
              <circle cx="30" cy="30" r="25" class="stat-ring-bg"/>
              <circle cx="30" cy="30" r="25" class="stat-ring-progress" 
                      :style="{ 'stroke-dashoffset': calculateOffset(92) }"/>
              <text x="30" y="30" class="stat-text">92%</text>
            </svg>
          </div>
        </div>

        <div class="stat-item">
          <div class="stat-label">Average</div>
          <div class="stat-ring">
            <svg width="60" height="60" viewBox="0 0 60 60">
              <circle cx="30" cy="30" r="25" class="stat-ring-bg"/>
              <circle cx="30" cy="30" r="25" class="stat-ring-progress" 
                      :style="{ 'stroke-dashoffset': calculateOffset(88) }"/>
              <text x="30" y="30" class="stat-text">88%</text>
            </svg>
          </div>
        </div>
      </div>

      <div class="upcoming-activities">
        <h4>Upcoming Activities</h4>
        <div class="activity-list">
          <div class="activity-item">
            <div class="activity-icon">📚</div>
            <div class="activity-info">
              <h5>Mathematics Test</h5>
              <p>March 15, 2025</p>
            </div>
          </div>
          <div class="activity-item">
            <div class="activity-icon">🏆</div>
            <div class="activity-info">
              <h5>Science Project Due</h5>
              <p>March 20, 2025</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps ,computed} from 'vue';

const props = defineProps({
  students: {
    type: Array,
    required: true
  }
});

const calculateOffset = (percentage) => {
  const circumference = 2 * Math.PI * 25; // r = 25
  return circumference - (percentage / 100) * circumference;
};

const studentActivities = computed(() => {
  return props.students.map(student => ({
    ...student,
    activities: [
      {
        icon: '📚',
        title: 'Mathematics Test',
        date: 'March 15, 2025'
      },
      {
        icon: '🏆',
        title: 'Science Project Due',
        date: 'March 20, 2025'
      }
    ]
  }));
});
</script>

<style scoped>
.student-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.student-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
  transition: transform 0.3s ease;
}

.student-card:hover {
  transform: translateY(-5px);
}

.student-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.student-avatar {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
  font-weight: 600;
}

.student-info {
  flex: 1;
}

.student-info h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.25rem;
  color: #1e293b;
  margin: 0 0 0.25rem 0;
}

.student-info p {
  color: #64748b;
  margin: 0;
}

.status-badge {
  padding: 0.5rem 1rem;
  background: rgba(16, 185, 129, 0.1);
  color: #059669;
  border-radius: 100px;
  font-size: 0.875rem;
  font-weight: 600;
}

.student-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-item {
  text-align: center;
}

.stat-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.stat-ring {
  position: relative;
  display: inline-block;
}

.stat-ring-bg {
  fill: none;
  stroke: rgba(139, 92, 246, 0.1);
  stroke-width: 5;
}

.stat-ring-progress {
  fill: none;
  stroke: #7c3aed;
  stroke-width: 5;
  stroke-linecap: round;
  transform: rotate(-90deg);
  transform-origin: 50% 50%;
  transition: stroke-dashoffset 0.3s ease;
  stroke-dasharray: 157; /* 2 * PI * 25 */
}

.stat-text {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 14px;
  fill: #1e293b;
  text-anchor: middle;
  dominant-baseline: middle;
  font-weight: 600;
}

.upcoming-activities {
  border-top: 1px solid rgba(139, 92, 246, 0.1);
  padding-top: 1.5rem;
}

.upcoming-activities h4 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.1rem;
  color: #1e293b;
  margin: 0 0 1rem 0;
}

.activity-list {
  display: grid;
  gap: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 12px;
  transition: background-color 0.3s ease;
}

.activity-item:hover {
  background: rgba(139, 92, 246, 0.1);
}

.activity-icon {
  font-size: 1.5rem;
}

.activity-info h5 {
  font-size: 1rem;
  color: #1e293b;
  margin: 0 0 0.25rem 0;
}

.activity-info p {
  font-size: 0.875rem;
  color: #64748b;
  margin: 0;
}

@media (max-width: 768px) {
  .student-overview {
    grid-template-columns: 1fr;
  }

  .student-stats {
    gap: 0.5rem;
  }

  .stat-ring svg {
    width: 50px;
    height: 50px;
  }
}
</style>