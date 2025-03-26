<template>
  <section class="testimonials-section">
    <div class="container">
      <h2 class="section-heading">
        What Our Parents Say
        <span class="heading-accent"></span>
      </h2>
      
      <div v-if="loading" class="loading-state">
        <div class="loading-spinner"></div>
      </div>
      
      <div v-else class="testimonial-slider" @touchstart="touchStart" @touchmove="touchMove" @touchend="touchEnd">
        <div class="testimonial-track" ref="trackRef">
          <div 
            v-for="(testimonial, index) in testimonials" 
            :key="index"
            class="testimonial-card"
            :class="{ active: currentIndex === index }"
          >
            <div class="quote-icon">❝</div>
            <p class="testimonial-text">{{ testimonial.review }}</p>
            <div class="author-info">
              <div class="author-name">{{ testimonial.name }}</div>
              <div class="author-role">{{ testimonial.role || "Parent" }}</div>
            </div>
          </div>
        </div>
        
        <div class="slider-controls" v-if="testimonials.length > 1">
          <div class="dots">
            <button 
              v-for="(_, index) in testimonials" 
              :key="index"
              class="dot"
              :class="{ active: currentIndex === index }"
              @click="currentIndex = index"
            ></button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.testimonials-section {
  background-color: #fafaea;
  padding: 80px 0;
  position: relative;
  overflow: hidden;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-heading {
  font-size: 2.5rem;
  font-weight: 800;
  color: #222;
  text-align: center;
  margin-bottom: 60px;
  position: relative;
}

.heading-accent {
  display: block;
  width: 80px;
  height: 4px;
  background: #ffeb3b;
  margin: 20px auto 0;
  border-radius: 2px;
}

.testimonial-slider {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.testimonial-track {
  position: relative;
  min-height: 300px;
}

.testimonial-card {
  position: absolute;
  width: 100%;
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  opacity: 0;
  transform: translateX(100px);
  transition: all 0.5s ease;
}

.testimonial-card.active {
  opacity: 1;
  transform: translateX(0);
}

.quote-icon {
  font-size: 4rem;
  color: #ffeb3b;
  line-height: 1;
  margin-bottom: 20px;
}

.testimonial-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #444;
  margin-bottom: 30px;
  font-style: italic;
}

.author-info {
  border-top: 2px solid #f0f0f0;
  padding-top: 20px;
}

.author-name {
  font-size: 1.2rem;
  font-weight: 700;
  color: #222;
  margin-bottom: 5px;
}

.author-role {
  font-size: 0.9rem;
  color: #666;
}

.slider-controls {
  margin-top: 40px;
}

.dots {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #ddd;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: #ffeb3b;
  transform: scale(1.2);
}

@media (max-width: 768px) {
  .testimonials-section {
    padding: 40px 0;
  }

  .section-heading {
    font-size: 1.8rem;
    margin-bottom: 30px;
  }

  .testimonial-card {
    padding: 25px;
  }

  .testimonial-track {
    min-height: 380px;
  }

  .testimonial-text {
    font-size: 0.95rem;
    line-height: 1.7;
  }
}

@media (max-width: 480px) {
  .testimonials-section {
    padding: 30px 0;
  }

  .container {
    padding: 0 15px;
  }

  .section-heading {
    font-size: 1.5rem;
  }

  .testimonial-track {
    min-height: 420px;
  }

  .testimonial-card {
    padding: 20px;
  }

  .quote-icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
  }

  .testimonial-text {
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 20px;
  }

  .author-info {
    padding-top: 15px;
  }

  .author-name {
    font-size: 1rem;
  }

  .author-role {
    font-size: 0.8rem;
  }

  .slider-controls {
    margin-top: 25px;
  }

  .dot {
    width: 8px;
    height: 8px;
  }
}

@media (max-width: 360px) {
  .testimonial-track {
    min-height: 460px;
  }

  .testimonial-card {
    padding: 15px;
  }
}
</style>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from 'axios';

// Initialize testimonials as an empty array
const testimonials = ref([]);
const loading = ref(true);
const currentIndex = ref(0);
const autoplayInterval = ref(null);
const trackRef = ref(null);

// Touch handling
const touchStartX = ref(0);
const touchEndX = ref(0);

const touchStart = (e) => {
  touchStartX.value = e.changedTouches[0].screenX;
};

const touchMove = (e) => {
  touchEndX.value = e.changedTouches[0].screenX;
};

const touchEnd = () => {
  const minSwipeDistance = 50;
  const distance = touchEndX.value - touchStartX.value;
  
  if (Math.abs(distance) > minSwipeDistance) {
    if (distance > 0) {
      prevTestimonial();
    } else {
      nextTestimonial();
    }
  }
};

// Fetch testimonials
const fetchTestimonials = async () => {
  loading.value = true;
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/reviews/');
    testimonials.value = response.data.slice(0, 6);
    
    if (testimonials.value.length > 1) {
      startAutoplay();
    }
  } catch (error) {
    console.error('Error fetching testimonials:', error);
    testimonials.value = [
      {
        name: "Sarah Johnson",
        role: "Parent",
        review: "The teachers are exceptional and truly care about each student's progress. My daughter has shown remarkable improvement in her confidence and academic skills.",
      },
      {
        name: "Michael Roberts",
        role: "Parent",
        review: "The personalized attention my son receives has made all the difference. The regular progress updates keep us informed, and we're very happy with the results.",
      },
      {
        name: "Jennifer Williams",
        role: "Parent",
        review: "We've tried several educational programs, but this one stands out for its quality curriculum and dedicated staff. Highly recommended for any parent looking for quality education.",
      }
    ];
    startAutoplay();
  } finally {
    loading.value = false;
  }
};

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

const startAutoplay = () => {
  if (testimonials.value.length > 1) {
    autoplayInterval.value = setInterval(nextTestimonial, 5000);
  }
};

const resetAutoplay = () => {
  clearInterval(autoplayInterval.value);
  startAutoplay();
};

onMounted(() => {
  fetchTestimonials();
});

onBeforeUnmount(() => {
  clearInterval(autoplayInterval.value);
});
</script>