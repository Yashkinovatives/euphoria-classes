<template>
    <section class="team-section">
      <!-- Animated Background Elements -->
      <div class="animated-bg">
        <div v-for="n in 8" :key="n" class="floating-element"></div>
      </div>
  
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Meet Our <span class="gradient-text">Team</span></h2>
          <p class="section-subtitle">Passionate educators and industry experts dedicated to your success</p>
        </div>
        
        <div class="team-grid">
          <div 
            v-for="member in teamMembers" 
            :key="member.id"
            class="team-card"
          >
            <div class="member-image-container">
              <img :src="member.image" :alt="member.name" class="member-image" />
              <div class="image-overlay">
                <div class="social-links">
                  <a 
                    v-for="social in member.socials" 
                    :key="social.name" 
                    :href="social.url" 
                    class="social-link" 
                    :aria-label="social.name"
                  >
                    <svg v-if="social.name === 'LinkedIn'" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                    <svg v-if="social.name === 'Twitter'" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path>
                    </svg>
                  </a>
                </div>
              </div>
            </div>
            <div class="member-info">
              <h3 class="member-name">{{ member.name }}</h3>
              <p class="member-position">{{ member.position }}</p>
              <p class="member-bio">{{ member.bio }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const teamMembers = ref([
    {
      id: 1,
      name: "Dr. Sarah Johnson",
      position: "Founder & CEO",
      bio: "With over 15 years in education technology, Sarah leads our vision for transforming online learning.",
      image: "/api/placeholder/400/400",
      socials: [
        { name: "LinkedIn", url: "#" },
        { name: "Twitter", url: "#" }
      ]
    },
    {
      id: 2,
      name: "Michael Chen",
      position: "Chief Learning Officer",
      bio: "Former university professor passionate about creating engaging curriculum and learning experiences.",
      image: "/api/placeholder/400/400",
      socials: [
        { name: "LinkedIn", url: "#" },
        { name: "Twitter", url: "#" }
      ]
    },
    {
      id: 3,
      name: "Emily Rodriguez",
      position: "Head of Technology",
      bio: "Tech innovator with expertise in AI-powered learning algorithms and adaptive educational systems.",
      image: "/api/placeholder/400/400",
      socials: [
        { name: "LinkedIn", url: "#" },
        { name: "Twitter", url: "#" }
      ]
    },
    {
      id: 4,
      name: "James Wilson",
      position: "Head of Student Success",
      bio: "Dedicated to ensuring every student receives personalized support throughout their learning journey.",
      image: "/api/placeholder/400/400",
      socials: [
        { name: "LinkedIn", url: "#" },
        { name: "Twitter", url: "#" }
      ]
    }
  ]);
  </script>
  
  <style scoped>
  /* Import Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  
  .team-section {
    position: relative;
    background: rgba(255, 255, 255, 0.6);
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
  
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2.5rem;
  }
  
  .team-card {
    background: white;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.08);
    transition: all 0.3s ease;
    height: 100%;
  }
  
  .team-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(139, 92, 246, 0.15);
  }
  
  .member-image-container {
    position: relative;
    overflow: hidden;
  }
  
  .member-image {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  
  .team-card:hover .member-image {
    transform: scale(1.05);
  }
  
  .image-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(124, 58, 237, 0.9), transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 1.5rem;
  }
  
  .team-card:hover .image-overlay {
    opacity: 1;
  }
  
  .social-links {
    display: flex;
    gap: 1rem;
  }
  
  .social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2.5rem;
    height: 2.5rem;
    background: white;
    border-radius: 50%;
    color: #7C3AED;
    transition: all 0.3s ease;
  }
  
  .social-link:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    background: linear-gradient(135deg, #7C3AED, #C084FC);
    color: white;
  }
  
  .member-info {
    padding: 1.5rem;
  }
  
  .member-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.25rem;
  }
  
  .member-position {
    font-size: 0.875rem;
    color: #7C3AED;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  
  .member-bio {
    font-size: 0.95rem;
    color: #475569;
    line-height: 1.6;
  }
  
  /* Responsive Design */
  @media (max-width: 1024px) {
    .team-grid {
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    }
  }
  
  @media (max-width: 768px) {
    .team-section {
      padding: 4rem 1.5rem;
    }
    
    .section-title {
      font-size: 2rem;
    }
    
    .section-subtitle {
      font-size: 1.125rem;
    }
    
    .team-grid {
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }
  }
  
  @media (max-width: 480px) {
    .team-section {
      padding: 3rem 1rem;
    }
    
    .section-title {
      font-size: 1.75rem;
    }
    
    .team-grid {
      grid-template-columns: 1fr;
    }
    
    .member-info {
      padding: 1.25rem;
    }
  }
  </style>