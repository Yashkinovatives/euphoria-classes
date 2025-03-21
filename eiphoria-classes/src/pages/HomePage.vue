<template>
  <section class="hero">
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <div class="content-container">
      <div class="hero-content" v-motion
        :initial="{ opacity: 0, y: 100 }"
        :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 50, damping: 15 } }">

        <div class="badge-container">
          <div class="badge" v-motion
            :initial="{ scale: 0, opacity: 0 }"
            :enter="{ scale: 1, opacity: 1, transition: { delay: 300 } }">
            <span class="badge-icon">🎓</span>
            <span>Euphoria Tutorials</span>
          </div>
        </div>

        <h1 class="title">
          Helping Children
          <div class="gradient-text-wrapper">
            <span class="gradient-text">Discover Their Potential</span>
          </div>
        </h1>

        <p class="description">
          Stay connected with your child's educational journey through our interactive platform. 
          Monitor progress, view assignments, and celebrate achievements all in one place.
        </p>

        <div class="cta-group">
          <button class="primary-btn" @click="$router.push('/Login')">
            <span class="btn-icon">✨</span>
            <span>Parent Login</span>
          </button>

          <button class="secondary-btn" @click="$router.push('/About')">
            <span>About Classes</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14M12 5l7 7-7 7" />
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

      <div class="features-section">
        <h2 class="features-title">Why Parents Choose Us</h2>

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
  <AboutUsComponent />
  <ScrollingSection />
</template>

<script setup>
// import FeaturedClasses from '@/components/FeaturedClasses.vue';
import AboutUsComponent from '@/components/HomePageComponents/AboutUsComponent.vue';
import ScrollingSection from '@/components/HomePageComponents/ScrollingSection.vue';

// Uncomment this section to properly define stats
const stats = [
  { value: '500+', label: 'Happy Students' },
  { value: '15+', label: 'Years of Excellence' },
  { value: '98%', label: 'Parent Satisfaction' }
];

const features = [
  {
    icon: '📚',
    title: 'Engaging Curriculum',
    description: 'Our curriculum balances fun and learning, designed to keep children motivated while building essential skills for their future.',
    bgColor: 'linear-gradient(135deg, #4B96F3, #3178E6)' // Blue gradient for learning
  },
  {
    icon: '📱',
    title: 'Real-time Progress Updates',
    description: 'Get instant notifications about assignments, grades, and milestones so you\'re always informed about your child\'s progress.',
    bgColor: 'linear-gradient(135deg, #A076F9, #7C4AE0)' // Purple gradient for technology
  },
  {
    icon: '👨‍👩‍👧‍👦',
    title: 'Parent-Teacher Partnership',
    description: 'Schedule meetings, exchange messages, and collaborate with teachers to create the best learning environment for your child.',
    bgColor: 'linear-gradient(135deg, #FF9671, #F46036)' // Orange gradient for community
  },
  {
    icon: '🔍',
    title: 'Personalized Learning Path',
    description: 'Every child learns differently. Our adaptive system tailors resources and activities to match your child\'s unique learning style.',
    bgColor: 'linear-gradient(135deg, #57C89F, #38B2AC)' // Teal gradient for personalization
  }
]
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

/* Base Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hero {
  min-height: 100vh;
  background: linear-gradient(135deg, #F0F7FF, #E6F2FF); /* Soft blue background */
  position: relative;
  overflow: hidden;
  padding: 4rem 1rem; /* Reduced side padding for mobile */
  color: #2D3748; /* Dark blue-gray text for readability */
  font-family: 'Nunito', sans-serif;
  letter-spacing: -0.01em;
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
  background: linear-gradient(45deg, rgba(75, 150, 243, 0.1), rgba(49, 120, 230, 0.1)); /* Blue floating elements */
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.floating-element:nth-child(1) { width: 20%; height: 20vw; top: 5%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { width: 15%; height: 15vw; top: 65%; left: 85%; animation-delay: -4s; }
.floating-element:nth-child(3) { width: 25%; height: 25vw; top: 35%; left: 55%; animation-delay: -8s; }
.floating-element:nth-child(4) { width: 10%; height: 10vw; top: 75%; left: 15%; animation-delay: -12s; }
.floating-element:nth-child(5) { width: 18%; height: 18vw; top: 20%; left: 75%; animation-delay: -16s; }
.floating-element:nth-child(6) { width: 12%; height: 12vw; top: 80%; left: 45%; animation-delay: -5s; }
.floating-element:nth-child(7) { width: 14%; height: 14vw; top: 15%; left: 35%; animation-delay: -9s; }
.floating-element:nth-child(8) { width: 20%; height: 20vw; top: 60%; left: 70%; animation-delay: -13s; }

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(3deg); }
  100% { transform: translateY(-40px) rotate(-3deg); }
}

