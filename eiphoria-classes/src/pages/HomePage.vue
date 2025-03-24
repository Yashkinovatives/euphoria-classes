<template>
  <div class="main-container">
    <!-- Background circles with stronger visibility -->
    <div class="bg-circle" style="position: absolute; width: 500px; height: 500px; border-radius: 50%; background-color: rgba(255, 235, 59, 0.2); top: -100px; right: -100px;"></div>
    <div class="bg-circle" style="position: absolute; width: 600px; height: 600px; border-radius: 50%; background-color: rgba(255, 235, 59, 0.15); bottom: -150px; right: -150px;"></div>
    
    <!-- Background dots -->
    <div class="background-dots">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    
    <div class="content-wrapper">
      <!-- Header section with logo -->
      <header class="header">
        <div class="logo">
          <span class="logo-dot"></span> Euphoria Tutorials
        </div>
      </header>
      
      <!-- Main content pushed down to account for navbar -->
      <div class="hero-section">
        <div class="left-column">
          <h1 class="main-heading">
            <span class="line">Helping Children</span>
            <span class="line"><span class="discover-text">Discover</span> Their</span>
            <span class="line">Potential</span>
          </h1>
          
          <p class="subtitle">
            Stay connected with your child's educational journey through our interactive platform. 
            Monitor progress, view assignments, and celebrate achievements all in one place.
          </p>
          
          <div class="action-buttons">
            <button class="action-button primary">Parent Login <span class="arrow">→</span></button>
            <button class="action-button secondary">Learn More</button>
          </div>
        </div>
        
        <div class="right-column">
          <!-- Stats container with yellow border -->
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
        <div class="underline"></div>
        
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
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ffeb3b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                  <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>`,
    title: 'Engaging Curriculum',
    description: 'Our curriculum balances fun and learning, designed to keep children motivated while building essential skills for their future.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ffeb3b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <path d="M21 15l-5-5L5 21"></path>
                </svg>`,
    title: 'Real-time Progress Updates',
    description: 'Get instant notifications about assignments, grades, and milestones so you\'re always informed about your child\'s progress.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ffeb3b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>`,
    title: 'Parent-Teacher Partnership',
    description: 'Schedule meetings, exchange messages, and collaborate with teachers to create the best learning environment for your child.',
  },
  {
    modernIcon: `<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ffeb3b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
/* Import Google Fonts - Inter for the whole page for consistency */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-container {
  min-height: 100vh;
  background-color: #fafaea;
  color: #333;
  font-family: 'Inter', sans-serif;
  position: relative;
  overflow: hidden;
  padding-top: 100px;
}

/* Remove the previous circle styles that weren't working */

/* Header styling */
.header {
  padding: 20px;
  text-align: left;
  margin-bottom: 60px;
}

.logo {
  font-size: 1.1em;
  font-weight: 600;
  color: #333;
  background-color: #fff;
  display: inline-block;
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

/* Background dots and floating circle */
.background-dots {
  position: absolute;
  top: 280px;
  left: 50px;
  width: 200px;
  height: 100px;
  pointer-events: none;
  z-index: 1;
  opacity: 0.6;
}

.dot {
  position: absolute;
  width: 8px;
  height: 8px;
  background-color: #ffeb3b;
  border-radius: 50%;
  opacity: 0.3;
}

/* Grid pattern of dots behind "Discover" */
.dot:nth-child(1) { top: 0px; left: 0px; }
.dot:nth-child(2) { top: 0px; left: 25px; }
.dot:nth-child(3) { top: 0px; left: 50px; }
.dot:nth-child(4) { top: 25px; left: 0px; }
.dot:nth-child(5) { top: 25px; left: 25px; }
.dot:nth-child(6) { top: 25px; left: 50px; }
.dot:nth-child(7) { top: 50px; left: 0px; }
.dot:nth-child(8) { top: 50px; left: 25px; }
.dot:nth-child(9) { top: 50px; left: 50px; }

/* Removed floating-circle class as we're using ::before and ::after instead */

.content-wrapper {
  position: relative;
  z-index: 1;
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

/* Hero section */
.hero-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  margin-top: 20px;
  margin-bottom: 60px;
}

.left-column {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.main-heading {
  font-family: 'Inter', sans-serif;
  font-size: 3em;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 30px;
  color: #333;
  position: relative;
  z-index: 2;
}

.line {
  display: block;
}

/* Yellow "Discover" text with underline */
.discover-text {
  color: #ffeb3b;
  position: relative;
  font-weight: 800;
}

.discover-text::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 3px;
  background-color: #ffeb3b;
  bottom: -5px;
  left: 0;
}

.subtitle {
  font-family: 'Inter', sans-serif;
  font-size: 1.1em;
  line-height: 1.6;
  color: #666;
  margin-bottom: 30px;
  max-width: 90%;
}

.action-buttons {
  display: flex;
  gap: 15px;
}

.action-button {
  padding: 15px 30px;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
}

.action-button.primary {
  background-color: #ffeb3b;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  box-shadow: 0 4px 10px rgba(255, 235, 59, 0.3);
}

.action-button.primary:hover {
  background-color: #ffe100;
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(255, 235, 59, 0.4);
}

.action-button.secondary {
  background-color: #fff;
  color: #333;
  border: 1px solid #eee !important;
}

.arrow {
  margin-left: 10px;
}

/* Right column */
.right-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Stats container with separate boxes */
.stats-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  margin-bottom: 20px;
}

.stat-item {
  background-color: #fff;
  padding: 20px 15px;
  border-radius: 8px;
  text-align: center;
  transition: all 0.3s ease;
  border: 2px solid #ffeb3b;
  box-shadow: 0 2px 8px rgba(255, 235, 59, 0.15);
}

.stat-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(255, 235, 59, 0.25);
}

.stat-number {
  font-family: 'Inter', sans-serif;
  font-size: 2.5em;
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
  color: #333; /* Changed to black text */
}

.stat-label {
  font-family: 'Inter', sans-serif;
  font-size: 1em;
  color: #666;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.info-card {
  display: flex;
  align-items: center;
  background-color: #fff;
  border: 2px solid #ffeb3b;
  padding: 15px;
  border-radius: 10px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(255, 235, 59, 0.1);
}

.info-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(255, 235, 59, 0.15);
}

.card-icon {
  font-size: 1.8em;
  margin-right: 15px;
}

.card-title {
  font-family: 'Inter', sans-serif;
  font-size: 1.2em;
  font-weight: bold;
  color: #333;
}

/* Features section */
.features-section {
  padding: 40px 0;
}

.section-title {
  font-family: 'Inter', sans-serif;
  font-size: 2.5em;
  font-weight: 800;
  margin-bottom: 10px;
  text-align: center;
  color: #333;
  position: relative;
}

.underline {
  width: 50px;
  height: 4px;
  background-color: #ffeb3b;
  margin: 0 auto 40px auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.feature {
  background-color: #fff;
  border: 2px solid #ffeb3b;
  border-radius: 10px;
  padding: 20px;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 10px rgba(255, 235, 59, 0.1);
}

.feature:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(255, 235, 59, 0.15);
}

.feature-header {
  display: flex;
  align-items: flex-start;
  gap: 15px;
  margin-bottom: 15px;
}

.modern-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-title {
  font-family: 'Inter', sans-serif;
  font-size: 1.2em;
  font-weight: 700;
  color: #333;
}

.feature-description {
  font-family: 'Inter', sans-serif;
  color: #666;
  line-height: 1.6;
  font-size: 1em;
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

/* Media queries for responsiveness */
@media (max-width: 1200px) {
  .main-container {
    padding-top: 120px;
  }
}

@media (max-width: 1024px) {
  .hero-section {
    grid-template-columns: 1fr;
    gap: 30px;
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

@media (max-width: 768px) {
  .main-container {
    padding-top: 80px;
  }

  .stats-container {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .stat-item:last-child {
    grid-column: span 2;
  }
  
  .action-button {
    padding: 12px 24px;
  }
}

@media (max-width: 480px) {
  .main-container {
    padding-top: 70px;
  }
  
  .header {
    margin-bottom: 30px;
    text-align: center;
  }
  
  .logo {
    display: inline-block;
  }
  
  .main-heading {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  .subtitle {
    font-size: 0.95em;
    margin-bottom: 25px;
  }
  
  .action-buttons {
    flex-direction: column;
    width: 100%;
  }
  
  .action-button {
    width: 100%;
    padding: 12px 20px;
    margin-bottom: 10px;
  }
  
  .stats-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
      "stat1 stat2"
      "stat3 stat3";
    gap: 10px;
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
  
  .stat-item {
    padding: 15px;
    margin-bottom: 10px;
  }
  
  .card-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .info-card {
    padding: 12px;
  }
  
  .card-icon {
    font-size: 1.5em;
    margin-right: 10px;
  }
  
  .card-title {
    font-size: 1em;
  }
  
  .section-title {
    font-size: 2em;
  }
  
  .feature {
    padding: 15px;
  }
  
  .feature-title {
    font-size: 1.1em;
  }
  
  .feature-description {
    font-size: 0.9em;
  }
}
</style>