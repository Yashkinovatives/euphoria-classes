<template>
  <div class="main-container">
    <!-- Abstract shapes for background effect -->
    <div class="shape shape-1"></div>
    <div class="shape shape-2"></div>
    <div class="shape shape-3"></div>
    <div class="shape shape-4"></div>
    
    <div class="content-wrapper">
      <!-- Main content pushed down to account for navbar -->
      <div class="hero-section">
        <div class="left-column">
          <h1 class="main-heading">
            <span class="line">Helping</span>
            <span class="line">Children</span>
            <span class="line">Discover Their</span>
            <span class="line accent">Potential</span>
          </h1>
          
          <p class="subtitle">
            Stay connected with your child's educational journey through our interactive platform. 
            Monitor progress, view assignments, and celebrate achievements all in one place.
          </p>
          
          <div class="action-buttons">
            <button class="action-button primary">Get Started</button>
            <button class="action-button secondary">Learn More</button>
          </div>
        </div>
        
        <div class="right-column">
          <div class="stats-container">
            <div class="stat-item" v-for="(stat, index) in stats" :key="index" ref="statItems">
              <div class="stat-number">
                <span ref="countElements">{{ stat.currentValue }}</span>{{ stat.suffix }}
              </div>
              <div class="stat-label">{{ stat.label }}</div>
            </div>
          </div>
          
          <div class="card-grid">
            <div class="info-card" v-for="(card, index) in infoCards" :key="index">
              <div class="card-icon">{{ card.icon }}</div>
              <div class="card-title">{{ card.title }}</div>
            </div>
          </div>
        </div>
      </div>
      
      <section class="features-section">
        <h2 class="section-title">Why Parents Choose Us</h2>
        
        <div class="features-grid">
          <div class="feature" v-for="(feature, index) in features" :key="index">
            <div class="feature-header">
              <div class="modern-icon" v-html="feature.modernIcon"></div>
              <h3 class="feature-title">{{ feature.title }}</h3>
            </div>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
  <AboutUsComponent />
  <ScrollingSection />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import AboutUsComponent from '@/components/HomePageComponents/AboutUsComponent.vue';
import ScrollingSection from '@/components/HomePageComponents/ScrollingSection.vue';

const statItems = ref([]);
const countElements = ref([]);

const stats = ref([
  { value: '1500+', currentValue: '0', endValue: 1500, suffix: '+', label: 'Happy Students' },
  { value: '15+', currentValue: '0', endValue: 15, suffix: '+', label: 'Years of Excellence' },
  { value: '98%', currentValue: '0', endValue: 98, suffix: '%', label: 'Parent Satisfaction' }
]);

const infoCards = [
  { icon: '🎨', title: 'Creative Arts' },
  { icon: '🧮', title: 'Mathematics' },
  { icon: '🔬', title: 'Sciences' },
  { icon: '📝', title: 'Languages' }
];

const features = [
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FFC107" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                  <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>`,
    title: 'Engaging Curriculum',
    description: 'Our curriculum balances fun and learning, designed to keep children motivated while building essential skills for their future.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FFC107" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <path d="M21 15l-5-5L5 21"></path>
                </svg>`,
    title: 'Real-time Progress Updates',
    description: 'Get instant notifications about assignments, grades, and milestones so you\'re always informed about your child\'s progress.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FFC107" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>`,
    title: 'Parent-Teacher Partnership',
    description: 'Schedule meetings, exchange messages, and collaborate with teachers to create the best learning environment for your child.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FFC107" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 22s-8-4.5-8-11.8A8 8 0 0 1 12 2a8 8 0 0 1 8 8.2c0 7.3-8 11.8-8 11.8z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>`,
    title: 'Personalized Learning Path',
    description: 'Every child learns differently. Our adaptive system tailors resources and activities to match your child\'s unique learning style.',
  }
];

onMounted(() => {
  // Wait for a short delay to ensure the page is fully loaded
  setTimeout(() => {
    animateCounters();
    
    // Add intersection observer for scroll-triggered animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    
    // Observe elements that should animate on scroll
    document.querySelectorAll('.feature, .info-card').forEach(el => {
      observer.observe(el);
    });
  }, 300);
});

