<template>
  <section class="about-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>
    
    <div class="container">
      <div class="about-content">
        <h2 class="section-heading" v-motion 
            :initial="{ opacity: 0, y: 30 }" 
            :enter="{ opacity: 1, y: 0, transition: { duration: 800 } }">
          About <span class="gradient-text">Our Class</span>
        </h2>
        
        <div class="about-grid">
          <div class="about-image" v-motion 
               :initial="{ opacity: 0, scale: 0.9 }" 
               :enter="{ opacity: 1, scale: 1, transition: { duration: 800, delay: 200 } }">
              <img :src="image" alt="About our school" />
            <div class="image-accent" v-motion 
                 :initial="{ opacity: 0, x: 30, y: 30 }" 
                 :enter="{ opacity: 1, x: 0, y: 0, transition: { duration: 1000, delay: 400 } }"></div>
          </div>
          
          <div class="about-text">
            <p v-motion 
               :initial="{ opacity: 0, x: 40 }" 
               :enter="{ opacity: 1, x: 0, transition: { duration: 800, delay: 300 } }">
              We believe every child deserves a nurturing educational environment that fosters growth, creativity, and academic excellence. Our dedicated teachers create personalized learning experiences that help students discover their unique potential and develop confidence for future success.
            </p>
            
            <div class="key-features">
              <div class="feature" v-for="(feature, index) in features" :key="feature" v-motion 
                   :initial="{ opacity: 0, x: 30 }" 
                   :enter="{ opacity: 1, x: 0, transition: { duration: 600, delay: 400 + (index * 150) } }">
                <div class="feature-icon">✓</div>
                <div>{{ feature }}</div>
              </div>
            </div>
            
            <button @click="$router.push('/about')" class="learn-more-btn" v-motion 
                    :initial="{ opacity: 0, y: 20 }" 
                    :enter="{ opacity: 1, y: 0, transition: { duration: 600, delay: 800 } }">
              Learn More
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import image from '@/assets/images/avatar2.jpg'
const features = [
  "Personal Attention on each Student",
  "Career Guidance",
  "Limited seats per Batch",
  "Timely Feedback"
];
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.about-section {
  padding: 5rem 0;
  background-color: #fafaea;
  position: relative;
  overflow: hidden;
  color: #333;
  font-family: 'Inter', sans-serif;
}

/* Background circles with improved styling */
.about-section::before {
  content: '';
  position: absolute;
  top: -250px;
  right: -250px;
  width: 500px;
  height: 500px;
  background-color: rgba(255, 235, 59, 0.1);
  border-radius: 50%;
  z-index: 1;
}

/* Bottom right circle with border */
.about-section::after {
  content: '';
  position: absolute;
  bottom: -300px;
  right: -300px;
  width: 600px;
  height: 600px;
  border: 2px solid rgba(255, 235, 59, 0.2);
  border-radius: 50%;
  z-index: 1;
  opacity: 0.5;
}

.section-heading {
  font-family: 'Inter', sans-serif;
  font-size: 2.5rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 3rem;
  color: #333;
  position: relative;
}

.gradient-text {
  color: #ffeb3b;
  position: relative;
  font-weight: 800;
  background: none;
  -webkit-background-clip: initial;
  -webkit-text-fill-color: initial;
}

.gradient-text::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 3px;
  background-color: #ffeb3b;
  bottom: -5px;
  left: 0;
}

.about-image {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(255, 235, 59, 0.15);
  max-width: 90%;
  margin: 0 auto;
}

.image-accent {
  position: absolute;
  bottom: -15px;
  right: -15px;
  width: 100px;
  height: 100px;
  background: #ffeb3b;
  border-radius: 16px;
  z-index: -1;
  opacity: 0.8;
}

.feature-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  background: #ffeb3b;
  border-radius: 50%;
  color: #333;
  font-size: 0.875rem;
  box-shadow: 0 4px 8px rgba(255, 235, 59, 0.2);
  transition: all 0.3s ease;
}

