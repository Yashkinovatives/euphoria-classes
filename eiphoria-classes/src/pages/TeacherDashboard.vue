<!-- TeacherDashboard.vue -->
<template>
  <div class="dashboard">
    <!-- Animated Background -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <!-- Main Content -->
    <div class="dashboard-container">
      <!-- Header Section -->
      <header class="header">
        <div class="header-content">
          <div class="header-left">
            <h1>Teacher Dashboard</h1>
          </div>
          <div class="header-actions">
            <button @click="openNoticeBoardModal" class="notice-btn">
              <span class="btn-icon">📌</span>
              <span>Notice Board</span>
            </button>
            <button @click="logout" class="logout-btn">
              <span class="btn-icon">🚪</span>
              <span>Logout</span>
            </button>
          </div>
        </div>
      </header>

      <div v-if="loading" class="loader">
        <div class="loader-spinner"></div>
        <p>Loading your dashboard...</p>
      </div>

      <div v-else class="dashboard-content">
        <!-- Welcome Card -->
        <div class="welcome-card">
          <div class="welcome-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
          </div>
          <div class="welcome-text">
            <h2>Welcome <span class="teacher-name">{{ teacherName }}</span> to Your Dashboard</h2>
            <p>Manage your students, classes, and teaching resources all in one place.</p>
          </div>
        </div>

        <!-- Students Management -->
        <StudentsTable
          :students="students"
          @view-details="viewStudentDetails"
          @add-test="openTestModal"
          @view-results="openViewResultsModal"
          @manage-fees="manageStudentFees"
          @manage-attendance="manageStudentAttendance"
        />
      </div>

      <!-- Modals -->
      <AddTestModal
        v-if="showTestModal"
        :student="selectedStudent"
        @close="closeTestModal"
        @submit="submitTestResult"
      />
      
      <FeesModal
        v-if="showFeesModal"
        :student="selectedStudent"
        @close="closeFeesModal"
        @update="refreshData"
      />

      <AttendanceModal
        v-if="showAttendanceModal"
        :student="selectedStudent"
        @close="closeAttendanceModal"
        @update="refreshData"
      />
      <ViewStudentResultsModal
        v-if="showViewResultsModal"
        :student="selectedStudent"
        @close="showViewResultsModal = false"
      />
      <NoticeBoardModal
        v-if="showNoticeBoardModal"
        @close="closeNoticeBoardModal"
        @update="refreshData"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

import StudentsTable from "@/components/TeacherDashboradComponents/StudentsTable.vue";
import AddTestModal from "@/components/TeacherDashboradComponents/AddTestModal.vue";
// import StudentDetailsModal from "@/components/TeacherDashboradComponents/StudentDetailsModal.vue";
import FeesModal from "@/components/TeacherDashboradComponents/FeesModal.vue";
import AttendanceModal from "@/components/TeacherDashboradComponents/AttendanceModal.vue";
import NoticeBoardModal from "@/components/TeacherDashboradComponents/NoticeBoardModal.vue";
import ViewStudentResultsModal from "@/components/TeacherDashboradComponents/ViewStudentResultsModal.vue";

const router = useRouter();
const loading = ref(true);
const students = ref([]);
const teacherName = ref("");
const showTestModal = ref(false);
const showFeesModal = ref(false);
const showAttendanceModal = ref(false);
const showNoticeBoardModal = ref(false);
const selectedStudent = ref(null);
const selectedStudentDetails = ref(null);
const showViewResultsModal = ref(false);

onMounted(async () => {
  await refreshData();
});

const openViewResultsModal = (student) => {
  selectedStudent.value = student;
  showViewResultsModal.value = true;
};

const refreshData = async () => {
  try {
    const token = localStorage.getItem("access_token");
    const response = await axios.get(
      "http://127.0.0.1:8000/api/teacher-dashboard/",
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );

    students.value = response.data.students;
    teacherName.value = response.data.teacher_name || "Teacher";
  } catch (error) {
    console.error("Error fetching data:", error);
    if (error.response?.status === 401) {
      localStorage.clear();
      router.push("/");
    }
  } finally {
    loading.value = false;
  }
};