/* Main Content */
.content-container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 4rem; /* Reduced gap for mobile */
  padding: 0 1rem; /* Added padding for all screen sizes */
}

.hero-content {
  width: 100%;
  max-width: 750px;
  margin: 0 auto;
  text-align: center;
  padding-top: 1rem; /* Reduced top padding for mobile */
}

.badge-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1.25rem; /* Slightly reduced margin for mobile */
}

.badge {
  display: flex;
  align-items: center;
  padding: 0.6rem 1rem; /* Slightly smaller padding for mobile */
  background: rgba(75, 150, 243, 0.15);
  border-radius: 100px;
  backdrop-filter: blur(10px);
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(0.8rem, 2.5vw, 1rem); /* Responsive font size */
  font-weight: 600;
  letter-spacing: 0.02em;
  border: 1px solid rgba(75, 150, 243, 0.3);
  box-shadow: 0 2px 10px rgba(75, 150, 243, 0.2);
  gap: 0.5rem;
  color: #3178E6; 
  width: fit-content; /* Ensure the badge only takes the space it needs */
}

.badge-icon {
  font-size: clamp(1rem, 3vw, 1.25rem); /* Responsive icon size */
}

.title {
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(2rem, 6vw, 4.5rem); /* Responsive font size */
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem; /* Reduced margin for mobile */
  letter-spacing: -0.02em;
  color: #2D3748;
}

.gradient-text-wrapper {
  display: inline-block;
  position: relative;
}

.gradient-text {
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue gradient text */
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
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue gradient underline */
  border-radius: 4px;
}

.description {
  font-size: clamp(1rem, 3vw, 1.25rem); /* Responsive font size */
  font-weight: 400;
  color: #4A5568; /* Medium gray description */
  margin-bottom: 2rem; /* Reduced margin for mobile */
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
  margin-bottom: 2.5rem; /* Reduced margin for mobile */
  flex-wrap: wrap; /* Allow buttons to wrap on very small screens */
}

.primary-btn, .secondary-btn {
  padding: clamp(0.8rem, 2.5vw, 1.25rem) clamp(1.5rem, 5vw, 2.5rem); /* Responsive padding */
  border-radius: 100px;
  font-weight: 600;
  font-size: clamp(0.9rem, 2.5vw, 1.125rem); /* Responsive font size */
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s ease;
  letter-spacing: 0;
  border: none;
  cursor: pointer;
  min-width: 140px; /* Minimum width for buttons */
  justify-content: center; /* Center content on mobile */
  font-family: 'Quicksand', sans-serif;
}

.primary-btn {
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue primary button */
  color: white; /* White text */
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.3);
}

.primary-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(75, 150, 243, 0.4);
}

.btn-icon {
  font-size: clamp(1rem, 3vw, 1.25rem); /* Responsive icon size */
}

.secondary-btn {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(75, 150, 243, 0.3);
  color: #3178E6; /* Blue for secondary */
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.1);
}

.secondary-btn:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(75, 150, 243, 0.2);
}

/* Stats Section */
.stats-container {
  display: flex;
  justify-content: center;
  gap: clamp(1.5rem, 5vw, 3.5rem); /* Responsive gap */
  margin-top: 2rem;
  flex-wrap: wrap; /* Allow stats to wrap on mobile */
}

.stat-item {
  text-align: center;
  min-width: 120px; /* Minimum width for stat items */
  margin-bottom: 1rem; /* Add bottom margin for when they wrap */
}

