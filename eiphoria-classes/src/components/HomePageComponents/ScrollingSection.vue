<template>
  <section class="testimonials-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>
    
    <div class="container">
      <h2 class="section-heading">Success Stories</h2>
      
      <div v-if="loading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>Loading testimonials...</p>
      </div>
      
      <div v-else-if="testimonials.length === 0" class="empty-state">
        <p>No testimonials available yet. Be the first to share your experience!</p>
      </div>
      
      <div v-else class="testimonial-carousel">
        <div class="testimonial-track" ref="trackRef">
          <div 
            v-for="(testimonial, index) in testimonials" 
            :key="index"
            class="testimonial-card"
            :class="{ active: currentIndex === index }"
          >
            <div class="quote-mark">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M11.192 15.757c0-.88-.23-1.618-.69-2.217-.326-.412-.768-.683-1.327-.812-.55-.128-1.07-.137-1.54-.028-.16-.95.1-1.626.41-2.032.24-.317.52-.566.84-.747.167-.092.34-.16.52-.205.33-.08.7-.08 1.12 0 .5.09.86.29 1.08.6.01.03.03.05.04.08l1.46-1.8c-.51-.4-1.08-.7-1.73-.88-.65-.19-1.23-.24-1.73-.12-.5.11-.93.32-1.29.63-.35.31-.7.94-1.02 1.88-.32.95-.5 1.68-.52 2.2-.02.5.04.95.18 1.35.13.41.35.77.65 1.08.28.31.67.58 1.16.81.49.24 1.11.36 1.84.36.53 0 1.2-.27 2-.83.53-.37.97-.83 1.31-1.39.34-.56.52-1.17.54-1.8zm5.46-4.6h1.42v-1.48h-1.38v-2.37h-1.54v2.37h-1.38v1.48h1.38v2.37h1.54v-2.37z"></path>
              </svg>
            </div>
            
            <p class="testimonial-content">{{ testimonial.review }}</p>
            
            <div class="user-info">
              <div class="user-avatar-container">
                <img :src="testimonial.image || defaultAvatar" :alt="testimonial.name" class="user-avatar">
              </div>
              <div class="user-details">
                <h3 class="user-name">{{ testimonial.name }}</h3>
                <p class="user-role">{{ testimonial.role || "Learner" }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Navigation buttons below the testimonial cards -->
        <div class="controls-container" v-if="testimonials.length > 1">
          <div class="controls">
            <button @click="prevTestimonial" class="control-btn prev" aria-label="Previous testimonial">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="15 18 9 12 15 6"></polyline>
              </svg>
            </button>
            
            <div class="indicators">
              <button 
                v-for="(_, index) in testimonials" 
                :key="index"
                @click="setTestimonial(index)"
                class="indicator-dot"
                :class="{ active: currentIndex === index }"
                :aria-label="`Go to testimonial ${index + 1}`"
              ></button>
            </div>
            
            <button @click="nextTestimonial" class="control-btn next" aria-label="Next testimonial">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
          </div>
        </div>
      </div>
      
    
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from 'axios';

// State management
const testimonials = ref([]);
const loading = ref(true);
const currentIndex = ref(0);
const autoplayInterval = ref(null);
const trackRef = ref(null);
const defaultAvatar = '/default-avatar.png';

// Fetch testimonials from the database (limited to 6)
const fetchTestimonials = async () => {
  loading.value = true;
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/reviews/');
    // Limit to 6 testimonials maximum
    testimonials.value = response.data.slice(0, 6);
  } catch (error) {
    console.error('Error fetching testimonials:', error);
  } finally {
    loading.value = false;
  }
};



// Carousel navigation functions
const nextTestimonial = () => {
  if (testimonials.value.length > 0) {
    currentIndex.value = (currentIndex.value + 1) % testimonials.value.length;
    resetAutoplay();
  }
};

const prevTestimonial = () => {
  if (testimonials.value.length > 0) {
    currentIndex.value = currentIndex.value === 0 
      ? testimonials.value.length - 1 
      : currentIndex.value - 1;
    resetAutoplay();
  }
};

const setTestimonial = (index) => {
  currentIndex.value = index;
  resetAutoplay();
};

// Autoplay functions
const startAutoplay = () => {
  if (testimonials.value.length > 1) {
    autoplayInterval.value = setInterval(() => {
      nextTestimonial();
    }, 6000);
  }
};

