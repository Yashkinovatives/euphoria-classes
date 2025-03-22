<template>
  <teleport to="body">
    <div class="modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h2>View Results - {{ student?.name }}</h2>
          <button @click="$emit('close')" class="close-modal-btn">&times;</button>
        </div>

        <div class="modal-body">
          <!-- Select Semester -->
          <div class="form-group">
            <label for="semester">Select Semester</label>
            <select 
              id="semester"
              v-model="selectedSemester" 
              @change="fetchResults"
              class="semester-select"
            >
              <option value="" disabled selected>Choose a semester</option>
              <option 
                v-for="semester in semesters" 
                :key="semester.id" 
                :value="semester.id"
              >
                {{ semester.semester }} ({{ semester.year }})
              </option>
            </select>
          </div>

          <!-- Display Results -->
          <div v-if="loadingResults" class="loading-section">
            <div class="loader-spinner"></div>
            <p>Loading results...</p>
          </div>

          <div v-else-if="studentResults.length > 0" class="results-section">
            <div class="table-container">
              <table class="results-table">
                <thead>
                  <tr>
                    <th>Subject</th>
                    <th>Marks Obtained</th>
                    <th>Total Marks</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="result in studentResults" :key="result.subject">
                    <td>{{ result.subject }}</td>
                    <td>{{ result.marks_obtained }}</td>
                    <td>{{ result.total_marks }}</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Display Uploaded Document -->
            <div v-if="resultDocument" class="document-section">
              <p>Uploaded Result:</p>
              <a :href="resultDocument" target="_blank" class="view-document-btn">
                <span class="doc-icon">📄</span> View Result
              </a>
            </div>

            <!-- Delete Button for Teachers -->
            <div v-if="selectedSemester" class="delete-section">
              <button @click="deleteResult" class="delete-btn" :disabled="isDeleting">
                <span class="delete-icon">🗑️</span>
                <span v-if="isDeleting">Deleting...</span>
                <span v-else>Delete Result</span>
              </button>
            </div>

          </div>

          <div v-else class="no-results">
            <p>No results found for this semester.</p>
          </div>
        </div>

        <!-- Close Button -->
        <div class="modal-footer">
          <button @click="$emit('close')" class="close-btn">Close</button>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script setup>
import { ref, watch, defineProps, onMounted, onBeforeUnmount } from "vue";
import axios from "axios";

const props = defineProps({
  student: Object, // The selected student
});

const selectedSemester = ref("");
const semesters = ref([]);
const studentResults = ref([]);
const resultDocument = ref(null);
const loadingResults = ref(false);
const isDeleting = ref(false);

// Lock body scrolling when modal is open
onMounted(() => {
  document.documentElement.style.overflow = 'hidden';
  document.body.style.overflow = 'hidden';
  document.body.style.position = 'fixed';
  document.body.style.width = '100%';
  document.body.style.top = `-${window.scrollY}px`;
  fetchSemesters();
});

// Restore scrolling when modal is closed
onBeforeUnmount(() => {
  const scrollY = document.body.style.top;
  document.documentElement.style.overflow = '';
  document.body.style.overflow = '';
  document.body.style.position = '';
  document.body.style.width = '';
  document.body.style.top = '';
  window.scrollTo(0, parseInt(scrollY || '0') * -1);
});

// ✅ Fetch available semesters for the selected student
const fetchSemesters = async () => {
  if (!props.student || !props.student.id) return;

  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/teacher/view-results/`, {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });

    // ✅ Ensure filtering is based on `student_id` instead of `student__name`
    semesters.value = response.data.results.filter(res => res.student_id === props.student.id);
  } catch (error) {
    console.error("Error fetching semesters:", error);
  }
};

// ✅ Fetch results for the selected semester
const fetchResults = async () => {
  if (!selectedSemester.value) return;
  loadingResults.value = true;

  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/teacher/view-result/${selectedSemester.value}/`, {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });

    studentResults.value = response.data.subjects || [];
    resultDocument.value = response.data.document || null;
  } catch (error) {
    console.error("Error fetching student results:", error);
  } finally {
    loadingResults.value = false;
  }
};

// ✅ Delete result API call
const deleteResult = async () => {
  if (!selectedSemester.value) return;

  if (!confirm("Are you sure you want to delete this result? This action cannot be undone.")) return;

  try {
    isDeleting.value = true;
    const token = localStorage.getItem("access_token");

    await axios.delete(`http://127.0.0.1:8000/api/teacher/delete-result/${selectedSemester.value}/`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    alert("Result deleted successfully.");
    fetchSemesters(); // Refresh available results
    studentResults.value = [];
    resultDocument.value = null;
    selectedSemester.value = "";
  } catch (error) {
    console.error("Error deleting result:", error);
    alert("Failed to delete result.");
  } finally {
    isDeleting.value = false;
  }
};

// ✅ Trigger data fetch when student is selected
watch(() => props.student, (newStudent) => {
  if (newStudent) {
    fetchSemesters();
  }
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap");

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999999;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  overflow: hidden !important;
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 600px;
  max-width: 90%;
  height: auto;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(75, 150, 243, 0.2);
  border: 1px solid rgba(75, 150, 243, 0.1);
  font-family: "Nunito", sans-serif;
  z-index: 1000000;
  animation: modalFade 0.25s ease;
}

@keyframes modalFade {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  padding: 1.5rem;
  background: white;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 10;
  flex-shrink: 0;
}

.modal-header h2 {
  margin: 0;
  color: #2D3748;
  font-family: 'Quicksand', sans-serif;
  font-weight: 700;
  font-size: 1.25rem;
}

.close-modal-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #64748b;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  flex-shrink: 0;
}

.close-modal-btn:hover {
  background-color: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  overflow-x: hidden;
  flex-grow: 1;
  -webkit-overflow-scrolling: touch;
  background-color: white;
}

.modal-footer {
  padding: 1rem 1.5rem;
  border-top: 1px solid rgba(75, 150, 243, 0.1);
  text-align: right;
  background: white;
  flex-shrink: 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #2D3748;
}

.semester-select {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  background-color: white;
  font-size: 16px; /* Prevents iOS zoom on focus */
  font-family: "Nunito", sans-serif;
  color: #2D3748;
  -webkit-appearance: none; /* Better appearance on iOS */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%234B96F3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 2.5rem;
  transition: all 0.2s ease;
  box-sizing: border-box;
  height: 3.25rem;
}

.semester-select:focus {
  outline: none;
  border-color: #4B96F3;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
}

.loading-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 0;
  color: #64748b;
}

