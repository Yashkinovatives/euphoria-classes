# components/AddTestModal.vue
<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <div class="student-info">
          <div class="student-avatar">{{ student.name[0] }}</div>
          <div>
            <h2>Add Test Result</h2>
            <p class="student-name">{{ student.name }}</p>
          </div>
        </div>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>

      <form @submit.prevent="handleSubmit" class="test-form">
        <div class="form-group">
          <label>Subject</label>
          <input 
            type="text" 
            v-model="formData.subject" 
            required 
            placeholder="Enter subject name"
          />
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label>Marks Obtained</label>
            <input 
              type="number" 
              v-model.number="formData.marks_obtained" 
              required 
              min="0"
              placeholder="Enter marks"
            />
          </div>

          <div class="form-group">
            <label>Total Marks</label>
            <input 
              type="number" 
              v-model.number="formData.total_marks" 
              required 
              min="1"
              placeholder="Enter total"
            />
          </div>
        </div>

        <div class="score-preview" v-if="showScorePreview">
          <div class="preview-label">Score Preview:</div>
          <div class="preview-score" :class="getScoreClass">
            {{ calculatePercentage }}%
          </div>
        </div>

        <div class="form-actions">
          <button type="button" class="btn-cancel" @click="$emit('close')">
            Cancel
          </button>
          <button type="submit" class="btn-submit" :disabled="!isValidForm">
            Save Test Result
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed ,defineEmits,defineProps} from 'vue';

// Replace props declaration with defineProps
defineProps({
  student: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['close', 'submit']);

const formData = ref({
  subject: '',
  marks_obtained: null,
  total_marks: null
});

const isValidForm = computed(() => {
  return formData.value.subject &&
         formData.value.marks_obtained !== null &&
         formData.value.total_marks > 0 &&
         formData.value.marks_obtained <= formData.value.total_marks;
});

const showScorePreview = computed(() => {
  return formData.value.marks_obtained !== null && 
         formData.value.total_marks > 0;
});

const calculatePercentage = computed(() => {
  if (!showScorePreview.value) return 0;
  return Math.round((formData.value.marks_obtained / formData.value.total_marks) * 100);
});

const getScoreClass = computed(() => {
  const score = calculatePercentage.value;
  if (score >= 80) return 'excellent';
  if (score >= 60) return 'good';
  if (score >= 40) return 'average';
  return 'poor';
});

const handleSubmit = () => {
  if (!isValidForm.value) return;
  emit('submit', { ...formData.value });
};
</script>

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
  max-width: 500px;
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

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(139, 92, 246, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.25rem;
  font-weight: 600;
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  color: #1e293b;
  margin: 0;
}

.student-name {
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

.test-form {
  padding: 1.5rem;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  font-weight: 500;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(139, 92, 246, 0.2);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #7c3aed;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.score-preview {
  background: rgba(139, 92, 246, 0.05);
  padding: 1rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.preview-label {
  color: #64748b;
  font-weight: 500;
}

.preview-score {
  font-size: 1.25rem;
  font-weight: 600;
  font-family: 'Space Grotesk', sans-serif;
}

.preview-score.excellent { color: #10b981; }
.preview-score.good { color: #3b82f6; }
.preview-score.average { color: #f59e0b; }
.preview-score.poor { color: #ef4444; }

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-cancel, .btn-submit {
  flex: 1;
  padding: 0.75rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-cancel {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.btn-submit {
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: white;
  border: none;
}

.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-cancel:hover, .btn-submit:not(:disabled):hover {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .modal-content {
    width: 95%;
    margin: 1rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column;
  }
}
</style>