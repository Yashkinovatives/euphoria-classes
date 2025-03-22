<template>
  <div class="dashboard">
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <div class="dashboard-container">
      <header class="header">
        <div class="header-content">
          <div class="header-left">
            <h1>Parent Dashboard</h1>
            <div class="badge">
              <span class="badge-icon">👋</span>
              <span>Welcome Back!</span>
            </div>
          </div>
          <div class="header-actions">
            <button
              @click="openViewResultsModal"
              class="action-btn results-btn"
            >
              <span class="btn-icon">📑</span>
              <span>View Uploaded Results</span>
            </button>
            <button @click="openNoticeBoardModal" class="action-btn notice-btn">
              <span class="btn-icon">📌</span>
              <span>School Notices</span>
            </button>
            <button
              @click="openUploadResultModal"
              class="action-btn upload-btn"
            >
              <span class="btn-icon">📄</span>
              <span>Upload Results</span>
            </button>
            <button @click="logout" class="action-btn logout-btn">
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

      <div v-else>
        <div v-if="successMessage" class="success-message">
          {{ successMessage }}
        </div>

        <div v-if="enrollmentRequired" class="enrollment-section">
          <EnrollmentForm
            :classSections="classSections"
            @enroll="handleEnrollment"
            @enrollmentSuccess="refreshDashboard"
          />
        </div>

        <div v-else class="dashboard-content">
          <QuickStats
            :students="students"
            :testResults="testResults"
            :attendanceRecords="attendanceRecords"
          />

          <StudentOverview :students="students" />

          <StudentAttendance
            :attendanceRecords="attendanceRecords"
            :isLoading="isLoadingAttendance"
          />

          <!-- <AcademicPerformance :testResults="testResults" /> -->

          <FeeStatus :feeStatus="feeStatus" />
        </div>
      </div>

      <!-- Notice Board Modal -->
      <ParentNoticeBoardModal
        v-if="showNoticeBoardModal"
        @close="closeNoticeBoardModal"
      />

      <!-- Upload Result Modal -->
      <UploadResultModal
        v-if="showUploadResultModal"
        @close="closeUploadResultModal"
        :students="students"
        @uploadSuccess="refreshDashboard"
      />

      <!-- View Uploaded Results Modal -->
      <ViewUploadedResultsModal
        v-if="showViewResultsModal"
        @close="closeViewResultsModal"
      />
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

import EnrollmentForm from "@/components/ParentDashboradComponents/EnrollmentForm.vue";
import QuickStats from "@/components/ParentDashboradComponents/QuickStats.vue";
import StudentOverview from "@/components/ParentDashboradComponents/StudentOverview.vue";
// import AcademicPerformance from "@/components/ParentDashboradComponents/AcademicPerformance.vue";
import FeeStatus from "@/components/ParentDashboradComponents/FeeStatus.vue";
import StudentAttendance from "@/components/ParentDashboradComponents/StudentAttendance.vue";
import ParentNoticeBoardModal from "@/components/ParentDashboradComponents/ParentNoticeBoardModal.vue";
import UploadResultModal from "@/components/ParentDashboradComponents/UploadResultModal.vue";
import ViewUploadedResultsModal from "@/components/ParentDashboradComponents/ViewUploadedResultsModal.vue";

const router = useRouter();
const students = ref([]);
const enrollmentRequired = ref(false);
const loading = ref(true);
const classSections = ref([]);
const testResults = ref([]);
const feeStatus = ref([]);
const successMessage = ref("");
const attendanceRecords = ref([]);
const isLoadingAttendance = ref(true);
const error = ref(null);
const showNoticeBoardModal = ref(false);
const showUploadResultModal = ref(false);
const showViewResultsModal = ref(false); // 🆕 State for View Results Modal

// Open/Close View Results Modal
const openViewResultsModal = () => {
  showViewResultsModal.value = true;
};
const closeViewResultsModal = () => {
  showViewResultsModal.value = false;
};
// Open/Close Notice Modal
const openNoticeBoardModal = () => {
  showNoticeBoardModal.value = true;
};

const closeNoticeBoardModal = () => {
  showNoticeBoardModal.value = false;
};

// Open/Close Upload Result Modal
const openUploadResultModal = () => {
  showUploadResultModal.value = true;
};

const closeUploadResultModal = () => {
  showUploadResultModal.value = false;
};

// Fetch Attendance Records
const fetchAttendance = async () => {
  isLoadingAttendance.value = true;
  error.value = null;

  try {
    const token = localStorage.getItem("access_token");
    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };

    const response = await axios.get(
      "http://127.0.0.1:8000/api/parent/student-attendance/",
      config
    );
    attendanceRecords.value = response.data.attendance_records || [];
  } catch (err) {
    error.value = err;
    attendanceRecords.value = [];
  } finally {
    isLoadingAttendance.value = false;
  }
};

// Fetch Student Test Results
const fetchStudentResults = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/parent/test-results/",
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
      }
    );
    testResults.value = response.data.results || [];
  } catch (error) {
    testResults.value = [];
  }
};

// Fetch Fee Status
const fetchFeeStatus = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/parent/monthly-fee-status/",
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
      }
    );
    feeStatus.value = response.data.fee_status || [];
  } catch (error) {
    feeStatus.value = [];
  }
};

