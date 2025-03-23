<template>
  <div class="top-nav-container" :class="{ 'nav-hidden': isScrolled }">
    <nav class="top-nav">
      <div class="logo-container">
        <a @click="goToDashboard" class="logo-link">
          <div class="logo">
            <img :src="logoImage" alt="Class Logo" class="class-logo" />
          </div>
          <span class="brand-name">Euphoria Tutorials</span>
        </a>
      </div>

      <!-- Desktop Navigation -->
      <ul class="nav-list desktop-nav">
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
            <span class="nav-text">Home</span>
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
            <span class="nav-text">About Us</span>
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
            <span class="nav-text">Reviews</span>
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
            <span class="nav-text">Contact</span>
          </router-link>
        </li>
      </ul>

      <!-- Right side controls -->
      <div class="right-controls">
        <!-- Login Button -->
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
            <span class="nav-text login-text">Login</span>
          </router-link>
        </div>

        <!-- Mobile Menu Button (Three Dots) -->
        <div class="mobile-menu-container">
          <button class="mobile-menu-button" @click="mobileMenuOpen = !mobileMenuOpen">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="12" cy="12" r="1"></circle>
              <circle cx="19" cy="12" r="1"></circle>
              <circle cx="5" cy="12" r="1"></circle>
            </svg>
          </button>

          <!-- Mobile Menu Dropdown -->
          <div class="mobile-menu" v-if="mobileMenuOpen">
            <router-link
              to="/"
              class="mobile-menu-item"
              :class="{ active: activeItem === '/' }"
              @click="setActiveAndClose('/')"
            >
              <svg
                viewBox="0 0 24 24"
                width="20"
                height="20"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
              >
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
              <span>Home</span>
            </router-link>

            <router-link
              to="/about"
              class="mobile-menu-item"
              :class="{ active: activeItem === '/about' }"
              @click="setActiveAndClose('/about')"
            >
              <svg
                viewBox="0 0 24 24"
                width="20"
                height="20"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
              >
                <circle cx="12" cy="7" r="4"></circle>
                <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"></path>
              </svg>
              <span>About Us</span>
            </router-link>

            <router-link
              to="/reviews"
              class="mobile-menu-item"
              :class="{ active: activeItem === '/reviews' }"
              @click="setActiveAndClose('/reviews')"
            >
              <svg
                viewBox="0 0 24 24"
                width="20"
                height="20"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
              >
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
              </svg>
              <span>Reviews</span>
            </router-link>

            <router-link
              to="/contact"
              class="mobile-menu-item"
              :class="{ active: activeItem === '/contact' }"
              @click="setActiveAndClose('/contact')"
            >
              <svg
                viewBox="0 0 24 24"
                width="20"
                height="20"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
              >
                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
              </svg>
              <span>Contact</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
/* eslint-disable */
// Import the logo image
import logoImage from '@/assets/images/CLogo.jpg';

export default {
  name: "TopNav",
  data() {
    return {
      activeItem: "/",
      userType: null, // Will store 'teacher', 'parent', or null
      logoImage: logoImage, // Make the imported logo available to the template
      isScrolled: false,
      lastScrollPosition: 0,
      mobileMenuOpen: false
    };
  },
  mounted() {
    // Set active item based on current route
    this.activeItem = this.$route.path;
    
    // Check user login status and type
    this.checkUserStatus();
    
    // Add scroll event listener
    window.addEventListener('scroll', this.handleScroll);
    
    // Add click outside listener to close mobile menu
    document.addEventListener('click', this.handleClickOutside);
  },
  // Changed from beforeDestroy to beforeUnmount to fix the ESLint warning
  beforeUnmount() {
    // Clean up event listeners
    window.removeEventListener('scroll', this.handleScroll);
    document.removeEventListener('click', this.handleClickOutside);
  },
  methods: {
    checkUserStatus() {
      // This is a placeholder - implement based on your authentication system
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
    },
    
    // Handle scroll behavior
    handleScroll() {
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;
      
      // Determine if we're scrolling up or down
      if (currentScrollPosition < 0) {
        return;
      }
      
      // Show navbar if scrolling up or at the top
      if (currentScrollPosition < 50 || currentScrollPosition < this.lastScrollPosition) {
        this.isScrolled = false;
      } else {
        // Hide navbar if scrolling down and not at the top
        this.isScrolled = true;
        // Close mobile menu when scrolling
        this.mobileMenuOpen = false;
      }
      
      this.lastScrollPosition = currentScrollPosition;
    },
    
    // Set active item and close mobile menu
    setActiveAndClose(route) {
      this.activeItem = route;
      this.mobileMenuOpen = false;
    },
    
    // Close mobile menu when clicking outside
    handleClickOutside(event) {
      const mobileMenuContainer = this.$el.querySelector('.mobile-menu-container');
      if (this.mobileMenuOpen && mobileMenuContainer && !mobileMenuContainer.contains(event.target)) {
        this.mobileMenuOpen = false;
      }
    }
  },
};
</script>

<style scoped>
/* Import Google Fonts - Montserrat for headings, Roboto for body text */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;700&display=swap');

