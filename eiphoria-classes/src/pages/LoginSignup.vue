<template>
  <div class="auth-wrapper">
    <div class="auth-container">
      <!-- Left Panel -->
      <div class="image-panel">
        <div class="logo">
          <img src="/logo.svg" alt="Logo" />
        </div>

        <div class="image-content">
          <h2 class="image-title">Capturing Moments,<br />Creating Memories</h2>

          <div class="slide-indicators">
            <span></span>
            <span></span>
            <span class="active"></span>
          </div>
        </div>
      </div>

      <!-- Right Panel -->
      <div class="form-panel">
        <div class="back-link">
          <a href="#" @click.prevent="goBack">
            <span>Back to website</span>
            <i class="fas fa-arrow-right"></i>
          </a>
        </div>

        <div class="auth-form-container">
          <h1 class="form-title">
            {{ isLogin ? "Sign in to your account" : awaitingApproval ? "Verify Approval Code" : "Create an account" }}
          </h1>

          <p class="account-switch">
            {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
            <a href="#" @click.prevent="toggleAuthMode">
              {{ isLogin ? "Sign up" : "Log in" }}
            </a>
          </p>

          <form @submit.prevent="handleSubmit" class="auth-form">
            <!-- Full Name Field -->
            <div class="form-group" v-if="!isLogin && !awaitingApproval">
              <label>Full Name</label>
              <input type="text" v-model="form.name" placeholder="Enter your full name" required />
            </div>

            <!-- Email Address -->
            <div class="form-group">
              <label>Email Address</label>
              <input type="email" v-model="form.email" placeholder="Enter your email" required />
            </div>

            <!-- Password Field -->
            <div class="form-group" v-if="!awaitingApproval">
              <label>Password</label>
              <div class="password-input">
                <input
                  :type="showPassword ? 'text' : 'password'"
                  v-model="form.password"
                  placeholder="Enter your password"
                  required
                />
                <button type="button" class="toggle-password" @click="togglePasswordVisibility">
                  <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                </button>
              </div>
            </div>

            <!-- Role Selection -->
            <div class="form-group" v-if="!isLogin && !awaitingApproval">
              <label>Select Role</label>
              <div class="role-buttons">
                <button
                  type="button"
                  v-for="role in roles"
                  :key="role.value"
                  :class="{ selected: form.user_type === role.value }"
                  class="role-btn"
                  @click="form.user_type = role.value"
                >
                  {{ role.label }}
                </button>
              </div>
            </div>

            <!-- Approval Code Input (Only for Teachers after Signup) -->
            <div class="form-group" v-if="awaitingApproval">
              <label>Enter Approval Code</label>
              <input type="text" v-model="approvalCode" placeholder="Enter the code sent to admin" required />
            </div>

            <!-- Submit Button -->
            <button type="submit" class="submit-btn" :disabled="loading">
              <span v-if="!loading">
                {{ isLogin ? "Sign In" : awaitingApproval ? "Verify Code" : "Create Account" }}
              </span>
              <span v-else class="loader"></span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const loading = ref(false);
const showPassword = ref(false);
const isLogin = ref(true);
const awaitingApproval = ref(false);
const approvalCode = ref("");

const form = reactive({
  name: "",
  email: "",
  password: "",
  user_type: "teacher",
});

const roles = [
  { label: "Teacher", value: "teacher" },
  { label: "Parent", value: "parent" },
];

const toggleAuthMode = () => {
  isLogin.value = !isLogin.value;
  form.name = "";
  awaitingApproval.value = false;
  approvalCode.value = "";
};

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

const handleSubmit = async () => {
  loading.value = true;
  try {
    let endpoint;
    let payload = { ...form };

    // Convert email to lowercase for consistency
    payload.email = payload.email.toLowerCase(); 

    if (isLogin.value) {
      endpoint = "http://127.0.0.1:8000/api/login/";
    } else {
      if (awaitingApproval.value) {
        // Teacher Verification
        endpoint = "http://127.0.0.1:8000/api/verify-teacher/";
        payload = { email: payload.email, approval_code: approvalCode.value };
      } else {
        // Initial Signup
        endpoint = "http://127.0.0.1:8000/api/signup/";
      }
    }

    const response = await axios.post(endpoint, payload);

    if (isLogin.value) {
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
      localStorage.setItem("user_type", response.data.user_type);
      router.push(response.data.user_type === "teacher" ? "/teacher-dashboard" : "/parent-dashboard");
    } else {
      if (form.user_type === "teacher" && !awaitingApproval.value) {
        awaitingApproval.value = true;
      } else {
        isLogin.value = true;
      }
    }
  } catch (error) {
    alert(error.response?.data?.error || "Something went wrong.");
  } finally {
    loading.value = false;
  }
};
</script>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Inter', sans-serif;
}

