<template>
  <section class="teacher-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Meet Our <span class="gradient-text">Teacher</span></h2>
        <p class="section-subtitle">Dedicated educator committed to helping students excel</p>
      </div>
      
      <div class="teacher-profile">
        <div class="profile-image-container">
          <img :src="teacher.image" :alt="teacher.name" class="profile-image" />
          <div class="image-accent"></div>
        </div>
        
        <div class="profile-content">
          <div class="profile-header">
            <h3 class="teacher-name">{{ teacher.name }}</h3>
            <p class="teacher-credentials">{{ teacher.credentials }}</p>
          </div>
          
          <div class="profile-details">
            <p class="profile-bio" v-for="(paragraph, index) in teacher.bio" :key="index">
              {{ paragraph }}
            </p>
          </div>
          
          <div class="teacher-achievements">
            <div class="achievement" v-for="(achievement, index) in teacher.achievements" :key="index">
              <div class="achievement-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </div>
              <span>{{ achievement }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const teacher = ref({
  name: "Rohan N. Sawant",
  credentials: "M.Com, B.Ed (1st Rank)",
  image: "/api/placeholder/400/500", // Replace with actual image
  bio: [
    "Rohan N. Sawant's commitment to education is the cornerstone of Euphoria Classes. Holding an M.Com and a B.Ed where he achieved 1st rank, his qualifications are only a portion of the value he brings to his students.",
    "He has dedicated his career to creating a learning atmosphere where students are encouraged to reach their full potential. His experience is vast, and his focus is always on the individual needs of his students. He is a mentor, a guide, and a dedicated teacher."
  ],
  achievements: [
    "First rank in B.Ed program",
    "Years of teaching excellence",
    "Personalized approach to education",
    "Mentor to hundreds of successful students"
  ]
});
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

/* Update background and gradients */
.teacher-section {
  position: relative;
  background: white;  /* Changed from blue gradient to white */
  padding: 5rem 2rem;
  font-family: 'Nunito', sans-serif;
  color: #2D3748;
  overflow: hidden;
}

.floating-element {
  position: absolute;
  background: linear-gradient(45deg, rgba(255, 193, 7, 0.1), rgba(255, 213, 79, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.gradient-text {
  background: linear-gradient(45deg, #FFC107, #FFD54F);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Add grid pattern */
.teacher-section::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-image: 
    linear-gradient(rgba(255, 193, 7, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 193, 7, 0.05) 1px, transparent 1px);
  background-size: 20px 20px;
  opacity: 0.5;
  pointer-events: none;
}

/* Update accent colors */
.image-accent {
  background: linear-gradient(135deg, #FFC107, #FFD54F);
}

.teacher-credentials {
  color: #FFC107;
}

.achievement-icon {
  background: rgba(255, 193, 7, 0.1);
  color: #FFC107;
}

.teacher-profile {
  box-shadow: 0 10px 30px rgba(255, 193, 7, 0.1);
}

/* Update responsive styles */
@media (max-width: 480px) {
  .teacher-section::before {
    background-size: 15px 15px;
    opacity: 0.3;
  }
  
  .floating-element {
    opacity: 0.5;
  }
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
  background: linear-gradient(45deg, rgba(255, 193, 7, 0.1), rgba(255, 213, 79, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

/* Update the border color for profile elements */
.profile-header {
  border-bottom: 1px solid rgba(255, 193, 7, 0.1);
  padding-bottom: 1.5rem;
  margin-bottom: 0.5rem;
}

.image-accent {
  position: absolute;
  bottom: -20px;
  right: -20px;
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, #FFC107, #FFD54F);
  border-radius: 1rem;
  z-index: -1;
  opacity: 0.7;
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

.section-header {
  text-align: center;
  max-width: 700px;
  margin: 0 auto 4rem;
}

.section-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(45deg, #f37b4b, #5c3617);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-subtitle {
  font-size: 1.25rem;
  color: #4A5568;
  line-height: 1.6;
}

.teacher-profile {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 3rem;
  align-items: start;
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(75, 150, 243, 0.1);
}

.profile-image-container {
  position: relative;
  overflow: hidden;
  height: 100%;
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.teacher-profile:hover .profile-image {
  transform: scale(1.03);
}

.image-accent {
  position: absolute;
  bottom: -20px;
  right: -20px;
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  border-radius: 1rem;
  z-index: -1;
  opacity: 0.7;
}

.profile-content {
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.profile-header {
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
  padding-bottom: 1.5rem;
  margin-bottom: 0.5rem;
}

.teacher-name {
  font-family: 'Quicksand', sans-serif;
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 0.5rem;
}

.teacher-credentials {
  font-size: 1.1rem;
  color: #eb4520;
  font-weight: 600;
}

.profile-bio {
  font-size: 1.05rem;
  color: #4A5568;
  line-height: 1.7;
  margin-bottom: 1rem;
}

.teacher-achievements {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
  margin-top: 1rem;
}

.achievement {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.achievement-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.75rem;
  height: 1.75rem;
  min-width: 1.75rem;
  background: rgba(75, 150, 243, 0.1);
  border-radius: 50%;
  color: #f38e4b;
}

.achievement-icon svg {
  width: 1rem;
  height: 1rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .teacher-profile {
    gap: 2rem;
  }
  
  .profile-content {
    padding: 2rem;
  }
  
  .teacher-name {
    font-size: 1.75rem;
  }
}

@media (max-width: 768px) {
  .teacher-section {
    padding: 3rem 1rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .section-subtitle {
    font-size: 1.125rem;
    margin-bottom: 2rem;
  }
  
  .teacher-profile {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .profile-image-container {
    max-height: 300px;  /* Reduced from 400px */
  }
  
  .profile-content {
    padding: 1.5rem;
    gap: 1rem;  /* Reduced from 1.5rem */
  }
  
  .teacher-achievements {
    grid-template-columns: 1fr;
    gap: 1rem;  /* Reduced from 1.25rem */
  }

  .profile-bio {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 0.5rem;
  }
}

@media (max-width: 480px) {
  .teacher-section {
    padding: 2rem 1rem;
  }
  
  .section-title {
    font-size: 1.75rem;
  }
  
  .profile-image-container {
    max-height: 250px;  /* Further reduced */
  }
  
  .teacher-name {
    font-size: 1.5rem;
  }
  
  .teacher-credentials {
    font-size: 1rem;
  }
  
  .profile-header {
    padding-bottom: 1rem;
  }
  
  .achievement {
    font-size: 0.9rem;
  }
  
  .achievement-icon {
    width: 1.5rem;
    height: 1.5rem;
    min-width: 1.5rem;
  }
}
</style>