const resetAutoplay = () => {
  clearInterval(autoplayInterval.value);
  startAutoplay();
};

// Keyboard navigation
const handleKeydown = (e) => {
  if (e.key === 'ArrowLeft') {
    prevTestimonial();
  } else if (e.key === 'ArrowRight') {
    nextTestimonial();
  }
};

// Lifecycle hooks
onMounted(() => {
  fetchTestimonials();
  window.addEventListener('keydown', handleKeydown);
});

onBeforeUnmount(() => {
  clearInterval(autoplayInterval.value);
  window.removeEventListener('keydown', handleKeydown);
});
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.testimonials-section {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f3ff, #ede9fe);
  position: relative;
  overflow: hidden;
  color: #1e293b;
  font-family: 'Outfit', sans-serif;
  min-height: 50vh;
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

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.section-heading {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 3rem;
  color: #1e293b;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.section-heading::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, #7C3AED, #C084FC);
  border-radius: 2px;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  gap: 1rem;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(139, 92, 246, 0.2);
  border-top: 4px solid #7C3AED;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Empty State */
.empty-state {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  font-size: 1.125rem;
  color: #475569;
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid rgba(139, 92, 246, 0.2);
  min-height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Testimonial Carousel */
.testimonial-carousel {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 0 4rem;
}

.controls-container {
  margin-top: 2rem;
  width: 100%;
}

.controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
}

.control-btn {
  background: white;
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(124, 58, 237, 0.15);
  color: #7C3AED;
  transition: all 0.3s ease;
}

.control-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(124, 58, 237, 0.25);
  background: #7C3AED;
  color: white;
}

.control-btn:active {
  transform: translateY(0);
}

.control-btn svg {
  width: 24px;
  height: 24px;
}

.testimonial-track {
  position: relative;
  min-height: 350px;
}

.testimonial-card {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  opacity: 0;
  transform: translateX(20px);
  transition: all 0.6s ease;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(124, 58, 237, 0.08);
  padding: 2rem;
  z-index: 1;
  pointer-events: none;
}

.testimonial-card.active {
  opacity: 1;
  transform: translateX(0);
  z-index: 2;
  pointer-events: auto;
}

.quote-mark {
  position: absolute;
  top: -25px;
  left: 25px;
  background: linear-gradient(135deg, #7C3AED, #C084FC);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 6px 15px rgba(124, 58, 237, 0.2);
}

.quote-mark svg {
  width: 24px;
  height: 24px;
}

.testimonial-content {
  font-size: 1.125rem;
  line-height: 1.8;
  color: #4b5563;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.user-info {
  display: flex;
  align-items: center;
  border-top: 1px solid #e5e7eb;
  padding-top: 1.5rem;
}

.user-avatar-container {
  position: relative;
  width: 60px;
  height: 60px;
  margin-right: 1rem;
  border-radius: 50%;
  background: linear-gradient(135deg, #7C3AED, #C084FC);
  padding: 3px;
  box-shadow: 0 4px 10px rgba(124, 58, 237, 0.2);
}

.user-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid white;
}

.user-details {
  flex: 1;
}

.user-name {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.125rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 0.25rem;
}

.user-role {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.indicators {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  align-items: center;
}

.indicator-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #e5e7eb;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0;
}

.indicator-dot.active {
  background: #7C3AED;
  transform: scale(1.2);
}



/* Responsive Design */
@media (max-width: 768px) {
  .section-heading {
    font-size: 2rem;
  }
  
  .testimonial-content {
    font-size: 1rem;
  }
  
  .control-btn {
    width: 40px;
    height: 40px;
  }
  
  .testimonial-track {
    min-height: 400px; /* Increase height for mobile */
  }
  
  .controls {
    gap: 0.75rem;
  }
  
  .container {
    padding: 0 1.5rem;
  }
  

}

@media (max-width: 480px) {
  .testimonial-track {
    min-height: 450px; /* Further increase height for small mobile */
  }
  
  .testimonial-card {
    padding: 1.5rem;
  }
  
  .quote-mark {
    width: 40px;
    height: 40px;
    top: -20px;
    left: 20px;
  }
  
  .quote-mark svg {
    width: 20px;
    height: 20px;
  }
  
  .modal-content {
    padding: 1.75rem;
  }
}
</style>