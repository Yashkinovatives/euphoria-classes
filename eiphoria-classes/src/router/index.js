import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import AboutPage from "@/pages/AboutPage.vue";
import ContactPage from "@/pages/ContactPage.vue";
import ReviewPage from "@/pages/ReviewPage.vue";
import LoginSignup from "@/pages/LoginSignup.vue";
import TeacherDashboard from "@/pages/TeacherDashboard.vue";
import ParentDashboard from "@/pages/ParentDashboard.vue";

// Middleware to protect routes (Requires authentication)

const routes = [
  { path: "/", component: HomePage },
  { path: "/about", component: AboutPage },
  { path: "/contact", component: ContactPage },
  { path: "/reviews", component: ReviewPage },
  { path: "/login", component: LoginSignup },
  { path: '/teacher-dashboard', component: TeacherDashboard },
  { path: '/parent-dashboard', component: ParentDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
