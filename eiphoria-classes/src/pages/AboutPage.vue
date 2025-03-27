<template>
  <section class="about-hero">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <!-- Animated Hero Header -->
    <div class="hero-content">
      <h1 class="hero-title">
        Why <span class="gradient-text">Choose</span> Us
        <span class="arrow-icon">→</span>
      </h1>
      <p class="hero-subtitle">
        Dedicated to nurturing young minds and helping every student reach their full academic potential
      </p>

      <!-- Stats Grid -->
      <div class="stats-grid">
        <div
          v-for="(stat) in stats"
          :key="stat.id"
          class="stat-card"
          :class="{ 'featured': stat.featured }"
        >
          <div class="stat-content">
            <h2 class="stat-value">{{ stat.value }}</h2>
            <p class="stat-label">{{ stat.label }}</p>
          </div>
          <div class="hover-bg"></div>
        </div>
      </div>
    </div>
  </section>
  <MissionComponent/>
  <ClassroomPreviewComponent/>
  <TeamComponent/>
  <ValuesComponent/>
</template>

<script setup>
import ValuesComponent from "@/components/AboutPageComponents/ValuesComponent.vue";
import TeamComponent from "@/components/AboutPageComponents/TeamComponent.vue";
import MissionComponent from "@/components/AboutPageComponents/MissionComponent.vue";
import ClassroomPreviewComponent from "@/components/AboutPageComponents/ClassroomPreviewComponent.vue";
import { ref } from "vue";

const stats = ref([
  {
    id: 1,
    value: "15+",
    label: "Years of Excellence",
    featured: false,
  },
  {
    id: 2,
    value: "1500+",
    label: "Happy Students",
    featured: false,
  },
  {
    id: 3,
    value: "98%",
    label: "Parent Satisfaction",
    featured: false,
  },
  {
    id: 4,
    value: "92%",
    label: "Success Rate",
    featured: true,
  },
]);
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.about-hero {
  position: relative;
  min-height: 100vh;
  background: white;
  padding: 2rem  1rem; /* Increased top padding from 0.5rem to 8rem */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  font-family: 'Poppins', sans-serif;
}

@media (max-width: 768px) {
  .about-hero {
    padding: 6rem 1.5rem 2rem; /* Adjusted for mobile */
  }
  
  .hero-title {
    font-size: 3rem;
    flex-wrap: wrap;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: 3rem;
  }
}

@media (max-width: 480px) {
  .about-hero {
    padding: 5rem 1rem 2rem; /* Further adjusted for smaller screens */
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .stat-card {
    padding: 2rem 1rem;
  }
  
  .stat-value {
    font-size: 2.5rem;
  }
}
.floating-element {
  position: absolute;
  background: linear-gradient(45deg, rgba(255, 193, 7, 0.1), rgba(255, 213, 79, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.hero-title {
  font-family: 'Poppins', sans-serif;
  font-size: 4rem;
  font-weight: 700;
  color: #333;
}

.gradient-text {
  background: linear-gradient(45deg, #fff700, #fff700);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.arrow-icon {
  color: #ffbf00;
}

.hero-subtitle {
  color: #666;
}

.stat-card {
  background-color: white;
  box-shadow: 0 10px 25px rgba(255, 193, 7, 0.1);
}

.hover-bg {
  background: linear-gradient(135deg, #FFC107, #FFD54F);
}

.stat-card.featured {
  background: linear-gradient(135deg, #FFC107, #FFD54F);
}

.stat-card:hover {
  box-shadow: 0 15px 35px rgba(255, 193, 7, 0.2);
}

.stat-value {
  font-family: 'Poppins', sans-serif;
  color: #333;
}

.stat-label {
  color: #666;
}

.floating-element:nth-child(1) { width: 300px; height: 300px; top: 5%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { width: 200px; height: 200px; top: 65%; left: 85%; animation-delay: -4s; }
.floating-element:nth-child(3) { width: 350px; height: 350px; top: 35%; left: 55%; animation-delay: -8s; }
.floating-element:nth-child(4) { width: 150px; height: 150px; top: 75%; left: 15%; animation-delay: -12s; }
.floating-element:nth-child(5) { width: 250px; height: 250px; top: 20%; left: 75%; animation-delay: -16s; }
.floating-element:nth-child(6) { width: 180px; height: 180px; top: 80%; left: 45%; animation-delay: -5s; }
.floating-element:nth-child(7) { width: 220px; height: 220px; top: 15%; left: 35%; animation-delay: -9s; }
.floating-element:nth-child(8) { width: 270px; height: 270px; top: 60%; left: 70%; animation-delay: -13s; }

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(3deg); }
  100% { transform: translateY(-40px) rotate(-3deg); }
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 1200px;
  text-align: center;
}

.hero-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 4rem;
  font-weight: 800;
  color: #2D3748;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.gradient-text {
  background: linear-gradient(45deg, #dad725, #3e3c15);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.arrow-icon {
  font-size: 3rem;
  color: #4B96F3;
  animation: bounce 2s infinite alternate;
}

@keyframes bounce {
  0% { transform: translateX(0); }
  100% { transform: translateX(10px); }
}

.hero-subtitle {
  font-size: 1.5rem;
  color: #4A5568;
  max-width: 700px;
  margin: 0 auto 4rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
  max-width: 1200px;
  width: 95%;
  margin-left: auto;
  margin-right: auto;
}

.stat-card {
  background-color: white;
  padding: 2.5rem 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 10px 25px rgba(75, 150, 243, 0.1);
  transition: all 0.3s ease-in-out;
  position: relative;
  overflow: hidden;
  min-width: 220px;
}

.hover-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #cf2d0d, #3178E6);
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 0;
}

.stat-card:hover .hover-bg {
  opacity: 1;
}

.stat-card.featured {
  background: linear-gradient(135deg, #d3431b, #3178E6);
}

.stat-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 35px rgba(75, 150, 243, 0.2);
}

.stat-content {
  position: relative;
  z-index: 1;
}

.stat-value {
  font-family: 'Quicksand', sans-serif;
  font-size: 3rem;
  font-weight: 800;
  color: #2D3748;
  margin-bottom: 0.75rem;
  transition: color 0.4s ease;
}

.stat-card:hover .stat-value {
  color: white;
}

.stat-card.featured .stat-value {
  color: white;
}

.stat-label {
  font-size: 1.125rem;
  color: #4A5568;
  line-height: 1.4;
  transition: color 0.4s ease;
}

.stat-card:hover .stat-label {
  color: rgba(255, 255, 255, 0.9);
}

.stat-card.featured .stat-label {
  color: rgba(255, 255, 255, 0.9);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    max-width: 800px;
  }
  
  .stat-card {
    min-width: 230px;
  }
}

@media (max-width: 768px) {
  .about-hero {
    padding: 4rem 1.5rem 2rem;
    min-height: 85vh;
  }
  
  .hero-title {
    font-size: 3rem;
    flex-wrap: wrap;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: 3rem;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr); /* Changed from 1fr to repeat(2, 1fr) */
    gap: 1rem; /* Reduced gap for better fit */
  }
  
  .stat-card {
    padding: 1.5rem 1rem;
    min-width: auto; /* Remove min-width constraint */
  }
  
  .stat-value {
    font-size: 2rem; /* Slightly reduced font size */
  }
  
  .stat-label {
    font-size: 0.9rem; /* Adjusted label size */
  }
}
</style>