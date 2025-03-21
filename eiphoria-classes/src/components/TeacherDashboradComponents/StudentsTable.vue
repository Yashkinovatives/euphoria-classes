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
        <div 
          v-for="student in filteredStudents" 
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
          </div>
          
          <!-- Card body removed as per request to remove Performance and Last Test -->
          <!-- Spacer div to maintain some spacing between header and actions -->
          <div class="spacer"></div>
          
          <div class="card-actions">
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
        </div>
      </div>

      <div v-if="filteredStudents.length === 0" class="no-results">
        <div class="no-results-icon">🔍</div>
        <p>No students found</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps, defineEmits } from 'vue';

// Define props without assigning to a variable
const props = defineProps({
  students: {
    type: Array,
    required: true
  }
});

// Define emits for all the events
defineEmits(['add-test', 'view-details', 'view-results', 'manage-fees', 'manage-attendance']);

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

</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap");

.students-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(75, 150, 243, 0.15);
  border: 1px solid rgba(75, 150, 243, 0.1);
  font-family: "Nunito", sans-serif;
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
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 100px;
  font-size: 0.9rem;
  width: 250px;
  transition: all 0.3s ease;
  font-size: 16px; /* Prevents iOS zoom on focus */
  -webkit-appearance: none; /* Better appearance on iOS */
}

.search-input:focus {
  outline: none;
  border-color: #3178E6;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
}

.class-filter {
  padding: 0.75rem 1.5rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 100px;
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
}

.class-filter:focus {
  outline: none;
  border-color: #3178E6;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
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

/* Performance and test styles removed */
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
  border-radius: 100px;
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

.btn:hover {
  transform: translateY(-2px);
}

.btn:active {
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

.student-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.1);
}

.card-header {
  margin-bottom: 1rem;
}

.spacer {
  margin-bottom: 1.25rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
}

.card-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
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
}

/* Media query removed as Performance and Last Test columns were removed */

@media (max-width: 768px) {
  .section-header {
    flex-direction: column;
    gap: 1.25rem;
    align-items: flex-start;
  }

  .search-filter {
    width: 100%;
    flex-direction: column;
    gap: 0.75rem;
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
  
  .card-actions {
    grid-template-columns: 1fr 1fr;
  }
  
  .card-item {
    padding: 0.5rem 0;
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
  
  .card-actions {
    grid-template-columns: 1fr;
  }
  
  /* Card item styles adjusted */
  
  .search-input, 
  .class-filter {
    padding: 0.7rem 1rem;
    font-size: 0.9rem;
  }
  
  .search-input {
    padding-left: 2.25rem;
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
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .students-section {
    padding-left: max(1.5rem, env(safe-area-inset-left));
    padding-right: max(1.5rem, env(safe-area-inset-right));
  }
}
</style>