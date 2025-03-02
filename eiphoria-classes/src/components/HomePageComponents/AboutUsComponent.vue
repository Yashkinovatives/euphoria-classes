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
            About <span class="gradient-text">Us</span>
          </h2>
          
          <div class="about-grid">
            <div class="about-image" v-motion 
                 :initial="{ opacity: 0, scale: 0.9 }" 
                 :enter="{ opacity: 1, scale: 1, transition: { duration: 800, delay: 200 } }">
                <img :src="image" alt="About our platform" />
              <div class="image-accent" v-motion 
                   :initial="{ opacity: 0, x: 30, y: 30 }" 
                   :enter="{ opacity: 1, x: 0, y: 0, transition: { duration: 1000, delay: 400 } }"></div>
            </div>
            
            <div class="about-text">
              <p v-motion 
                 :initial="{ opacity: 0, x: 40 }" 
                 :enter="{ opacity: 1, x: 0, transition: { duration: 800, delay: 300 } }">
                We're on a mission to transform education through technology. Our platform combines AI-driven insights with proven learning methodologies to create personalized educational experiences that adapt to your unique learning style.
              </p>
              
              <div class="key-features">
                <div class="feature" v-for="(feature, index) in features" :key="feature" v-motion 
                     :initial="{ opacity: 0, x: 30 }" 
                     :enter="{ opacity: 1, x: 0, transition: { duration: 600, delay: 400 + (index * 150) } }">
                  <div class="feature-icon">✓</div>
                  <div>{{ feature }}</div>
                </div>
              </div>
              
              <button class="learn-more-btn" v-motion 
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
    "Personalized Learning Paths",
    "Interactive Content",
    "Expert-Led Courses"
  ];
  </script>
  
  <style scoped>
  /* Import Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  
  .about-section {
    padding: 5rem 0;
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
    position: relative;
    overflow: hidden;
    color: #1e293b;
    font-family: 'Outfit', sans-serif;
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
  
  .about-content {
    width: 100%;
  }
  
  .section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 3rem;
    letter-spacing: -0.02em;
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
    background: linear-gradient(45deg, #7C3AED, #C084FC);
    border-radius: 4px;
  }
  
  .gradient-text {
    background: linear-gradient(45deg, #7C3AED, #C084FC);
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
    box-shadow: 0 15px 30px rgba(124, 58, 237, 0.1);
  }
  
  .about-image img {
    width: 100%;
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
    background: linear-gradient(135deg, #7C3AED, #C084FC);
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
    color: #475569;
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
    color: #1e293b;
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
    background: linear-gradient(135deg, #7C3AED, #C084FC);
    border-radius: 50%;
    color: white;
    font-size: 0.875rem;
    box-shadow: 0 4px 8px rgba(124, 58, 237, 0.2);
    transition: all 0.3s ease;
  }
  
  .feature:hover .feature-icon {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(124, 58, 237, 0.3);
  }
  
  .learn-more-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    background: linear-gradient(45deg, #7C3AED, #A855F7);
    color: white;
    border-radius: 100px;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    transition: all 0.3s ease;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
    margin-top: 0.5rem;
    align-self: flex-start;
    position: relative;
    overflow: hidden;
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
    box-shadow: 0 6px 15px rgba(124, 58, 237, 0.3);
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
  }
  
  @media (max-width: 480px) {
    .about-section {
      padding: 3rem 0;
    }
    
    .section-heading {
      font-size: 1.75rem;
    }
  }
  </style>