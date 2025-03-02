# components/EnrollmentForm.vue
<template>
  <div class="enrollment-card">
    <div class="badge">
      <span class="badge-icon">✨</span>
      <span>Get Started</span>
    </div>
    
    <h2>Enroll Your Child</h2>
    <p class="subtitle">Begin your child's learning journey with us</p>

    <form @submit.prevent="handleSubmit" class="enrollment-form">
      <div class="form-group">
        <label>Full Name</label>
        <input 
          type="text" 
          v-model="studentData.name" 
          required
          placeholder="Enter student's full name"
          :disabled="isSubmitting"
        />
      </div>

      <div class="form-group">
        <label>Class Section</label>
        <select 
          v-model="studentData.class_section" 
          required
          :disabled="isSubmitting"
        >
          <option value="" disabled>Select a class</option>
          <option 
            v-for="cls in classSections" 
            :key="cls.id" 
            :value="cls.id"
          >
            {{ cls.name }}
          </option>
        </select>
      </div>

      <button 
        type="submit" 
        class="submit-btn"
        :disabled="isSubmitting"
      >
        <span class="btn-icon">{{ isSubmitting ? '⏳' : '🚀' }}</span>
        <span>{{ isSubmitting ? 'Enrolling...' : 'Complete Enrollment' }}</span>
      </button>

      <p v-if="error" class="error-message">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits, defineProps } from 'vue';
import axios from 'axios';

defineProps({
  classSections: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['enroll', 'enrollmentSuccess']);

const studentData = ref({
  name: '',
  class_section: ''
});

const isSubmitting = ref(false);
const error = ref(null);

const handleSubmit = async () => {
  try {
    isSubmitting.value = true;
    error.value = null;

    console.log("Enrollment data being sent:", studentData.value);

    // Remove the response variable or use it if needed
    await axios.post(
      'http://127.0.0.1:8000/api/parent/enroll-student/',
      studentData.value,
      {
        headers: { 
          Authorization: `Bearer ${localStorage.getItem('access_token')}` 
        }
      }
    );

    emit('enroll', studentData.value);
    emit('enrollmentSuccess');

    studentData.value = {
      name: '',
      class_section: ''
    };

  } catch (err) {
    console.error('Enrollment error:', err);
    console.error('Response data:', err.response?.data);
    error.value = err.response?.data?.error || 'Failed to enroll student';
    alert(error.value);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.enrollment-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 2.5rem;
  max-width: 600px;
  margin: 2rem auto;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
}
.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}
.error-message {
  color: #ef4444;
  margin-top: 1rem;
  text-align: center;
  font-size: 0.9rem;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: rgba(139, 92, 246, 0.15);
  border-radius: 100px;
  margin-bottom: 1.5rem;
  gap: 0.5rem;
  font-weight: 600;
  color: #6d28d9;
}

.badge-icon {
  font-size: 1.25rem;
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #64748b;
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 500;
  margin-bottom: 0.5rem;
  color: #1e293b;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 1rem;
  border: 1px solid rgba(139, 92, 246, 0.2);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #7c3aed;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

.submit-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(45deg, #7c3aed, #a855f7);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(124, 58, 237, 0.2);
}

@media (max-width: 768px) {
  .enrollment-card {
    padding: 1.5rem;
    margin: 1rem;
  }

  h2 {
    font-size: 2rem;
  }
}
</style>