.learn-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: #ffeb3b;
  color: #333;
  border-radius: 100px;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  transition: all 0.3s ease;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(255, 235, 59, 0.2);
  margin-top: 0.5rem;
  align-self: flex-start;
  position: relative;
  overflow: hidden;
  font-family: 'Inter', sans-serif;
}

.gradient-text {
  background: linear-gradient(45deg, #000000, #050a11); /* Blue gradient text */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.about-image {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(75, 150, 243, 0.15);
  max-width: 90%;
  margin: 0 auto;
}

.about-image img {
  width: 100%;
  max-height: 400px; /* Limit the image height */
  object-fit: cover;
  object-position: center;
  display: block;
  border-radius: 16px;
  transition: transform 0.6s ease-out;
}

.about-image:hover img {
  transform: scale(1.03);
}

.image-accent {
  position: absolute;
  bottom: -15px;
  right: -15px;
  width: 100px;
  height: 100px;
  background: linear-gradient(45deg, #d3f303, #d4ff00); /* Blue gradient accent */
  border-radius: 16px;
  z-index: -1;
  opacity: 0.8;
}

.about-text {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.about-text p {
  font-size: 1.125rem;
  line-height: 1.7;
  color: #4A5568;
}

.key-features {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.05rem;
  color: #2D3748;
  font-weight: 500;
  transition: transform 0.3s ease;
}

.feature:hover {
  transform: translateX(5px);
}

.feature-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue gradient icon */
  border-radius: 50%;
  color: white;
  font-size: 0.875rem;
  box-shadow: 0 4px 8px rgba(75, 150, 243, 0.2);
  transition: all 0.3s ease;
}

.feature:hover .feature-icon {
  transform: scale(1.1);
  box-shadow: 0 6px 12px rgba(75, 150, 243, 0.3);
}

.learn-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: linear-gradient(45deg, #4B96F3, #3178E6); /* Blue gradient button */
  color: white;
  border-radius: 100px;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  transition: all 0.3s ease;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(75, 150, 243, 0.2);
  margin-top: 0.5rem;
  align-self: flex-start;
  position: relative;
  overflow: hidden;
  font-family: 'Quicksand', sans-serif;
}

.learn-more-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.2);
  transform: skewX(-30deg);
  transition: all 0.5s ease;
}

.learn-more-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(75, 150, 243, 0.3);
}

.learn-more-btn:hover::before {
  left: 100%;
}

.learn-more-btn svg {
  transition: transform 0.3s ease;
}

.learn-more-btn:hover svg {
  transform: translateX(3px);
}

@media (max-width: 1024px) {
  .about-section {
    padding: 4.5rem 0;
  }
  
  .section-heading {
    font-size: 2.25rem;
  }
}

@media (max-width: 768px) {
  .about-section {
    padding: 4rem 0;
  }
  
  .about-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .section-heading {
    font-size: 2rem;
  }
  
  .about-text p {
    font-size: 1rem;
  }
  
  .feature {
    font-size: 1rem;
  }
  
  .container {
    padding: 0 1.5rem;
  }
  
  .image-accent {
    width: 80px;
    height: 80px;
  }
}

@media (max-width: 480px) {
  .about-section {
    padding: 3rem 0;
  }
  
  .section-heading {
    font-size: 1.75rem;
  }
  
  .about-text p {
    font-size: 0.95rem;
  }
  
  .feature {
    font-size: 0.95rem;
  }
  
  .learn-more-btn {
    padding: 0.7rem 1.2rem;
    font-size: 0.95rem;
  }
  
  .image-accent {
    width: 60px;
    height: 60px;
    bottom: -10px;
    right: -10px;
  }
  
  .container {
    padding: 0 1.25rem;
  }
}

@media (max-width: 360px) {
  .about-section {
    padding: 2.5rem 0;
  }
  
  .section-heading {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .key-features {
    gap: 0.5rem;
  }
  
  .feature-icon {
    width: 24px;
    height: 24px;
  }
}
</style>