const animateCounters = () => {
  stats.value.forEach((stat, index) => {
    const endValue = stat.endValue;
    const duration = 3000; // 3 seconds for animation
    const startTime = Date.now();
    const startValue = 0;
    
    const updateCounter = () => {
      const currentTime = Date.now();
      const elapsedTime = currentTime - startTime;
      
      if (elapsedTime < duration) {
        // Calculate the current value based on elapsed time
        const progress = elapsedTime / duration;
        // Use easeOutQuad easing function for smoother animation
        const easedProgress = 1 - (1 - progress) * (1 - progress);
        const currentValue = Math.floor(startValue + easedProgress * (endValue - startValue));
        
        // Update the displayed value
        stats.value[index].currentValue = currentValue.toString();
        
        // Continue animation
        requestAnimationFrame(updateCounter);
      } else {
        // Animation complete, set to final value
        stats.value[index].currentValue = endValue.toString();
      }
    };
    
    // Start animation
    updateCounter();
  });
};
</script>

<style scoped>
/* Import Google Fonts - Montserrat for headings, Roboto for body text */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;700&display=swap');

:root {
  --yellow-primary: #FFC107;
  --yellow-secondary: #FFD54F;
  --yellow-light: #FFF8E1;
  --text-dark: #1a1a2e;
  --text-medium: #3a506b;
  --card-bg: rgba(255, 255, 255, 0.8);
  --shape-color-1: rgba(255, 193, 7, 0.1);
  --shape-color-2: rgba(255, 236, 179, 0.15);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #e9eaf4 0%, #f6f7f9 25%, #eceeeb 50%, #dee0f5 75%, #f1f2f7 100%);
  color: var(--text-dark);
  font-family: 'Roboto', sans-serif;
  position: relative;
  overflow: hidden;
  /* Added top padding to account for the navbar */
  padding-top: 130px;
}

/* Abstract shapes */
.shape {
  position: absolute;
  z-index: 0;
  filter: blur(70px);
  opacity: 0.5;
}

.shape-1 {
  width: 600px;
  height: 600px;
  background: var(--shape-color-1);
  top: -200px;
  right: -200px;
  border-radius: 100%;
}

.shape-2 {
  width: 400px;
  height: 400px;
  background: var(--shape-color-2);
  bottom: 10%;
  left: -100px;
  border-radius: 100%;
}

.shape-3 {
  width: 300px;
  height: 300px;
  background: var(--shape-color-1);
  top: 40%;
  left: 10%;
  border-radius: 100%;
}

.shape-4 {
  width: 500px;
  height: 500px;
  background: var(--shape-color-2);
  bottom: -200px;
  right: 15%;
  border-radius: 100%;
}

.content-wrapper {
  position: relative;
  z-index: 1;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* Hero section - adjusted spacing */
.hero-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  margin-top: 2rem;
  margin-bottom: 8rem;
}

.left-column {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.main-heading {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  color: var(--text-dark);
  letter-spacing: -0.02em;
}

.line {
  display: block;
}

.accent {
  color: var(--yellow-primary);
  position: relative;
}

.accent::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 1px;
  background: var(--yellow-secondary);
  bottom: -10px;
  left: 0;
  z-index: -1;
  opacity: 0.8;
}

.subtitle {
  font-family: 'Roboto', sans-serif;
  font-size: clamp(1rem, 2vw, 1.125rem);
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 3rem;
  max-width: 500px;
  font-weight: 400;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.action-button {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(0.875rem, 1.5vw, 1rem);
  font-weight: 600;
  padding: clamp(0.75rem, 2vw, 1rem) clamp(1.5rem, 3vw, 2rem);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  width: 100%;
  max-width: 240px;
}

.action-button.primary {
  background: var(--yellow-primary);
  color: var(--text-dark);
  box-shadow: 0 4px 12px rgba(255, 193, 7, 0.3);
}

.action-button.primary:hover {
  background: var(--yellow-secondary);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 193, 7, 0.4);
}

.action-button.secondary {
  background: transparent;
  border: 2px solid var(--yellow-primary);
  color: var(--yellow-primary);
}

.action-button.secondary:hover {
  background: var(--yellow-light);
  transform: translateY(-2px);
}

/* Right column */
.right-column {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-item {
  background: var(--card-bg);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 236, 179, 0.5);
  transition: all 0.3s ease;
  box-shadow: 0 4px 20px rgba(255, 193, 7, 0.1);
}

.stat-item:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(255, 193, 7, 0.15);
}

.stat-number {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  font-weight: 800;
  color: var(--yellow-primary);
  margin-bottom: 0.5rem;
}

