<template>
  <section class="hero">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <!-- Main Content -->
    <div class="content-container">
      <div class="hero-content" v-motion 
           :initial="{ opacity: 0, y: 100 }" 
           :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 50, damping: 15 } }">
        
        <div class="badge-container">
          <div class="badge" v-motion 
               :initial="{ scale: 0, opacity: 0 }" 
               :enter="{ scale: 1, opacity: 1, transition: { delay: 300 } }">
            <span class="badge-icon">🚀</span>
            <span>Elevate Your Learning</span>
          </div>
        </div>

        <h1 class="title">
          Step into the Future with
          <div class="gradient-text-wrapper">
            <span class="gradient-text">Limitless Possibilities</span>
          </div>
        </h1>

        <p class="description">
          Unlock the full potential of your skills with interactive courses, 
          AI-driven insights, and personalized guidance tailored to your unique learning journey.
        </p>

        <div class="cta-group">
          <button class="primary-btn" @click="$router.push('/Login')">
            <span class="btn-icon">✨</span>
            <span>Get Started</span>
          </button>
          
          <button class="secondary-btn" @click="$router.push('/courses')">
            <span>Explore Courses</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </button>
        </div>
        
        <div class="stats-container">
          <div class="stat-item" v-for="(stat, index) in stats" :key="index" 
               v-motion :initial="{ opacity: 0, y: 20 }" 
               :enter="{ opacity: 1, y: 0, transition: { delay: 300 + (index * 100) } }">
            <h3 class="stat-value">{{ stat.value }}</h3>
            <p class="stat-label">{{ stat.label }}</p>
          </div>
        </div>
      </div>

      <!-- Feature Cards -->
      <div class="features-section">
        <h2 class="features-title">Why Choose Our Platform</h2>
        
        <div class="features-grid">
          <div v-for="(feature, index) in features" 
               :key="feature.title"
               class="feature-card"
               v-motion
               :initial="{ opacity: 0, y: 50 }"
               :enter="{ opacity: 1, y: 0, transition: { delay: index * 150 } }">
            <div class="feature-icon-container" :style="{ background: feature.bgColor }">
              <div class="feature-icon">{{ feature.icon }}</div>
            </div>
            <div class="feature-content">
              <h3 class="feature-title">{{ feature.title }}</h3>
              <p class="feature-description">{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <AboutUsComponent/>
  <!-- <FeaturedClasses/> -->
  <ScrollingSection/>
</template>

<script setup>
// import FeaturedClasses from '@/components/FeaturedClasses.vue';
import AboutUsComponent from '@/components/HomePageComponents/AboutUsComponent.vue';
import ScrollingSection from '@/components/HomePageComponents/ScrollingSection.vue';

const stats = [
  { value: '50K+', label: 'Active Learners' },
  { value: '200+', label: 'Expert Courses' },
  { value: '95%', label: 'Success Rate' }
];

const features = [
  {
    icon: '🎯',
    title: 'AI-Powered Learning',
    description: 'Our smart technology analyzes your progress and learning style to deliver personalized content that adapts to your needs.',
    bgColor: 'linear-gradient(135deg, #8B5CF6, #C084FC)'
  },
  {
    icon: '⚡',
    title: 'Ultra Fast Performance',
    description: 'Enjoy seamless access to all courses, tools, and insights with our high-performance platform optimized for any device.',
    bgColor: 'linear-gradient(135deg, #6366F1, #A5B4FC)'
  },
  {
    icon: '🌎',
    title: 'Global Community',
    description: 'Connect with passionate learners and industry experts worldwide, collaborate on projects, and expand your professional network.',
    bgColor: 'linear-gradient(135deg, #8B5CF6, #A78BFA)'
  },
  {
    icon: '🔍',
    title: 'Comprehensive Resources',
    description: 'Access a vast library of cutting-edge learning materials, case studies, and practical exercises to master any skill.',
    bgColor: 'linear-gradient(135deg, #7C3AED, #C084FC)'
  }
]
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

/* Base Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hero {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f3ff, #ede9fe);
  position: relative;
  overflow: hidden;
  padding: 4rem 2rem;
  color: #1e293b;
  font-family: 'Outfit', sans-serif;
  letter-spacing: -0.02em;
}

/* Animated Background */
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
  background: linear-gradient(45deg, rgba(139, 92, 246, 0.1), rgba(192, 132, 252, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
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

/* Main Content */
.content-container {
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 6rem;
}

.hero-content {
  max-width: 750px;
  margin: 0 auto;
  text-align: center;
  padding-top: 2rem;
}

.badge-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.badge {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: rgba(139, 92, 246, 0.15);
  border-radius: 100px;
  backdrop-filter: blur(10px);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  border: 1px solid rgba(139, 92, 246, 0.3);
  box-shadow: 0 2px 10px rgba(139, 92, 246, 0.2);
  gap: 0.5rem;
  color: #4c1d95;
}

.badge-icon {
  font-size: 1.25rem;
}

.title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 4.5rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.75rem;
  letter-spacing: -0.03em;
  color: #1e293b;
}

.gradient-text-wrapper {
  display: inline-block;
  position: relative;
}

.gradient-text {
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
  position: relative;
}

.gradient-text::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  border-radius: 4px;
}

.description {
  font-size: 1.25rem;
  font-weight: 400;
  color: #475569;
  margin-bottom: 2.5rem;
  line-height: 1.7;
  letter-spacing: -0.01em;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.cta-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 3rem;
}

.primary-btn {
  padding: 1.25rem 2.5rem;
  border-radius: 100px;
  font-weight: 600;
  font-size: 1.125rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s ease;
  background: linear-gradient(45deg, #7C3AED, #A855F7);
  color: white;
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
  letter-spacing: 0;
  border: none;
  cursor: pointer;
}

.primary-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4);
}

