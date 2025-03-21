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
          <label for="subject">Subject</label>
          <input 
            id="subject"
            type="text" 
            v-model="formData.subject" 
            required 
            placeholder="Enter subject name"
          />
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label for="marks_obtained">Marks Obtained</label>
            <input 
              id="marks_obtained"
              type="number" 
              v-model.number="formData.marks_obtained" 
              required 
              min="0"
              placeholder="Enter marks"
            />
          </div>

          <div class="form-group">
            <label for="total_marks">Total Marks</label>
            <input 
              id="total_marks"
              type="number" 
              v-model.number="formData.total_marks" 
              required 
              min="1"
              placeholder="Enter total"
            />
          </div>
        </div>

        <div class="score-preview" v-if="showScorePreview">
          <div class="preview-label">Score Preview</div>
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
import { ref, computed, defineEmits, defineProps } from 'vue';

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
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

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
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 90%;
  max-width: 500px;
  position: relative;
  animation: modalSlide 0.3s ease;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  overflow: hidden;
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
  padding: 1.5rem 2rem;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #F8FAFC;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.25rem;
  font-weight: 600;
  text-transform: uppercase;
}

h2 {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.5rem;
  color: #2D3748;
  margin: 0;
  font-weight: 700;
}

.student-name {
  color: #4A5568;
  margin: 0.25rem 0 0 0;
  font-size: 0.95rem;
  font-weight: 500;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.75rem;
  color: #4A5568;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: all 0.3s ease;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
}

.close-btn:hover {
  background: rgba(75, 150, 243, 0.1);
  color: #3178E6;
}

.test-form {
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #2D3748;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
  font-family: 'Nunito', sans-serif;
}

.form-group input {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  background-color: #F8FAFC;
  color: #2D3748;
  font-family: 'Nunito', sans-serif;
}

.form-group input:focus {
  outline: none;
  border-color: #4B96F3;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
  background-color: #FFFFFF;
}

.form-group input::placeholder {
  color: #A0AEC0;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  align-items: start;
}

.score-preview {
  background: rgba(75, 150, 243, 0.05);
  padding: 1.25rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.preview-label {
  color: #4A5568;
  font-weight: 600;
  font-size: 0.95rem;
}

.preview-score {
  font-size: 1.25rem;
  font-weight: 700;
  font-family: 'Quicksand', sans-serif;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  min-width: 80px;
  text-align: center;
}

.preview-score.excellent { 
  color: #10b981; 
  background-color: rgba(16, 185, 129, 0.1);
}
.preview-score.good { 
  color: #3178E6; 
  background-color: rgba(75, 150, 243, 0.1);
}
.preview-score.average { 
  color: #f59e0b; 
  background-color: rgba(245, 158, 11, 0.1);
}
.preview-score.poor { 
  color: #ef4444; 
  background-color: rgba(239, 68, 68, 0.1);
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.btn-cancel, .btn-submit {
  padding: 0.875rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  font-family: 'Nunito', sans-serif;
}

.btn-cancel {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.btn-submit {
  background: #4B96F3;
  color: white;
  border: none;
  min-width: 140px;
}

.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-cancel:hover {
  background: rgba(239, 68, 68, 0.15);
}

.btn-submit:not(:disabled):hover {
  background: #3178E6;
}

@media (max-width: 768px) {
  .modal-content {
    width: 95%;
  }
}

@media (max-width: 576px) {
  .modal-header {
    padding: 1.25rem 1.5rem;
  }
  
  .test-form {
    padding: 1.5rem;
  }

  .form-row {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .student-avatar {
    width: 40px;
    height: 40px;
    font-size: 1.125rem;
  }
  
  h2 {
    font-size: 1.25rem;
  }
  
  .form-actions {
    flex-direction: column-reverse;
    gap: 0.75rem;
  }
  
  .btn-cancel, .btn-submit {
    width: 100%;
    justify-content: center;
    padding: 0.75rem 1rem;
  }
}
</style>