.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  background-color: rgba(67, 56, 83, 0.1);
}

.auth-container {
  display: flex;
  width: 100%;
  max-width: 1000px;
  background-color: #1a1625;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

/* Left Panel - Image Section */
.image-panel {
  flex: 5;
  background: linear-gradient(to bottom, #5e38a8, #7048bc);
  display: flex;
  flex-direction: column;
  padding: 2rem;
  position: relative;
  overflow: hidden;
  color: white;
}

.logo {
  margin-bottom: 3rem;
}

.logo img {
  height: 32px;
}

.image-content {
  display: flex;
  flex-direction: column;
  margin-top: auto;
  margin-bottom: 2rem;
}

.image-title {
  font-size: 1.8rem;
  font-weight: 600;
  line-height: 1.3;
  margin-bottom: 2rem;
}

.slide-indicators {
  display: flex;
  gap: 0.5rem;
}

.slide-indicators span {
  width: 2rem;
  height: 4px;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
}

.slide-indicators span.active {
  background-color: white;
}

/* Right Panel - Form Section */
.form-panel {
  flex: 6;
  background-color: #1a1625;
  padding: 2rem;
  position: relative;
  color: white;
}

.back-link {
  position: absolute;
  top: 2rem;
  right: 2rem;
}

.back-link a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 0.2s;
}

.back-link a:hover {
  color: white;
}

.back-link i {
  font-size: 0.75rem;
}

.auth-form-container {
  max-width: 380px;
  margin: 2rem auto;
}

.form-title {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.account-switch {
  font-size: 0.875rem;
  margin-bottom: 2rem;
  color: rgba(255, 255, 255, 0.7);
}

.account-switch a {
  color: #7048bc;
  text-decoration: none;
  font-weight: 500;
}

.account-switch a:hover {
  text-decoration: underline;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.name-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  position: relative;
}

.input-label {
  font-size: 0.9rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 0.5rem;
  display: block;
}

.form-group input {
  width: 100%;
  padding: 0.875rem 1rem;
  background-color: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 8px;
  color: white;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.form-group input:focus {
  outline: none;
  border-color: #7048bc;
  background-color: rgba(255, 255, 255, 0.12);
}

.form-group input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.password-input {
  position: relative;
}

.toggle-password {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  font-size: 0.9rem;
}

.role-buttons {
  display: flex;
  gap: 1rem;
}

.role-btn {
  flex: 1;
  padding: 0.75rem;
  background-color: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.role-btn i {
  font-size: 1rem;
}

.role-btn.selected {
  background-color: rgba(112, 72, 188, 0.2);
  border-color: #7048bc;
  color: white;
}

.terms-checkbox {
  margin: 0.5rem 0;
  user-select: none;
}

.checkbox-container {
  display: flex;
  align-items: center;
  position: relative;
  padding-left: 1.75rem;
  cursor: pointer;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

.checkbox-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 18px;
  width: 18px;
  background-color: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 4px;
}

.checkbox-container:hover input ~ .checkmark {
  background-color: rgba(255, 255, 255, 0.12);
}

.checkbox-container input:checked ~ .checkmark {
  background-color: #7048bc;
  border-color: #7048bc;
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.checkbox-container input:checked ~ .checkmark:after {
  display: block;
}

.checkbox-container .checkmark:after {
  left: 6px;
  top: 2px;
  width: 4px;
  height: 9px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.terms-link {
  color: #7048bc;
  text-decoration: none;
}

.terms-link:hover {
  text-decoration: underline;
}

.submit-btn {
  width: 100%;
  padding: 0.875rem;
  margin-top: 0.5rem;
  background-color: #7048bc;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover {
  background-color: #5e38a8;
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.loader {
  display: inline-block;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 900px) {
  .auth-container {
    flex-direction: column;
    max-width: 500px;
  }
  
  .image-panel {
    display: none;
  }
  
  .form-panel {
    padding: 2rem 1.5rem;
  }
  
  .auth-form-container {
    margin: 1rem auto;
  }
}

@media (max-width: 500px) {
  .auth-wrapper {
    padding: 1rem;
  }
  
  .form-panel {
    padding: 1.5rem 1rem;
  }
  
  .name-fields {
    grid-template-columns: 1fr;
  }
  
  .back-link {
    position: static;
    margin-bottom: 1rem;
    text-align: right;
  }
}
</style>