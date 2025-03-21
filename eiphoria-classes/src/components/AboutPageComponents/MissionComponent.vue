<template>
  <section class="mission-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <div class="container">
      <div class="mission-content">
        <div class="text-column">
          <div class="section-badge">Our Mission</div>
          <h2 class="section-title">Transforming Education Through <span class="gradient-text">Innovation</span></h2>
          <p class="section-text">
            At Euphoria Tutorials, we believe that education should be accessible, engaging, and effective for everyone. Our mission is to empower students to achieve their full potential through personalized education that adapts to individual learning styles.
          </p>
          <p class="section-text">
            We're committed to creating a supportive environment where students can connect with expert teachers and peers, fostering collaboration and growth in a dynamic learning atmosphere.
          </p>
          
          <div class="key-points">
            <div class="key-point">
              <div class="point-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </div>
              <span>Personalized Learning Approach</span>
            </div>
            <div class="key-point">
              <div class="point-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </div>
              <span>Expert Teaching Faculty</span>
            </div>
            <div class="key-point">
              <div class="point-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </div>
              <span>Comprehensive Support System</span>
            </div>
          </div>
        </div>
        
        <div class="image-column">
          <div class="image-wrapper">
            <img :src="Slearning" alt="Students learning" class="mission-image" />
            <div class="image-accent"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Slearning from "@/assets/images/Slearning.jpg";
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.mission-section {
  position: relative;
  background: linear-gradient(135deg, #F0F7FF, #E6F2FF);
  padding: 5rem 2rem;
  font-family: 'Nunito', sans-serif;
  color: #2D3748;
  overflow: hidden;
}

/* Animated Background */
.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.floating-element {
  position: absolute;
  background: linear-gradient(45deg, rgba(75, 150, 243, 0.1), rgba(49, 120, 230, 0.1));
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
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.mission-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.text-column {
  display: flex;
  flex-direction: column;
}

.section-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(75, 150, 243, 0.1);
  border-radius: 100px;
  color: #3178E6;
  font-weight: 600;
  font-size: 0.875rem;
  margin-bottom: 1rem;
  align-self: flex-start;
}

.section-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-text {
  font-size: 1.125rem;
  color: #4A5568;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.key-points {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.key-point {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-weight: 500;
  color: #2D3748;
  transition: transform 0.3s ease;
}

.key-point:hover {
  transform: translateX(8px);
}

.point-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  min-width: 2rem;
  background: rgba(75, 150, 243, 0.1);
  border-radius: 50%;
  color: #4B96F3;
  transition: all 0.3s ease;
}

.key-point:hover .point-icon {
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  color: white;
  transform: scale(1.1);
}

.point-icon svg {
  width: 1rem;
  height: 1rem;
}

.image-column {
  position: relative;
}

.image-wrapper {
  position: relative;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(75, 150, 243, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  max-width: 85%;
  margin: 0 auto;
}

.image-wrapper:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(75, 150, 243, 0.2);
}

.mission-image {
  width: 100%;
  height: auto;
  max-height: 350px;
  object-fit: cover;
  display: block;
  border-radius: 1rem;
  transform: scale(1.02);
  transition: transform 0.5s ease;
}

.image-wrapper:hover .mission-image {
  transform: scale(1.05);
}

.image-accent {
  position: absolute;
  bottom: -20px;
  right: -20px;
  width: 140px;
  height: 140px;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  border-radius: 1rem;
  z-index: -1;
  opacity: 0.8;
  transition: all 0.3s ease;
}

.image-wrapper:hover .image-accent {
  width: 160px;
  height: 160px;
  bottom: -25px;
  right: -25px;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .section-title {
    font-size: 2.2rem;
  }
}

@media (max-width: 768px) {
  .mission-section {
    padding: 4rem 1.5rem;
  }
  
  .mission-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  
  .image-column {
    order: -1;
  }
  
  .image-wrapper {
    max-width: 75%;
  }
  
  .mission-image {
    max-height: 300px;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .section-text {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .mission-section {
    padding: 3rem 1rem;
  }
  
  .section-title {
    font-size: 1.75rem;
  }
  
  .image-accent {
    width: 100px;
    height: 100px;
  }
  
  .image-wrapper:hover .image-accent {
    width: 120px;
    height: 120px;
  }
}
</style>