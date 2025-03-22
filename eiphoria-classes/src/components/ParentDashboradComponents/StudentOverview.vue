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

      <div class="additional-stats">
        <div class="additional-stat-card tertiary-gradient">
          <div class="stat-content">
            <h4>Completed Assignments</h4>
            <div class="compact-stat-value">45/48</div>
            <div class="progress-bar">
              <div class="progress" style="width: 94%"></div>
            </div>
          </div>
        </div>

        <div class="additional-stat-card quaternary-gradient">
          <div class="stat-content">
            <h4>Next Assessment</h4>
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
    </div>
  </div>
</template>

<script setup>
import { computed ,defineProps} from 'vue';

const props = defineProps({
  students: {
    type: Array,
    required: true
  }
});

const studentActivities = computed(() => {
  return props.students.map(student => ({
    ...student,
    class_section: student.class_section__name || student.class_section
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
  border-radius: 16px;
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
  margin-bottom: 1.5rem;
}

.student-avatar {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 16px;
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
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
}

.additional-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.additional-stat-card {
  background: rgba(255, 255, 255, 0.5);
  border-radius: 12px;
  padding: 1rem;
  transition: transform 0.3s ease;
}

.additional-stat-card:hover {
  transform: translateY(-3px);
}

.tertiary-gradient {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(52, 211, 153, 0.1));
}

.quaternary-gradient {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(251, 191, 36, 0.1));
}

.stat-content h4 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.95rem;
  color: #1e293b;
  margin: 0 0 0.5rem 0;
}

.compact-stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  font-family: 'Space Grotesk', sans-serif;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.progress-bar {
  width: 100%;
  height: 6px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 3px;
  overflow: hidden;
}

.progress {
  height: 100%;
  background: linear-gradient(90deg, #7c3aed, #a855f7);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.upcoming-test {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.test-icon {
  font-size: 1.25rem;
}

.test-info {
  flex: 1;
}

.test-name {
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
  font-size: 0.9rem;
}

.test-date {
  font-size: 0.8rem;
  color: #64748b;
}

@media (max-width: 768px) {
  .student-overview {
    grid-template-columns: 1fr;
  }
  
  .additional-stats {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .student-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }
  
  .status-badge {
    align-self: flex-start;
  }
}
</style>