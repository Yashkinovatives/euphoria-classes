<template>
  <div class="side-nav-container" :class="{ 'hide-nav': hideSidebar }">
    <div class="glow-effect"></div>
    <nav class="side-nav">
      <div class="logo-container">
        <a @click="goToDashboard" class="logo-link">
          <div class="logo">
            <!-- Use the imported logo -->
            <img :src="logoImage" alt="Class Logo" class="class-logo" />
          </div>
        </a>
      </div>

      <ul class="nav-list">
        <li class="nav-item" @click="activeItem = '/'">
          <router-link
            to="/"
            class="nav-link"
            :class="{ active: activeItem === '/' }"
          >
            <span class="icon-wrapper">
              <svg
                viewBox="0 0 24 24"
                width="24"
                height="24"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
                class="icon"
                :class="{ 'icon-active': activeItem === '/' }"
              >
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
            </span>
            <span class="tooltip">Home</span>
          </router-link>
        </li>

        <li class="nav-item" @click="activeItem = '/about'">
          <router-link
            to="/about"
            class="nav-link"
            :class="{ active: activeItem === '/about' }"
          >
            <span class="icon-wrapper">
              <svg
                viewBox="0 0 24 24"
                width="24"
                height="24"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
                class="icon"
                :class="{ 'icon-active': activeItem === '/about' }"
              >
                <circle cx="12" cy="7" r="4"></circle>
                <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"></path>
              </svg>
            </span>
            <span class="tooltip">About Us</span>
          </router-link>
        </li>

        <li class="nav-item" @click="activeItem = '/reviews'">
          <router-link
            to="/reviews"
            class="nav-link"
            :class="{ active: activeItem === '/reviews' }"
          >
            <span class="icon-wrapper">
              <svg
                viewBox="0 0 24 24"
                width="24"
                height="24"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
                class="icon"
                :class="{ 'icon-active': activeItem === '/reviews' }"
              >
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <path d="M14 8h.01"></path>
                <path d="M10 8h.01"></path>
                <path d="M18 8h.01"></path>
              </svg>
            </span>
            <span class="tooltip">Reviews</span>
          </router-link>
        </li>

        <li class="nav-item" @click="activeItem = '/contact'">
          <router-link
            to="/contact"
            class="nav-link"
            :class="{ active: activeItem === '/contact' }"
          >
            <span class="icon-wrapper">
              <svg
                viewBox="0 0 24 24"
                width="24"
                height="24"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
                class="icon"
                :class="{ 'icon-active': activeItem === '/contact' }"
              >
                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
              </svg>
            </span>
            <span class="tooltip">Contact</span>
          </router-link>
        </li>
      </ul>

      <div class="profile-container">
        <router-link
          to="/login"
          class="profile-link"
          :class="{ active: activeItem === '/login' }"
          @click="activeItem = '/login'"
        >
          <div class="profile-photo login-avatar">
            <svg
              viewBox="0 0 24 24"
              width="22"
              height="22"
              stroke="currentColor"
              stroke-width="2"
              fill="none"
            >
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <span class="tooltip profile-tooltip">Login</span>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
// Import the logo image
import logoImage from '@/assets/images/CLogo.jpg';

export default {
  name: "SideNav",
  data() {
    return {
      activeItem: "/",
      hideSidebar: false,
      lastScrollY: 0,
      userType: null, // Will store 'teacher', 'parent', or null
      logoImage: logoImage, // Make the imported logo available to the template
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
    
    // Set active item based on current route
    this.activeItem = this.$route.path;
    
    // Check user login status and type (this is a placeholder - implement based on your auth system)
    this.checkUserStatus();
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const currentScrollY = window.scrollY;
      // Only apply scroll-hiding on larger screens
      if (window.innerWidth > 480) {
        if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
          this.hideSidebar = true;
        } else {
          this.hideSidebar = false;
        }
      } else {
        // Always show on mobile
        this.hideSidebar = false;
      }
      this.lastScrollY = currentScrollY;
    },
    
    checkUserStatus() {
      // This is a placeholder - implement based on your authentication system
      // Example: read from store, local storage, session, etc.
      // Get user login status and type from your auth system
      
      // For demonstration purposes:
      // Check if user is logged in and determine type (teacher/parent)
      const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
      if (isLoggedIn) {
        this.userType = localStorage.getItem('userType'); // 'teacher' or 'parent'
      } else {
        this.userType = null;
      }
    },
    
    goToDashboard() {
      // Redirect based on user type
      if (this.userType === 'teacher') {
        this.$router.push('/teacher-dashboard');
      } else if (this.userType === 'parent') {
        this.$router.push('/parent-dashboard');
      } else {
        // If not logged in, go to homepage
        this.$router.push('/');
      }
    }
  },
};
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.side-nav-container {
  position: fixed;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 50;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: 'Nunito', sans-serif;
}