.btn-icon {
  font-size: 1.25rem;
}

.secondary-btn {
  padding: 1.25rem 2.5rem;
  border-radius: 100px;
  font-weight: 600;
  font-size: 1.125rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(139, 92, 246, 0.3);
  color: #6d28d9;
  box-shadow: 0 4px 15px rgba(139, 92, 246, 0.1);
  cursor: pointer;
}

.secondary-btn:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(139, 92, 246, 0.2);
}

/* Stats Section */
.stats-container {
  display: flex;
  justify-content: center;
  gap: 3.5rem;
  margin-top: 2rem;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stat-label {
  font-size: 1rem;
  color: #475569;
  font-weight: 500;
}

/* Features Section */
.features-section {
  width: 100%;
}

.features-title {
  text-align: center;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  letter-spacing: -0.02em;
  color: #1e293b;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.features-title::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  border-radius: 4px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 2.5rem;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(139, 92, 246, 0.1);
  height: 100%;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 14px 40px rgba(139, 92, 246, 0.12);
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.feature-icon-container {
  width: 70px;
  height: 70px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 8px 20px rgba(139, 92, 246, 0.15);
}

.feature-card:hover .feature-icon-container {
  transform: scale(1.1) rotate(5deg);
}

.feature-icon {
  font-size: 1.75rem;
}

.feature-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.feature-title {
  font-family: 'Space Grotesk', sans-serif;
  margin-bottom: 1rem;
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #1e293b;
}

.feature-description {
  font-size: 1.125rem;
  color: #475569;
  line-height: 1.6;
  font-weight: 400;
  flex: 1;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 3rem 1.5rem;
  }

  .title {
    font-size: 3.25rem;
  }

  .description {
    font-size: 1.125rem;
  }

  .cta-group {
    flex-direction: column;
    width: 100%;
    max-width: 320px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .primary-btn, .secondary-btn {
    width: 100%;
    justify-content: center;
  }

  .stats-container {
    flex-direction: column;
    gap: 1.5rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .hero {
    padding: 2rem 1rem;
  }

  .title {
    font-size: 2.75rem;
  }

  .badge {
    font-size: 0.875rem;
  }

  .feature-card {
    padding: 1.75rem;
  }
  
  .feature-title {
    font-size: 1.25rem;
  }

  .feature-description {
    font-size: 1rem;
  }
}
</style>