:root {
  --yellow-primary: #FFC107;
  --yellow-secondary: #FFD54F;
  --yellow-light: #FFF8E1;
  --teal-dark: #00796b;
  --teal-medium: #009688;
  --teal-light: #b2dfdb;
  --text-dark: #1a1a2e;
  --text-medium: #3a506b;
  --border-color: rgba(0, 0, 0, 0.1);
}

.top-nav-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 50;
  font-family: 'Montserrat', sans-serif;
  padding: 10px 20px;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 150, 136, 0.1);
  transition: transform 0.3s ease-in-out;
  border-bottom: 1px solid var(--border-color);
}

/* Hide navbar when scrolled down */
.nav-hidden {
  transform: translateY(-100%);
}

.top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  height: 70px;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo-link {
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: transform 0.3s ease;
  text-decoration: none;
  gap: 12px;
}

.logo-link:hover {
  transform: scale(1.02);
}

.logo {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: white;
  box-shadow: 0 4px 10px rgba(255, 193, 7, 0.2);
  overflow: hidden;
  border: 1px solid var(--border-color);
}

.class-logo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.brand-name {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 1.25rem;
  color: var(--yellow-primary);
  letter-spacing: -0.01em;
}

/* Desktop Navigation */
.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  gap: 1.5rem;
}

.nav-item {
  display: flex;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 12px;
  transition: all 0.3s ease;
  color: var(--text-medium);
  text-decoration: none;
}

.nav-link:hover {
  background-color: rgba(0, 150, 136, 0.05);
  color: var(--teal-medium);
}

.nav-link.active {
  background: linear-gradient(45deg, var(--teal-medium), var(--teal-dark));
  color: white;
  box-shadow: 0 4px 10px rgba(0, 150, 136, 0.2);
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

.nav-text {
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
}

/* Right side controls container */
.right-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-right: 10px; /* Added margin to prevent items from touching the edge */
}

/* Mobile Menu Button and Dropdown */
.mobile-menu-container {
  position: relative;
  display: none;
}

.mobile-menu-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 193, 7, 0.1);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  cursor: pointer;
  color: var(--yellow-primary);
  transition: all 0.3s ease;
  border: 1px solid var(--border-color);
}

.mobile-menu-button:hover {
  background-color: rgba(255, 193, 7, 0.2);
}

.mobile-menu {
  position: absolute;
  top: 50px;
  right: 0;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  width: 180px;
  padding: 10px 0;
  z-index: 100;
  border: 1px solid var(--border-color);
}

.mobile-menu-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  color: var(--text-medium);
  text-decoration: none;
  transition: all 0.3s ease;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
}

.mobile-menu-item:hover {
  background-color: rgba(0, 150, 136, 0.05);
  color: var(--teal-medium);
}

.mobile-menu-item.active {
  color: var(--yellow-primary);
  font-weight: 600;
}

/* Profile section */
.profile-container {
  position: relative;
}

.profile-link {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  border-radius: 12px;
  transition: all 0.3s ease;
  border: 1px solid var(--border-color);
  background-color: var(--yellow-primary);
  color: var(--text-dark);
  text-decoration: none;
  gap: 8px;
  box-shadow: 0 4px 10px rgba(255, 193, 7, 0.15);
}

.profile-link:hover,
.profile-link.active {
  background-color: var(--yellow-secondary);
  box-shadow: 0 6px 12px rgba(255, 193, 7, 0.25);
  transform: translateY(-2px);
}

.profile-photo {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-dark);
}

.login-text {
  font-weight: 600;
  font-family: 'Montserrat', sans-serif;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }
  
  .mobile-menu-container {
    display: block;
  }
  
  .logo {
    width: 45px;
    height: 45px;
  }
  
  .brand-name {
    font-size: 1.1rem;
  }
  
  .profile-link {
    padding: 6px 14px;
  }
  
  .top-nav {
    height: 60px;
  }
  
  .right-controls {
    margin-right: 15px; /* Increased margin for mobile view */
  }
}

@media (max-width: 480px) {
  .top-nav-container {
    padding: 8px 12px;
  }
  
  .top-nav {
    height: 50px;
  }
  
  .logo {
    width: 40px;
    height: 40px;
  }
  
  .brand-name {
    font-size: 0.9rem;
  }
  
  .mobile-menu-button {
    width: 35px;
    height: 35px;
  }
  
  .profile-link {
    padding: 5px 10px;
  }
  
  .login-text {
    font-size: 0.8rem;
  }
  
  .right-controls {
    gap: 0.5rem;
    margin-right: 20px; /* Further increased margin for smaller screens */
  }
  
  .mobile-menu {
    right: -20px; /* Move dropdown menu to the left */
  }
}

/* Very small screens */
@media (max-width: 360px) {
  .brand-name {
    max-width: 120px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .mobile-menu {
    width: 160px;
    right: -30px; /* Move dropdown menu even more to the left */
  }
  
  .right-controls {
    margin-right: 25px; /* Added even more margin for very small screens */
  }
}

@media (prefers-reduced-motion: reduce) {
  .top-nav-container,
  .logo-link,
  .nav-link,
  .profile-link {
    transition: none;
  }
}
</style>