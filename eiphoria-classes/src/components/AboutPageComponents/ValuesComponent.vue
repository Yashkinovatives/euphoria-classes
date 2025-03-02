<template>
    <section class="values-section">
      <!-- Animated Background Elements -->
      <div class="animated-bg">
        <div v-for="n in 8" :key="n" class="floating-element"></div>
      </div>
  
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Our <span class="gradient-text">Values</span></h2>
          <p class="section-subtitle">The principles that guide everything we do</p>
        </div>
        
        <div class="values-grid">
          <div 
            v-for="value in values" 
            :key="value.id"
            class="value-card"
          >
            <div class="value-icon">
              <div class="icon-wrapper" v-html="value.icon"></div>
            </div>
            <h3 class="value-title">{{ value.title }}</h3>
            <p class="value-description">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const values = ref([
    {
      id: 1,
      title: "Excellence",
      description: "We're committed to the highest standards in everything we do, from curriculum development to student support.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
    },
    {
      id: 2,
      title: "Innovation",
      description: "We continuously explore new teaching methods and technologies to improve the learning experience for our students.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"></path></svg>'
    },
    {
      id: 3,
      title: "Inclusivity",
      description: "We believe education should be accessible to everyone, regardless of background, location, or circumstances.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>'
    },
    {
      id: 4,
      title: "Integrity",
      description: "We operate with honesty, transparency, and a strong ethical foundation in all our interactions and decisions.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
    },
    {
      id: 5,
      title: "Community",
      description: "We foster a supportive environment where students and educators can connect, collaborate, and grow together.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
    },
    {
      id: 6,
      title: "Adaptability",
      description: "We embrace change and continuously evolve our approach to meet the ever-changing needs of learners and industries.",
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2v6h-6"></path><path d="M3 12a9 9 0 0 1 15-6.7L21 8"></path><path d="M3 22v-6h6"></path><path d="M21 12a9 9 0 0 1-15 6.7L3 16"></path></svg>'
    }
  ]);
  </script>
  
  <style scoped>
  /* Import Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  
  .values-section {
    position: relative;
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
    padding: 5rem 2rem;
    font-family: 'Outfit', sans-serif;
    color: #1e293b;
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
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1rem;
    line-height: 1.2;
    letter-spacing: -0.02em;
  }
  
  .gradient-text {
    background: linear-gradient(45deg, #7C3AED, #C084FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .section-subtitle {
    font-size: 1.25rem;
    color: #475569;
    line-height: 1.6;
  }
  
  .values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2.5rem;
  }
  
  .value-card {
    background-color: white;
    border-radius: 1rem;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 10px 25px rgba(139, 92, 246, 0.08);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .value-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(139, 92, 246, 0.15);
  }
  
  .value-icon {
    margin-bottom: 1.5rem;
  }
  
  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 4.5rem;
    height: 4.5rem;
    background: rgba(139, 92, 246, 0.1);
    border-radius: 50%;
    color: #7C3AED;
    transition: all 0.3s ease;
  }
  
  .value-card:hover .icon-wrapper {
    background: linear-gradient(135deg, #7C3AED, #C084FC);
    color: white;
    transform: scale(1.1);
  }
  
  .value-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1rem;
  }
  
  .value-description {
    font-size: 1rem;
    color: #475569;
    line-height: 1.6;
  }
  
  /* Responsive Design */
  @media (max-width: 1200px) {
    .values-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 768px) {
    .values-section {
      padding: 4rem 1.5rem;
    }
    
    .values-grid {
      grid-template-columns: 1fr;
      gap: 2rem;
    }
    
    .section-title {
      font-size: 2rem;
    }
    
    .section-subtitle {
      font-size: 1.125rem;
    }
  }
  
  @media (max-width: 480px) {
    .values-section {
      padding: 3rem 1rem;
    }
    
    .section-title {
      font-size: 1.75rem;
    }
    
    .value-card {
      padding: 2rem;
    }
    
    .value-title {
      font-size: 1.25rem;
    }
  }
  </style>