const viewStudentDetails = async (student) => {
  try {
    const token = localStorage.getItem("access_token");
    const response = await axios.get(
      `http://127.0.0.1:8000/api/student/${student.id}/details/`,
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    selectedStudentDetails.value = response.data;
  } catch (error) {
    console.error("Error fetching student details:", error);
  }
};

const openTestModal = (student) => {
  selectedStudent.value = student;
  showTestModal.value = true;
};

const closeTestModal = () => {
  showTestModal.value = false;
  selectedStudent.value = null;
};

const submitTestResult = async (testData) => {
  try {
    const token = localStorage.getItem("access_token");
    await axios.post(
      "http://127.0.0.1:8000/api/test-results/add/",
      {
        student_id: selectedStudent.value.id,
        ...testData,
      },
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );

    showTestModal.value = false;
    await refreshData();
  } catch (error) {
    console.error("Error adding test result:", error);
    throw error;
  }
};

const manageStudentFees = (student) => {
  selectedStudent.value = student;
  showFeesModal.value = true;
};

const closeFeesModal = () => {
  showFeesModal.value = false;
  selectedStudent.value = null;
};

const manageStudentAttendance = (student) => {
  selectedStudent.value = student;
  showAttendanceModal.value = true;
};

const closeAttendanceModal = () => {
  showAttendanceModal.value = false;
  selectedStudent.value = null;
};

const openNoticeBoardModal = () => {
  showNoticeBoardModal.value = true;
};

const closeNoticeBoardModal = () => {
  showNoticeBoardModal.value = false;
};

const logout = () => {
  localStorage.clear();
  router.push("/");
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap");

.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #F0F7FF, #E6F2FF);
  position: relative;
  overflow: hidden;
  font-family: "Nunito", sans-serif;
  color: #2D3748;
  font-size: 16px;
}

.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.floating-element {
  position: absolute;
  background: linear-gradient(
    45deg,
    rgba(75, 150, 243, 0.1),
    rgba(49, 120, 230, 0.1)
  );
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.floating-element:nth-child(1) {
  width: 300px;
  height: 300px;
  top: 10%;
  left: 10%;
}
.floating-element:nth-child(2) {
  width: 200px;
  height: 200px;
  top: 60%;
  left: 20%;
}
.floating-element:nth-child(3) {
  width: 150px;
  height: 150px;
  top: 30%;
  left: 60%;
}
.floating-element:nth-child(4) {
  width: 250px;
  height: 250px;
  top: 70%;
  left: 70%;
}
.floating-element:nth-child(5) {
  width: 180px;
  height: 180px;
  top: 40%;
  left: 40%;
}
.floating-element:nth-child(6) {
  width: 220px;
  height: 220px;
  top: 20%;
  left: 80%;
}
.floating-element:nth-child(7) {
  width: 160px;
  height: 160px;
  top: 80%;
  left: 30%;
}
.floating-element:nth-child(8) {
  width: 280px;
  height: 280px;
  top: 50%;
  left: 85%;
}

@keyframes float {
  0% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(3deg);
  }
  100% {
    transform: translateY(-40px) rotate(-3deg);
  }
}

.dashboard-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  position: relative;
  z-index: 1;
}

.header {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 20px rgba(75, 150, 243, 0.1);
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

h1 {
  font-family: "Quicksand", sans-serif;
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin: 0;
}

.badge {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: rgba(75, 150, 243, 0.15);
  border-radius: 100px;
  gap: 0.5rem;
  font-weight: 600;
  color: #3178E6;
  border: 1px solid rgba(75, 150, 243, 0.2);
}

.badge-icon {
  font-size: 1.25rem;
}

.notice-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: rgba(75, 150, 243, 0.1);
  color: #3178E6;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 100px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.notice-btn:hover {
  background: rgba(75, 150, 243, 0.2);
  transform: translateY(-2px);
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 100px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.logout-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  transform: translateY(-2px);
}