.loader-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(75, 150, 243, 0.1);
  border-top-color: #3178E6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.results-section {
  margin-top: 0.5rem;
}

.table-container {
  overflow-x: auto;
  border-radius: 8px;
  border: 1px solid rgba(75, 150, 243, 0.1);
  margin-bottom: 1.5rem;
}

.results-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.results-table th, 
.results-table td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
}

.results-table th {
  background-color: rgba(75, 150, 243, 0.05);
  font-weight: 600;
  color: #2D3748;
  white-space: nowrap;
}

.results-table tr:last-child td {
  border-bottom: none;
}

.document-section {
  background-color: rgba(75, 150, 243, 0.05);
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  border: 1px solid rgba(75, 150, 243, 0.1);
  margin-bottom: 1.5rem;
}

.document-section p {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #2D3748;
  font-weight: 600;
}

.view-document-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
}

.view-document-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(75, 150, 243, 0.2);
}

.doc-icon {
  font-size: 1.1rem;
}

.no-results {
  padding: 2rem;
  text-align: center;
  background-color: rgba(75, 150, 243, 0.05);
  border-radius: 8px;
  color: #64748b;
  font-weight: 500;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.close-btn {
  padding: 0.75rem 1.5rem;
  background: rgba(75, 150, 243, 0.1);
  color: #3178E6;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
}

.close-btn:hover {
  background: rgba(75, 150, 243, 0.2);
  transform: translateY(-2px);
}

.delete-section {
  text-align: center;
  margin-bottom: 1rem;
}

.delete-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #f87171, #ef4444);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  box-shadow: 0 2px 4px rgba(239, 68, 68, 0.2);
}

.delete-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(239, 68, 68, 0.3);
}

.delete-btn:disabled {
  background: linear-gradient(135deg, #f1a7a7, #f87171);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.7;
}

.delete-icon {
  font-size: 1.1rem;
}

/* Responsive styles */
@media (max-width: 768px) {
  .modal-content {
    width: 90%;
    max-height: 80vh;
  }
  
  .modal-header {
    padding: 1.25rem;
  }
  
  .modal-body {
    padding: 1.25rem;
  }
  
  .modal-footer {
    padding: 1rem 1.25rem;
  }
  
  .results-table th, 
  .results-table td {
    padding: 0.6rem 0.8rem;
  }
}

@media (max-width: 480px) {
  .modal-overlay {
    align-items: center;
    padding: 0 10px;
  }
  
  .modal-content {
    width: 100%;
    border-radius: 20px;
    max-height: 85vh;
    margin-bottom: 20px;
  }
  
  .modal-header {
    padding: 1rem;
    border-radius: 20px 20px 0 0;
  }
  
  .modal-header h2 {
    font-size: 1.1rem;
    max-width: 80%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .modal-body {
    padding: 1rem;
  }
  
  .form-group {
    margin-bottom: 1.25rem;
  }
  
  .semester-select {
    padding: 0.7rem 0.9rem;
  }
  
  .results-table {
    font-size: 0.85rem;
  }
  
  .results-table th, 
  .results-table td {
    padding: 0.6rem;
  }
  
  .document-section {
    padding: 0.875rem;
  }
  
  .view-document-btn {
    width: 100%;
    padding: 0.7rem 1rem;
  }
  
  .delete-btn {
    width: 100%;
    padding: 0.7rem 1rem;
  }
  
  .modal-footer {
    padding: 0.875rem 1rem;
  }
  
  .close-btn {
    width: 100%;
    padding: 0.7rem 1rem;
  }
}

@media (max-width: 360px) {
  .modal-header h2 {
    font-size: 1rem;
  }
  
  .results-table {
    font-size: 0.8rem;
  }
  
  .results-table th, 
  .results-table td {
    padding: 0.5rem;
  }
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .modal-overlay {
    padding-bottom: max(15px, env(safe-area-inset-bottom));
  }
}

/* Better handling for landscape mode */
@media (max-height: 500px) and (orientation: landscape) {
  .modal-content {
    max-height: 95vh;
  }
  
  .modal-body {
    padding: 0.875rem;
  }
  
  .form-group {
    margin-bottom: 0.75rem;
  }
}
</style>