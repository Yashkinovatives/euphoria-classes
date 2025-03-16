<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h2>View Results - {{ student?.name }}</h2>

      <!-- Select Semester -->
      <div class="form-group">
        <label for="semester">Select Semester</label>
        <select v-model="selectedSemester" @change="fetchResults">
          <option v-for="semester in semesters" :key="semester.id" :value="semester.id">
            {{ semester.semester }} ({{ semester.year }})
          </option>
        </select>
      </div>

      <!-- Display Results -->
      <div v-if="loadingResults" class="loading-section">
        <p>Loading results...</p>
      </div>

      <div v-else-if="studentResults.length > 0" class="results-section">
        <table>
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

        <!-- Display Uploaded Document -->
        <div v-if="resultDocument" class="document-section">
          <p>Uploaded Result:</p>
          <a :href="resultDocument" target="_blank" class="view-document-btn">📄 View Result</a>
        </div>
      </div>

      <div v-else class="no-results">
        <p>No results found for this semester.</p>
      </div>

      <!-- Close Button -->
      <button @click="$emit('close')" class="close-btn">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, onMounted } from "vue";
import axios from "axios";

const props = defineProps({
  student: Object, // The selected student
});

const selectedSemester = ref(null);
const semesters = ref([]);
const studentResults = ref([]);
const resultDocument = ref(null);
const loadingResults = ref(false);

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

// ✅ Trigger data fetch when student is selected
watch(() => props.student, (newStudent) => {
  if (newStudent) {
    fetchSemesters();
  }
});

// ✅ Fetch semesters when modal is opened
onMounted(() => {
  fetchSemesters();
});
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  width: 500px;
  max-width: 90%;
  text-align: center;
}

h2 {
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
  text-align: left;
}

select {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.3rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.loading-section, .no-results {
  margin-top: 1rem;
  font-weight: bold;
  color: #6b7280;
}

.results-section {
  margin-top: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.5rem;
  text-align: center;
}

th {
  background-color: #f3f4f6;
}

.document-section {
  margin-top: 1rem;
}

.view-document-btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

.close-btn {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: #ccc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