.loader {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.loader-spinner {
  width: 50px;
  height: 50px;
  border: 3px solid rgba(75, 150, 243, 0.2);
  border-top-color: #3178E6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.dashboard-content {
  display: grid;
  gap: 2rem;
}

/* Welcome Card */
.welcome-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 20px rgba(75, 150, 243, 0.08);
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.welcome-icon {
  width: 60px;
  height: 60px;
  background: rgba(75, 150, 243, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3178E6;
  flex-shrink: 0;
}

.welcome-icon svg {
  width: 32px;
  height: 32px;
}

.welcome-text {
  flex: 1;
}

.welcome-text h2 {
  font-family: "Quicksand", sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: #2D3748;
}

.teacher-name {
  color: #3178E6;
  font-weight: 800;
}

.welcome-text p {
  font-size: 1.125rem;
  color: #4A5568;
  margin: 0;
  line-height: 1.5;
}

/* Responsive styles */
@media (max-width: 1024px) {
  .dashboard-container {
    padding: 1.5rem;
  }
}

@media (max-width: 768px) {
  html, body {
    font-size: 14px;
  }

  .dashboard-container {
    padding: 1rem;
  }

  .header {
    padding: 1.25rem;
  }

  .header-content {
    flex-direction: column;
    gap: 1.25rem;
    text-align: center;
  }

  .header-left {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
  }

  .badge {
    width: 100%;
    justify-content: center;
    padding: 0.65rem 1rem;
  }

  .header-actions {
    flex-direction: row;
    width: 100%;
    gap: 0.75rem;
  }

  .notice-btn,
  .logout-btn {
    width: 50%;
    justify-content: center;
    padding: 0.65rem 1rem;
    font-size: 0.9rem;
  }

  h1 {
    font-size: 1.75rem;
  }
  
  .welcome-card {
    flex-direction: column;
    text-align: center;
    padding: 1.5rem;
  }
  
  .welcome-text h2 {
    font-size: 1.25rem;
  }
  
  .welcome-text p {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  html, body {
    font-size: 12px;
  }

  .dashboard-container {
    padding: 0.75rem;
  }
  
  .header {
    padding: 1rem;
    border-radius: 12px;
  }
  
  .header-actions {
    flex-direction: column;
  }
  
  .notice-btn,
  .logout-btn {
    width: 100%;
    padding: 0.6rem 1rem;
    font-size: 0.875rem;
  }
  
  .badge {
    padding: 0.5rem 0.75rem;
    font-size: 0.875rem;
  }
  
  .badge-icon {
    font-size: 1rem;
  }
  
  h1 {
    font-size: 1.5rem;
  }
  
  .welcome-card {
    padding: 1.25rem;
    border-radius: 12px;
  }
  
  .welcome-icon {
    width: 50px;
    height: 50px;
  }
  
  .welcome-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .welcome-text h2 {
    font-size: 1.125rem;
  }
  
  .welcome-text p {
    font-size: 0.875rem;
  }
  
  .loader-spinner {
    width: 40px;
    height: 40px;
  }
  
  .loader {
    min-height: 300px;
  }
}

/* Target very small mobile devices (Galaxy Fold, etc.) */
@media (max-width: 360px) {
  .dashboard-container {
    padding: 0.5rem;
  }
  
  .header, 
  .welcome-card {
    padding: 0.875rem;
    margin-bottom: 1rem;
  }
  
  h1 {
    font-size: 1.25rem;
  }
  
  .welcome-icon {
    width: 40px;
    height: 40px;
  }
  
  .welcome-icon svg {
    width: 20px;
    height: 20px;
  }
  
  .welcome-text h2 {
    font-size: 1rem;
  }
  
  .welcome-text p {
    font-size: 0.8rem;
  }
  
  .dashboard-content {
    gap: 1rem;
  }
}

/* Fix for mobile Safari overscroll issues */
@supports (-webkit-touch-callout: none) {
  .dashboard {
    min-height: -webkit-fill-available;
  }
}

/* Add safe areas for notched iPhones */
@supports (padding: max(0px)) {
  .dashboard-container {
    padding-left: max(1rem, env(safe-area-inset-left));
    padding-right: max(1rem, env(safe-area-inset-right));
    padding-bottom: max(1rem, env(safe-area-inset-bottom));
  }
}
</style>