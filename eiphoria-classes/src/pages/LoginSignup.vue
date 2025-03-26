<template>
  <div class="auth-wrapper">
    <div class="auth-container">
      <!-- Left Panel -->
      <div class="image-panel">
        <div class="logo">
          <span class="logo-dot"></span> Euphoria Tutorials
        </div>

        <div class="image-content">
          <h2 class="image-title">Connecting <br />Parents and Learning</h2>

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

            <!-- Role Selection - Now shown for both login and signup -->
            <div class="form-group" v-if="!awaitingApproval">
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
                  <i :class="role.icon"></i>
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
// import CLogo from "@/assets/images/CLogo.jpg";

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
  { label: "Teacher", value: "teacher", icon: "fas fa-chalkboard-teacher" },
  { label: "Parent", value: "parent", icon: "fas fa-user-friends" },
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

const goBack = () => {
  router.push('/');
};

const handleSubmit = async () => {
  loading.value = true;
  try {
    let endpoint;
    let payload = { ...form };

    payload.email = payload.email.toLowerCase(); 

    if (isLogin.value) {
      endpoint = "http://127.0.0.1:8000/api/login/";
    } else {
      if (awaitingApproval.value) {
        endpoint = "http://127.0.0.1:8000/api/verify-teacher/";
        payload = { email: payload.email, approval_code: approvalCode.value };
      } else {
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
}

.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10rem 1.5rem;
  background-color: #fafaea;
  position: relative;
  overflow: hidden;
}

/* Background circles */
.auth-wrapper::before {
  content: '';
  position: absolute;
  top: -250px;
  right: -250px;
  width: 500px;
  height: 500px;
  background-color: rgba(255, 235, 59, 0.1);
  border-radius: 50%;
  z-index: 1;
}

.auth-wrapper::after {
  content: '';
  position: absolute;
  bottom: -300px;
  left: -300px;
  width: 600px;
  height: 600px;
  border: 2px solid rgba(255, 235, 59, 0.2);
  border-radius: 50%;
  z-index: 1;
  opacity: 0.5;
}

.auth-container {
  display: flex;
  width: 100%;
  max-width: 1000px;
  background-color: #fff;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
  position: relative;
  z-index: 10;
  border: 2px solid #ffeb3b;
}

/* Left Panel - Image Section */
.image-panel {
  flex: 5;
  background: linear-gradient(to bottom, rgba(255, 235, 59, 0.2), rgba(255, 235, 59, 0.1));
  display: flex;
  flex-direction: column;
  padding: 2rem;
  position: relative;
  overflow: hidden;
  color: #333;
}

.logo {
  margin-bottom: 3rem;
  font-size: 1.1em;
  font-weight: 600;
  display: inline-block;
  background-color: #fff;
  padding: 8px 15px;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.logo-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: #ffeb3b;
  border-radius: 50%;
  margin-right: 8px;
}

.image-content {
  display: flex;
  flex-direction: column;
  margin-top: auto;
  margin-bottom: 2rem;
}

.image-title {
  font-size: 1.8rem;
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 2rem;
  color: #333;
}

.slide-indicators {
  display: flex;
  gap: 0.5rem;
}

.slide-indicators span {
  width: 2rem;
  height: 4px;
  background-color: rgba(51, 51, 51, 0.3);
  border-radius: 2px;
}

.slide-indicators span.active {
  background-color: #ffeb3b;
}

/* Right Panel - Form Section */
.form-panel {
  flex: 6;
  background-color: #fff;
  padding: 2.5rem;
  position: relative;
  color: #333;
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
  color: rgba(51, 51, 51, 0.7);
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 0.2s;
}

.back-link a:hover {
  color: #333;
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
  font-weight: 800;
  margin-bottom: 0.5rem;
  color: #333;
}

.account-switch {
  font-size: 0.875rem;
  margin-bottom: 2rem;
  color: rgba(51, 51, 51, 0.7);
}

.account-switch a {
  color: #050505;
  text-decoration: none;
  font-weight: 600;
}

.account-switch a:hover {
  text-decoration: underline;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  position: relative;
}

.form-group label {
  font-size: 0.9rem;
  font-weight: 500;
  color: rgba(51, 51, 51, 0.7);
  margin-bottom: 0.5rem;
  display: block;
}

.form-group input {
  width: 100%;
  padding: 0.875rem 1rem;
  background-color: rgba(255, 235, 59, 0.05);
  border: 1px solid rgba(255, 235, 59, 0.3);
  border-radius: 8px;
  color: #333;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.form-group input:focus {
  outline: none;
  border-color: #ffeb3b;
  background-color: rgba(255, 235, 59, 0.1);
}

.form-group input::placeholder {
  color: rgba(51, 51, 51, 0.5);
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
  color: rgba(51, 51, 51, 0.5);
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
  background-color: rgba(255, 235, 59, 0.05);
  border: 1px solid rgba(255, 235, 59, 0.3);
  border-radius: 8px;
  color: rgba(51, 51, 51, 0.7);
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
  background-color: rgba(255, 235, 59, 0.2);
  border-color: #ffeb3b;
  color: #333;
}

.submit-btn {
  width: 100%;
  padding: 0.875rem;
  margin-top: 0.5rem;
  background-color: #ffeb3b;
  color: #333;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 10px rgba(255, 235, 59, 0.3);
}

.submit-btn:hover {
  background-color: #ffe100;
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(255, 235, 59, 0.4);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.loader {
  display: inline-block;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid rgba(51, 51, 51, 0.3);
  border-radius: 50%;
  border-top-color: #333;
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
    padding: 4rem 1rem;
  }
  
  .auth-container {
    border-radius: 16px;
  }
  
  .form-panel {
    padding: 1.5rem 1rem;
  }
  
  .back-link {
    position: static;
    margin-bottom: 1rem;
    text-align: right;
  }
  
  .form-title {
    font-size: 1.5rem;
  }
}
</style>