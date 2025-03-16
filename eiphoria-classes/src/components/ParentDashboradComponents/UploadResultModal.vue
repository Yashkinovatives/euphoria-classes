<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h2>Upload Student Results</h2>

      <form @submit.prevent="uploadResults">
        <!-- Select Student -->
        <div class="form-group">
          <label for="student">Select Student</label>
          <select v-model="selectedStudent" required>
            <option v-for="student in students" :key="student.id" :value="student.id">
              {{ student.name }}
            </option>
          </select>
        </div>

        <!-- Select Semester -->
        <div class="form-group">
          <label for="semester">Select Semester</label>
          <select v-model="selectedSemester" required>
            <option value="Semester 1">Semester 1</option>
            <option value="Semester 2">Semester 2</option>
            <option value="Annual">Annual</option>
          </select>
        </div>

        <!-- Select Year -->
        <div class="form-group">
          <label for="year">Select Year</label>
          <input type="number" v-model="selectedYear" required min="2000" max="2099" />
        </div>

        <!-- Dynamic Subject Input -->
        <div class="form-group">
          <label>Subjects & Marks</label>
          <div v-for="(subject, index) in subjects" :key="index" class="subject-entry">
            <input type="text" v-model="subject.subject" placeholder="Subject Name" required />
            <input type="number" v-model="subject.marks_obtained" placeholder="Marks Obtained" required min="0" />
            <input type="number" v-model="subject.total_marks" placeholder="Total Marks" required min="1" />
            <button type="button" @click="removeSubject(index)" class="remove-btn">❌</button>
          </div>
          <button type="button" @click="addSubject" class="add-subject-btn">+ Add Subject</button>
        </div>

        <!-- File Upload -->
        <div class="form-group">
          <label for="document">Upload Result File (Optional)</label>
          <input type="file" @change="handleFileUpload" accept=".pdf,.jpg,.png" />
        </div>

        <!-- Submit & Close Buttons -->
        <div class="form-actions">
          <button type="submit" class="submit-btn" :disabled="loading">
            <span v-if="loading">Uploading...</span>
            <span v-else>Upload</span>
          </button>
          <button type="button" class="close-btn" @click="$emit('close')">Cancel</button>
        </div>

        <!-- Success/Error Message -->
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from "vue";
import axios from "axios";

// Props to receive students from parent component
defineProps({
students: Array,
});

// Define emit for closing modal
const emit = defineEmits(["close"]);

const selectedStudent = ref(null);
const selectedSemester = ref("Semester 1");
const selectedYear = ref(new Date().getFullYear());
const subjects = ref([{ subject: "", marks_obtained: "", total_marks: "" }]);
const resultFile = ref(null);
const loading = ref(false);
const successMessage = ref("");
const errorMessage = ref("");

// Add new subject entry
const addSubject = () => {
subjects.value.push({ subject: "", marks_obtained: "", total_marks: "" });
};

// Remove a subject entry
const removeSubject = (index) => {
subjects.value.splice(index, 1);
};

// Handle file selection
const handleFileUpload = (event) => {
resultFile.value = event.target.files[0];
};

// Upload results function
const uploadResults = async () => {
if (!selectedStudent.value || subjects.value.length === 0) {
  errorMessage.value = "Please complete all fields before submitting.";
  return;
}

loading.value = true;
errorMessage.value = "";
successMessage.value = "";

const formData = new FormData();
formData.append("student_id", selectedStudent.value);
formData.append("semester", selectedSemester.value);
formData.append("year", selectedYear.value);

// Convert subjects list to JSON string
const subjectsData = subjects.value.map(subject => ({
  subject: subject.subject,
  marks_obtained: parseInt(subject.marks_obtained),
  total_marks: parseInt(subject.total_marks),
}));

formData.append("subjects", JSON.stringify(subjectsData));

if (resultFile.value) {
  formData.append("document", resultFile.value);
}

try {
  await axios.post(
    "http://127.0.0.1:8000/api/parent/upload-result/",
    formData,
    {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        "Content-Type": "multipart/form-data",
      },
    }
  );

  successMessage.value = "Result uploaded successfully!";
  setTimeout(() => {
    successMessage.value = "";
    emit("close"); // Close the modal after success
  }, 2000);
} catch (error) {
  console.error("Error uploading results:", error);
  errorMessage.value = "Failed to upload results. Please try again.";
} finally {
  loading.value = false;
}
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

input, select {
width: 100%;
padding: 0.5rem;
margin-top: 0.3rem;
border: 1px solid #ccc;
border-radius: 5px;
}

.subject-entry {
display: flex;
align-items: center;
gap: 0.5rem;
}

.remove-btn {
background: #ff4d4d;
color: white;
border: none;
padding: 0.5rem;
border-radius: 5px;
cursor: pointer;
}

.add-subject-btn {
background: #4caf50;
color: white;
border: none;
padding: 0.5rem;
border-radius: 5px;
cursor: pointer;
}

.form-actions {
display: flex;
justify-content: space-between;
margin-top: 1rem;
}

.submit-btn {
background: #007bff;
color: white;
padding: 0.5rem 1rem;
border: none;
border-radius: 5px;
cursor: pointer;
}

.close-btn {
background: #ccc;
padding: 0.5rem 1rem;
border: none;
border-radius: 5px;
cursor: pointer;
}

.success-message {
color: green;
font-weight: bold;
margin-top: 1rem;
}

.error-message {
color: red;
font-weight: bold;
margin-top: 1rem;
}
</style>