// Fetch Class Sections
const fetchClassSections = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/class-sections/"
    );
    classSections.value = response.data;
  } catch (error) {
    console.error("Error fetching class sections:", error);
  }
};

// Fetch Parent Dashboard Data
const fetchParentDashboard = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/parent-dashboard/",
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
      }
    );

    if (response.data.enrollment_required) {
      enrollmentRequired.value = true;
    } else {
      enrollmentRequired.value = false;
      students.value = [
        ...new Set(response.data.students.map((s) => JSON.stringify(s))),
      ].map((s) => JSON.parse(s));
    }
  } catch (error) {
    if (error.response?.status === 401) {
      localStorage.clear();
      router.push("/");
    }
  }
};

// Refresh Dashboard Data
const refreshDashboard = async () => {
  try {
    loading.value = true;
    students.value = [];

    await Promise.all([
      fetchParentDashboard(),
      fetchStudentResults(),
      fetchFeeStatus(),
      fetchAttendance(),
    ]);
  } catch (error) {
    console.error("Error refreshing dashboard:", error);
  } finally {
    loading.value = false;
  }
};

// Logout User
const logout = () => {
  localStorage.clear();
  router.push("/");
};

// Load Data on Page Mount
onMounted(async () => {
  try {
    await Promise.all([
      fetchParentDashboard(),
      fetchClassSections(),
      fetchStudentResults(),
      fetchFeeStatus(),
      fetchAttendance(),
    ]);
  } catch (err) {
    console.error("Error loading dashboard:", err);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap");

.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f3ff, #ede9fe);
  position: relative;
  overflow: hidden;
  font-family: "Outfit", sans-serif;
}
.results-btn {
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
  border: 1px solid rgba(34, 197, 94, 0.2);
}

.results-btn:hover {
  background: rgba(34, 197, 94, 0.2);
  transform: translateY(-2px);
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
    rgba(139, 92, 246, 0.1),
    rgba(192, 132, 252, 0.1)
  );
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.floating-element:nth-child(1) {
  width: 300px;
  height: 300px;
  top: 5%;
  left: 10%;
  animation-delay: 0s;
}
.floating-element:nth-child(2) {
  width: 200px;
  height: 200px;
  top: 65%;
  left: 85%;
  animation-delay: -4s;
}
.floating-element:nth-child(3) {
  width: 350px;
  height: 350px;
  top: 35%;
  left: 55%;
  animation-delay: -8s;
}
.floating-element:nth-child(4) {
  width: 150px;
  height: 150px;
  top: 75%;
  left: 15%;
  animation-delay: -12s;
}
.floating-element:nth-child(5) {
  width: 250px;
  height: 250px;
  top: 20%;
  left: 75%;
  animation-delay: -16s;
}
.floating-element:nth-child(6) {
  width: 180px;
  height: 180px;
  top: 80%;
  left: 45%;
  animation-delay: -5s;
}
.floating-element:nth-child(7) {
  width: 220px;
  height: 220px;
  top: 15%;
  left: 35%;
  animation-delay: -9s;
}
.floating-element:nth-child(8) {
  width: 270px;
  height: 270px;
  top: 60%;
  left: 70%;
  animation-delay: -13s;
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
  box-shadow: 0 4px 20px rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.1);
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
  flex-wrap: wrap;
}

h1 {
  font-family: "Space Grotesk", sans-serif;
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
}

.badge {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: rgba(139, 92, 246, 0.15);
  border-radius: 8px;
  gap: 0.5rem;
  font-weight: 600;
  color: #6d28d9;
}

.badge-icon,
.btn-icon {
  font-size: 1.25rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-family: "Outfit", sans-serif;
}

.notice-btn {
  background: rgba(139, 92, 246, 0.1);
  color: #7c3aed;
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.notice-btn:hover {
  background: rgba(139, 92, 246, 0.2);
  transform: translateY(-2px);
}

.upload-btn {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.upload-btn:hover {
  background: rgba(59, 130, 246, 0.2);
  transform: translateY(-2px);
}

.logout-btn {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
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
  border: 3px solid #e9d5ff;
  border-top-color: #7c3aed;
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

.enrollment-section {
  animation: fadeIn 0.5s ease;
}

.success-message {
  background-color: rgba(34, 197, 94, 0.15);
  color: rgb(22, 163, 74);
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 600;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 940px) {
  .header-actions {
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .action-btn {
    min-width: 180px;
  }
}

@media (max-width: 768px) {
  .dashboard-container {
    padding: 1rem;
  }

  .header {
    padding: 1rem;
  }

  .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .header-left {
    flex-direction: column;
    gap: 1rem;
  }

  .header-actions {
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }

  .action-btn {
    width: 100%;
    justify-content: center;
    min-width: auto;
  }

  h1 {
    font-size: 1.5rem;
  }

  .badge {
    align-self: center;
  }
}

@media (max-width: 480px) {
  .dashboard-container {
    padding: 0.75rem;
  }

  .header {
    padding: 1rem;
    border-radius: 12px;
  }

  h1 {
    font-size: 1.3rem;
  }

  .badge {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }

  .action-btn {
    padding: 0.625rem 1rem;
    font-size: 0.9rem;
  }
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .dashboard-container {
    padding-left: max(2rem, env(safe-area-inset-left));
    padding-right: max(2rem, env(safe-area-inset-right));
  }
}
</style>
