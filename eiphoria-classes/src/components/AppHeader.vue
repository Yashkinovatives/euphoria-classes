<template>
  <div class="side-nav-container" :class="{ 'hide-nav': hideSidebar }">
    <div class="glow-effect"></div>
    <nav class="side-nav">
      <div class="logo-container">
        <router-link to="/">
          <div class="logo">
            <svg
              viewBox="0 0 24 24"
              width="24"
              height="24"
              stroke="currentColor"
              stroke-width="2"
              fill="none"
            >
              <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
              <path d="M2 17l10 5 10-5"></path>
              <path d="M2 12l10 5 10-5"></path>
            </svg>
          </div>
        </router-link>
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

        <li class="nav-item" @click="activeItem = '/courses'">
          <router-link
            to="/contact"
            class="nav-link"
            :class="{ active: activeItem === '/courses' }"
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
                :class="{ 'icon-active': activeItem === '/courses' }"
              >
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                <path
                  d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"
                ></path>
              </svg>
            </span>
            <span class="tooltip">Courses</span>
          </router-link>
        </li>

        <li class="nav-item" @click="activeItem = '/categories'">
          <router-link
            to="/reviews"
            class="nav-link"
            :class="{ active: activeItem === '/categories' }"
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
                :class="{ 'icon-active': activeItem === '/categories' }"
              >
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            </span>
            <span class="tooltip">Categories</span>
          </router-link>
        </li>
      </ul>

      <div class="profile-container">
        <router-link
          to="/login"
          class="profile-link"
          :class="{ active: activeItem === '/profile' }"
          @click="activeItem = '/profile'"
        >
          <div class="profile-photo">
            <img src="https://i.pravatar.cc/100" alt="Profile photo" />
          </div>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "SideNav",
  data() {
    return {
      activeItem: "/",
      hideSidebar: false,
      lastScrollY: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const currentScrollY = window.scrollY;
      if (currentScrollY > this.lastScrollY) {
        this.hideSidebar = true;
      } else {
        this.hideSidebar = false;
      }
      this.lastScrollY = currentScrollY;
    },
  },
};
</script>

<style scoped>
.side-nav-container {
  position: fixed;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 50;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.glow-effect {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #7C3AED, #A855F7);
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
  background: #7C3AED, #A855F7;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 25px 0;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}

.logo-container {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.logo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background-color: #111;
  color: white;
}

.notification-dot {
  position: absolute;
  width: 8px;
  height: 8px;
  background-color: #ff6b6b;
  border-radius: 50%;
  top: 5px;
  right: 16px;
}

.cart-badge {
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 36px;
  height: 36px;
  background-color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  color: #333;
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
  color: #888;
}

.nav-link:hover {
  background-color: rgba(0, 0, 0, 0.05);
  color: #333;
}

.nav-link.active {
  background-color: #111;
  color: white;
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
  background-color: #333;
  color: white;
  font-size: 0.8rem;
  padding: 0.5rem 0.8rem;
  border-radius: 6px;
  opacity: 0;
  visibility: hidden;
  transform: translateX(-8px);
  transition: all 0.3s ease;
  white-space: nowrap;
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
}

.profile-link {
  display: block;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.profile-link:hover,
.profile-link.active {
  border-color: #ff6b6b;
  transform: scale(1.05);
}

.profile-photo {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
}

.profile-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 768px) {
  .side-nav-container {
    left: 10px;
  }

  .side-nav {
    width: 60px;
    height: 400px;
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