.glow-effect {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  filter: blur(30px);
  opacity: 0.2;
  border-radius: 30px;
  z-index: -1;
}

.hide-nav {
  transform: translateY(-50%) translateX(-100px);
  opacity: 0;
}

.side-nav {
  width: 70px;
  height: 500px;
  background: #FFFFFF;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 25px 0;
  box-shadow: 0 10px 30px rgba(75, 150, 243, 0.1);
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.logo-container {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.logo-link {
  cursor: pointer;
  transition: transform 0.3s ease;
}

.logo-link:hover {
  transform: scale(1.05);
}

.logo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: white;
  box-shadow: 0 4px 10px rgba(75, 150, 243, 0.3);
  overflow: hidden;
}

.class-logo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.8rem;
  width: 100%;
}

.nav-item {
  width: 100%;
  display: flex;
  justify-content: center;
}

.nav-link {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  transition: all 0.3s ease;
  color: #4A5568;
}

.nav-link:hover {
  background-color: rgba(75, 150, 243, 0.1);
  color: #3178E6;
}

.nav-link.active {
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  color: white;
  box-shadow: 0 4px 10px rgba(75, 150, 243, 0.2);
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon {
  transition: all 0.3s ease;
}

.icon-active {
  color: white;
}

.tooltip {
  position: absolute;
  left: calc(100% + 12px);
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  color: white;
  font-size: 0.8rem;
  padding: 0.5rem 0.8rem;
  border-radius: 8px;
  opacity: 0;
  visibility: hidden;
  transform: translateX(-8px);
  transition: all 0.3s ease;
  white-space: nowrap;
  font-family: 'Quicksand', sans-serif;
  font-weight: 600;
  box-shadow: 0 4px 10px rgba(75, 150, 243, 0.2);
}

.tooltip::before {
  content: '';
  position: absolute;
  left: -6px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  border-right: 6px solid #4B96F3;
}

.nav-link:hover .tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(0);
}

.profile-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 20px;
  position: relative;
}

.profile-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 2px solid rgba(75, 150, 243, 0.3);
  position: relative;
  background-color: rgba(75, 150, 243, 0.1);
  color: #3178E6;
}

.profile-tooltip {
  bottom: -40px;
  left: 50%;
  transform: translateX(-50%) translateY(8px);
}

.profile-link:hover .profile-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

.profile-tooltip::before {
  display: none;
}

.profile-link:hover,
.profile-link.active {
  border-color: #4B96F3;
  transform: scale(1.05);
  background-color: rgba(75, 150, 243, 0.2);
}

.profile-photo {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login-avatar {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .side-nav-container {
    left: 15px;
  }
  
  .side-nav {
    height: 450px;
  }
}

@media (max-width: 768px) {
  .side-nav-container {
    left: 10px;
  }

  .side-nav {
    width: 60px;
    height: 400px;
  }
  
  .logo {
    width: 36px;
    height: 36px;
  }
  
  .nav-link {
    width: 38px;
    height: 38px;
  }
  
  .tooltip {
    font-size: 0.75rem;
    padding: 0.4rem 0.7rem;
  }
}

@media (max-width: 480px) {
  .side-nav-container {
    bottom: 20px;
    top: auto;
    left: 50%;
    transform: translateX(-50%);
    position: fixed;
  }
  
  .hide-nav {
    transform: translateY(100px) translateX(-50%);
    opacity: 0;
  }
  
  .side-nav {
    width: 300px;
    height: 70px;
    flex-direction: row;
    padding: 0 20px;
  }
  
  .logo-container {
    margin-bottom: 0;
  }
  
  .nav-list {
    flex-direction: row;
    gap: 1rem;
    justify-content: center;
  }
  
  .profile-container {
    margin-top: 0;
  }
  
  .tooltip {
    top: -45px;
    left: 50%;
    transform: translateX(-50%) translateY(-8px);
  }
  
  .tooltip::before {
    left: 50%;
    top: auto;
    bottom: -6px;
    transform: translateX(-50%) rotate(90deg);
  }
  
  .nav-link:hover .tooltip {
    transform: translateX(-50%) translateY(0);
  }
  
  .profile-tooltip {
    bottom: auto;
    top: -45px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .side-nav-container,
  .nav-link,
  .tooltip,
  .profile-link {
    transition: none;
  }
}
</style>