<template>
    <section class="classroom-preview">
      <!-- Add background patterns -->
      <div class="background-patterns">
        <div class="circle-pattern"></div>
        <div class="grid-pattern"></div>
      </div>
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">Our <span class="gradient-text">Classroom</span> Experience</h2>
          <p class="section-subtitle">
            Experience our modern, engaging, and thoughtfully designed learning environments where students thrive
          </p>
        </div>
  
        <div class="classroom-content">
          <div class="classroom-info">
            <h3 class="classroom-title">State-of-the-Art Learning Spaces</h3>
            <p class="classroom-description">
              Our classrooms are designed to inspire creativity, collaboration, and academic excellence. 
              Each space is carefully crafted to provide the optimal learning environment for students of all ages.
            </p>
            <ul class="classroom-features">
              <li><span class="feature-icon">✓</span> Interactive technology in every classroom</li>
              <li><span class="feature-icon">✓</span> Comfortable, ergonomic furniture</li>
              <li><span class="feature-icon">✓</span> Engaging learning centers and resource areas</li>
              <li><span class="feature-icon">✓</span> Natural lighting and calming color schemes</li>
              <li><span class="feature-icon">✓</span> Flexible layouts for different learning activities</li>
              <li><span class="feature-icon">✓</span> Dedicated spaces for group collaboration</li>
            </ul>
            <button class="explore-button">Schedule a Visit</button>
          </div>
  
          <div class="classroom-gallery">
            <div class="gallery-main">
              <img 
                :src="'/api/placeholder/600/400'" 
                :alt="`Classroom view ${currentImage + 1}`"
                class="main-image"
              />
              <div class="gallery-navigation">
                <button @click="prevImage" class="nav-button prev-button">❮</button>
                <div class="image-indicators">
                  <span 
                    v-for="n in totalImages" 
                    :key="n" 
                    class="indicator"
                    :class="{ 'active': currentImage === n - 1 }"
                    @click="setImage(n - 1)"
                  ></span>
                </div>
                <button @click="nextImage" class="nav-button next-button">❯</button>
              </div>
            </div>
          </div>
        </div>
      </div>
  
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  const currentImage = ref(0);
  const totalImages = 6; // Total number of classroom images
  
  const setImage = (index) => {
    currentImage.value = index;
  };
  
  const nextImage = () => {
    currentImage.value = (currentImage.value + 1) % totalImages;
  };
  
  const prevImage = () => {
    currentImage.value = (currentImage.value - 1 + totalImages) % totalImages;
  };
  
  // Auto-rotate images
  onMounted(() => {
    const interval = setInterval(() => {
      nextImage();
    }, 5000);
  
    // Clean up interval on unmount
    return () => clearInterval(interval);
  });
  </script>
  
  <style scoped>
  /* Add new background pattern styles */
  .background-patterns {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    pointer-events: none;
  }
  
  .circle-pattern {
    position: absolute;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: linear-gradient(45deg, rgba(255, 193, 7, 0.05), rgba(255, 213, 79, 0.05));
    top: -100px;
    right: -100px;
  }
  
  .grid-pattern {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: 
      linear-gradient(rgba(255, 193, 7, 0.05) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 193, 7, 0.05) 1px, transparent 1px);
    background-size: 20px 20px;
    opacity: 0.5;
  }
  
  .classroom-preview {
    position: relative;  /* Add this */
    padding: 5rem 2rem;
    background-color: white;
    font-family: 'Poppins', sans-serif;
    overflow: hidden;  /* Add this */
  }
  
  .section-container {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .section-header {
    text-align: center;
    margin-bottom: 3rem;
  }
  
  .section-title {
    font-family: 'Quicksand', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    color: #2D3748;
    margin-bottom: 1rem;
  }
  
  .gradient-text {
    background: linear-gradient(45deg, #FFC107, #FFD54F);
    -webkit-background-clip: text;
    background-clip: text;  /* Added for better browser support */
    -webkit-text-fill-color: transparent;
    color: #FFC107;  /* Fallback */
  }
  
  .section-subtitle {
    font-size: 1.25rem;
    color: #4A5568;
    max-width: 700px;
    margin: 0 auto;
  }
  
  .classroom-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
  }
  
  .classroom-info {
    padding-right: 2rem;
  }
  
  .classroom-title {
    font-family: 'Quicksand', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #2D3748;
    margin-bottom: 1rem;
  }
  
  .classroom-description {
    font-size: 1.1rem;
    color: #4A5568;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }
  
  .classroom-features {
    list-style: none;
    padding: 0;
    margin-bottom: 2rem;
  }
  
  .classroom-features li {
    margin-bottom: 0.75rem;
    font-size: 1.05rem;
    color: #4A5568;
    display: flex;
    align-items: center;
  }
  
  .feature-icon {
    color: #FFC107;
    font-weight: bold;
    margin-right: 0.75rem;
  }
  
  .explore-button {
    padding: 0.875rem 1.75rem;
    background: linear-gradient(45deg, #FFC107, #FFD54F);
    color: #333;  /* Changed to dark text for better contrast */
    border: none;
    border-radius: 0.5rem;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .explore-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(255, 193, 7, 0.3);
    background: linear-gradient(45deg, #FFD54F, #FFC107);  /* Reverse gradient on hover */
  }
  
  .classroom-gallery {
    width: 100%;
  }
  
  .gallery-main {
    position: relative;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: 0 10px 25px rgba(255, 193, 7, 0.15);
  }
  
  .main-image {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.5s ease;
  }
  
  .gallery-navigation {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(to top, rgba(0,0,0,0.5), transparent);
  }
  
  .nav-button {
    background: rgba(255, 255, 255, 0.8);
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-size: 1.2rem;
    color: #FFC107;
    transition: all 0.3s ease;
  }
  
  .nav-button:hover {
    background: white;
    color: #FFD54F;  /* Added hover color */
    transform: scale(1.1);
  }
  
  .image-indicators {
    display: flex;
    gap: 8px;
  }
  
  .indicator {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .indicator.active {
    background: white;
    transform: scale(1.2);
  }
  
  .classroom-testimonial {
    max-width: 900px;
    margin: 5rem auto 0;
    padding: 2.5rem;
    background: white;
    border-radius: 1rem;
    box-shadow: 0 10px 25px rgba(255, 193, 7, 0.1);
    position: relative;
  }
  
  .testimonial-content {
    position: relative;
    z-index: 1;
  }
  
  .quote-mark {
    position: absolute;
    top: -2rem;
    left: 2rem;
    font-size: 8rem;
    color: rgba(255, 193, 7, 0.1);
    font-family: Georgia, serif;
    line-height: 1;
  }
  
  .testimonial-text {
    font-size: 1.2rem;
    color: #4A5568;
    line-height: 1.7;
    margin-bottom: 1.5rem;
    font-style: italic;
  }
  
  .testimonial-author {
    display: flex;
    align-items: center;
  }
  
  .author-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 1rem;
  }
  
  .author-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: #2D3748;
    margin: 0;
  }
  
  .author-title {
    font-size: 0.9rem;
    color: #4A5568;
    margin: 0;
  }
  
  /* Responsive Design */
  @media (max-width: 1024px) {
    .classroom-content {
      gap: 2rem;
    }
    
    .classroom-info {
      padding-right: 1rem;
    }
  }
  
  /* Update responsive styles */
  @media (max-width: 768px) {
    .classroom-content {
      grid-template-columns: 1fr;
      gap: 2rem;
    }
    
    .classroom-info {
      padding-right: 0;
      order: 2;
    }
    
    .classroom-gallery {
      order: 1;
    }
  
    .circle-pattern {
      width: 300px;
      height: 300px;
      top: -50px;
      right: -50px;
    }
  
    .grid-pattern {
      background-size: 15px 15px;
    }
  }
  
  @media (max-width: 480px) {
    .section-title {
      font-size: 2.5rem;
    }
    
    .classroom-title {
      font-size: 1.75rem;
    }
  
    .circle-pattern {
      width: 200px;
      height: 200px;
      top: -30px;
      right: -30px;
    }
  
    .grid-pattern {
      background-size: 10px 10px;
      opacity: 0.3;
    }
    
    .classroom-preview {
      padding: 3rem 1rem;
    }
  
    .classroom-features li {
      font-size: 0.95rem;
    }
  
    .explore-button {
      width: 100%;
      padding: 1rem;
    }
  }
  
  .classroom-testimonial {
    padding: 1.5rem;
  }
  
  .testimonial-text {
    font-size: 1rem;
  }
  
  .nav-button {
    width: 30px;
    height: 30px;
    font-size: 1rem;
  }
  </style>