.stat-label {
  font-family: 'Roboto', sans-serif;
  font-size: clamp(0.8rem, 1.5vw, 0.9rem);
  color: var(--text-medium);
  font-weight: 500;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.info-card {
  background: rgba(255, 248, 225, 0.3);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 193, 7, 0.15);
  box-shadow: 0 4px 12px rgba(255, 193, 7, 0.05);
}

.info-card:hover {
  background: rgba(255, 248, 225, 0.5);
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(255, 193, 7, 0.1);
}

.card-icon {
  font-size: clamp(1.5rem, 3vw, 2rem);
}

.card-title {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(1rem, 2vw, 1.25rem);
  font-weight: 600;
  color: var(--text-dark);
}

/* Features section */
.features-section {
  padding: 3rem 0;
}

.section-title {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(2rem, 4vw, 2.5rem);
  font-weight: 800;
  margin-bottom: 3rem;
  text-align: center;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
  color: var(--text-dark);
  letter-spacing: -0.02em;
}

.section-title::after {
  content: '';
  position: absolute;
  width: 50px;
  height: 4px;
  background: var(--yellow-primary);
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature {
  background: var(--card-bg);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 20px rgba(255, 193, 7, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.feature:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(255, 193, 7, 0.15);
}

.feature-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.modern-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5rem;
}

.feature-title {
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(1.1rem, 2vw, 1.25rem);
  font-weight: 700;
  color: var(--yellow-primary);
}

.feature-description {
  font-family: 'Roboto', sans-serif;
  color: var(--text-medium);
  line-height: 1.6;
  font-weight: 400;
  font-size: clamp(0.9rem, 1.5vw, 1rem);
  flex: 1;
}

/* Animation classes */
.animate-in {
  animation: fadeInUp 0.6s ease-out forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Enhanced Media queries for better responsiveness */
@media (max-width: 1200px) {
  .main-container {
    padding-top: 100px;
  }
  
  .hero-section {
    gap: 4rem;
  }
}

@media (max-width: 1024px) {
  .hero-section {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  
  .right-column {
    order: 2; /* Put right column AFTER left column */
  }
  
  .content-wrapper {
    padding: 1.5rem;
  }
  
  .main-heading {
    text-align: center;
  }
  
  .subtitle {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
  }
  
  .action-buttons {
    justify-content: center;
  }
}

/* Mobile view adjustments */
@media (max-width: 768px) {
  .main-container {
    padding-top: 80px;
  }
  
  /* Keep the action buttons in one row */
  .action-buttons {
    flex-direction: row;
    justify-content: center;
    gap: 0.75rem;
  }
  
  .action-button {
    flex: 1;
    max-width: calc(50% - 0.375rem);
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
  }
  
  /* Stats layout: 2 in first row, 1 in second row */
  .stats-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
      "stat1 stat2"
      "stat3 stat3";
    gap: 1rem;
  }
  
  .stat-item:nth-child(1) {
    grid-area: stat1;
  }
  
  .stat-item:nth-child(2) {
    grid-area: stat2;
  }
  
  .stat-item:nth-child(3) {
    grid-area: stat3;
  }
  
  /* Keep info cards 2 per row */
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .feature-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .feature-description {
    text-align: center;
  }
}

@media (max-width: 600px) {
  .content-wrapper {
    padding: 1rem;
  }
  
  .hero-section {
    margin-bottom: 4rem;
  }
  
  .section-title::after {
    width: 40px;
  }
  
  .stat-item, .info-card, .feature {
    padding: 1.25rem;
  }
  
  .info-card {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .main-container {
    padding-top: 70px;
  }
  
  .stat-item {
    padding: 1rem;
  }
  
  .stat-number {
    font-size: 1.6rem;
    margin-bottom: 0.25rem;
  }
  
  .stat-label {
    font-size: 0.8rem;
  }
  
  .info-card {
    gap: 0.5rem;
  }
  
  .card-icon {
    font-size: 1.5rem;
  }
  
  .card-title {
    font-size: 0.9rem;
  }
  
  .feature {
    padding: 1.5rem;
  }
  
  .section-title {
    width: 100%;
    max-width: 90vw;
  }
  
  .modern-icon svg {
    width: 30px;
    height: 30px;
  }
}

/* Touch device optimizations */
@media (hover: none) {
  .feature:hover,
  .stat-item:hover,
  .info-card:hover,
  .action-button:hover {
    transform: none;
  }
}
</style>