.stat-value {
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(1.8rem, 5vw, 2.5rem); /* Responsive font size */
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(45deg, #4B96F3, #3178E6); 
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stat-label {
  font-size: clamp(0.8rem, 2.5vw, 1rem); /* Responsive font size */
  color: #4A5568;
  font-weight: 500;
}

/* Features Section */
.features-section {
  width: 100%;
  padding: 0 0.5rem; /* Add slight padding */
}

.features-title {
  text-align: center;
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(1.8rem, 5vw, 2.5rem); /* Responsive font size */
  font-weight: 700;
  margin-bottom: 3rem;
  letter-spacing: -0.02em;
  color: #2D3748;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
  width: 100%; /* Ensure full width for text centering */
  max-width: 90vw; /* Limit width on larger screens */
}

.features-title::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: clamp(50px, 15vw, 80px); /* Responsive width */
  height: 4px;
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue gradient feature title underline */
  border-radius: 4px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Smaller minimum width */
  gap: 1.5rem; /* Reduced gap for mobile */
  width: 100%;
}

.feature-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: clamp(1.5rem, 5vw, 2.5rem); /* Responsive padding */
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(75, 150, 243, 0.1); /* Blue border */
  height: 100%;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 14px 40px rgba(75, 150, 243, 0.12);
  border: 1px solid rgba(75, 150, 243, 0.2); /* Slightly darker blue border */
}

.feature-icon-container {
  width: clamp(50px, 12vw, 70px); /* Responsive size */
  height: clamp(50px, 12vw, 70px); /* Responsive size */
  border-radius: 16px; /* Slightly smaller radius for mobile */
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem; /* Reduced margin for mobile */
  transition: all 0.3s ease;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  color: white;
}

.feature-card:hover .feature-icon-container {
  transform: scale(1.1) rotate(5deg);
}

.feature-icon {
  font-size: clamp(1.3rem, 4vw, 1.75rem); /* Responsive font size */
}

.feature-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.feature-title {
  font-family: 'Quicksand', sans-serif;
  margin-bottom: 0.75rem; /* Reduced margin for mobile */
  font-size: clamp(1.2rem, 3.5vw, 1.5rem); /* Responsive font size */
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #2D3748;
}

.feature-description {
  font-size: clamp(0.9rem, 3vw, 1.125rem); /* Responsive font size */
  color: #4A5568;
  line-height: 1.6;
  font-weight: 400;
  flex: 1;
}

/* Media Queries - I've adjusted the existing ones and added some new breakpoints */
@media (max-width: 1200px) {
  .content-container {
    gap: 4rem;
  }
}

/* Tablet and smaller desktop screens */
@media (max-width: 1024px) {
  .hero {
    padding: 3rem 1rem;
  }
  
  .content-container {
    gap: 3.5rem;
  }
  
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Tablet portrait and large mobile */
@media (max-width: 768px) {
  .hero {
    padding: 2.5rem 1rem;
  }

  .content-container {
    gap: 3rem;
  }

  .title {
    margin-bottom: 1.25rem;
  }

  .description {
    margin-bottom: 1.75rem;
  }

  .cta-group {
    flex-direction: column;
    width: 100%;
    max-width: 280px;
    margin-left: auto;
    margin-right: auto;
    gap: 0.75rem;
  }

  .primary-btn, .secondary-btn {
    width: 100%;
    justify-content: center;
  }

  .stats-container {
    flex-direction: column;
    gap: 1.25rem;
  }

  .stat-item {
    margin-bottom: 0;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}

/* Small mobile devices */
@media (max-width: 480px) {
  .hero {
    padding: 2rem 0.75rem;
  }

  .content-container {
    gap: 2.5rem;
    padding: 0 0.5rem;
  }

  .hero-content {
    padding-top: 0.5rem;
  }

  .badge {
    padding: 0.5rem 0.875rem;
  }

  .feature-card {
    padding: 1.5rem;
    border-radius: 20px;
  }

  .feature-icon-container {
    margin-bottom: 1rem;
    border-radius: 12px;
  }

  .feature-title {
    margin-bottom: 0.5rem;
  }
}

/* Very small mobile devices */
@media (max-width: 360px) {
  .hero {
    padding: 1.5rem 0.5rem;
  }
  
  .content-container {
    gap: 2rem;
  }
  
  .badge-container {
    margin-bottom: 1rem;
  }
  
  .title {
    margin-bottom: 1rem;
  }
  
  .description {
    margin-bottom: 1.5rem;
  }
  
  .cta-group {
    margin-bottom: 2rem;
  }
  
  .features-title {
    margin-bottom: 2rem;
  }
}
</style>