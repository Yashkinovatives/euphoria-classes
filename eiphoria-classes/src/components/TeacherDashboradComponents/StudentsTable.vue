# components/StudentsTable.vue
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
      </div>
    </div>

    <div class="table-container">
      <table class="students-table">
        <thead>
          <tr>
            <th>Student</th>
            <th>Class</th>
            <th>Performance</th>
            <th>Last Test</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="student in filteredStudents" 
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
            <td>{{ student.class_section__name }}</td>
            <td>
              <div class="performance-indicator">
                <div class="score" :class="getPerformanceClass(student.average_score)">
                  {{ student.average_score ? student.average_score.toFixed(1) + '%' : 'N/A' }}
                </div>
                <div 
                  class="progress-bar"
                  v-if="student.average_score"
                >
                  <div 
                    class="progress" 
                    :style="{ 
                      width: `${student.average_score}%`,
                      backgroundColor: getProgressColor(student.average_score)
                    }"
                  ></div>
                </div>
              </div>
            </td>
            <td>
              <div class="last-test" v-if="student.latest_test">
                {{ student.latest_test.subject }}<br>
                <span class="test-date">{{ formatDate(student.latest_test.date) }}</span>
              </div>
              <span v-else class="no-test">No tests yet</span>
            </td>
            <td>
              <div class="action-buttons">
                <button 
                  @click="$emit('add-test', student)"
                  class="btn btn-primary"
                >
                  <span>📝</span> Add Test
                </button>
                <button @click="$emit('view-results', student)">View</button>

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

      <div v-if="filteredStudents.length === 0" class="no-results">
        <div class="no-results-icon">🔍</div>
        <p>No students found</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed ,defineProps,defineEmits} from 'vue';

// Define props without assigning to a variable
const props = defineProps({
  students: {
    type: Array,
    required: true
  }
});

// Define emits for all the events
defineEmits(['add-test', 'view-details', 'manage-fees', 'manage-attendance']);

const searchQuery = ref('');
const selectedClass = ref('');

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

const getPerformanceClass = (score) => {
  if (!score && score !== 0) return 'na';
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
    month: 'short',
    day: 'numeric'
  });
};
</script>

<style scoped>
.students-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
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
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  margin: 0;
  color: #1e293b;
}

.badge-icon {
  font-size: 1.5rem;
}

.search-filter {
  display: flex;
  gap: 1rem;
}

.search-box {
  position: relative;
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
  border: 1px solid rgba(139, 92, 246, 0.2);
  border-radius: 100px;
  font-size: 0.9rem;
  width: 250px;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #7c3aed;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

.class-filter {
  padding: 0.75rem 1.5rem;
  border: 1px solid rgba(139, 92, 246, 0.2);
  border-radius: 100px;
  font-size: 0.9rem;
  color: #1e293b;
  background: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.class-filter:focus {
  outline: none;
  border-color: #7c3aed;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

.table-container {
  overflow-x: auto;
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
  border-bottom: 1px solid rgba(139, 92, 246, 0.1);
}

.student-row {
  background: white;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.student-row:hover {
  transform: translateY(-2px);
}

.student-row td {
  padding: 1rem;
  vertical-align: middle;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
}

.student-details {
  display: flex;
  flex-direction: column;
}

.student-name {
  font-weight: 600;
  color: #1e293b;
}

.student-id {
  font-size: 0.85rem;
  color: #64748b;
}

.performance-indicator {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.score {
  font-weight: 600;
}

.score.excellent { color: #10b981; }
.score.good { color: #3b82f6; }
.score.average { color: #f59e0b; }
.score.poor { color: #ef4444; }
.score.na { color: #64748b; }

.progress-bar {
  width: 100px;
  height: 6px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 3px;
  overflow: hidden;
}

.progress {
  height: 100%;
  border-radius: 3px;
  transition: width 0.3s ease;
}

.last-test {
  font-size: 0.9rem;
}

.test-date {
  color: #64748b;
  font-size: 0.85rem;
}

.no-test {
  color: #64748b;
  font-size: 0.9rem;
}

.action-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 100px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: white;
}

.btn-secondary {
  background: rgba(139, 92, 246, 0.1);
  color: #7c3aed;
}

.btn-tertiary {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.btn-attendance {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.btn:hover {
  transform: translateY(-2px);
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

@media (max-width: 768px) {
  .section-header {
    flex-direction: column;
    gap: 1rem;
  }

  .search-filter {
    width: 100%;
    flex-direction: column;
  }

  .search-input,
  .class-filter {
    width: 100%;
  }

  .action-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
  }
}

@media (max-width: 480px) {
  .action-buttons {
    grid-template-columns: 1fr;
  }
}
</style>