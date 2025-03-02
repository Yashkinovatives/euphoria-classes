<template>
    <div class="testimonials-section">
      <div class="decorative-elements">
        <div class="circle circle-teal"></div>
        <div class="circle circle-yellow"></div>
        <div class="circle circle-purple"></div>
        <div class="circle circle-pink"></div>
      </div>
  
      <div class="content-wrapper">
        <div class="header">
          <h2 class="section-title">What <strong>People</strong> Say <strong>About Us</strong></h2>
          <p class="section-description">Nullam et elementum augue auctor dui. Donec non nunc sodales massa Finibus imperdiet tortor.</p>
        </div>
  
        <div class="testimonials-container">
          <!-- Left Column -->
          <div class="testimonial-column left-column">
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[0].review }}</p>
              <div class="user-info">
                <img :src="testimonials[0].image" :alt="testimonials[0].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[0].name }}</h3>
                  <p class="user-role">{{ testimonials[0].role }}</p>
                </div>
              </div>
            </div>
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[3].review }}</p>
              <div class="user-info">
                <img :src="testimonials[3].image" :alt="testimonials[3].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[3].name }}</h3>
                  <p class="user-role">{{ testimonials[3].role }}</p>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Middle Column -->
          <div class="testimonial-column middle-column">
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[1].review }}</p>
              <div class="user-info">
                <img :src="testimonials[1].image" :alt="testimonials[1].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[1].name }}</h3>
                  <p class="user-role">{{ testimonials[1].role }}</p>
                </div>
              </div>
            </div>
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[4].review }}</p>
              <div class="user-info">
                <img :src="testimonials[4].image" :alt="testimonials[4].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[4].name }}</h3>
                  <p class="user-role">{{ testimonials[4].role }}</p>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Right Column -->
          <div class="testimonial-column right-column">
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[2].review }}</p>
              <div class="user-info">
                <img :src="testimonials[2].image" :alt="testimonials[2].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[2].name }}</h3>
                  <p class="user-role">{{ testimonials[2].role }}</p>
                </div>
              </div>
            </div>
            <div class="testimonial-card">
              <div class="quote-mark">"</div>
              <p class="review">{{ testimonials[5].review }}</p>
              <div class="user-info">
                <img :src="testimonials[5].image" :alt="testimonials[5].name" class="user-image">
                <div class="user-details">
                  <h3 class="user-name">{{ testimonials[5].name }}</h3>
                  <p class="user-role">{{ testimonials[5].role }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TestimonialsSection',
    data() {
      return {
        testimonials: [
          {
            name: "Mark Anthony",
            role: "Web Developer",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image: "/person.jpg"
        },
          {
            name: "Dolly Rose",
            role: "Singer",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image: "/person.jpg"
          },
          {
            name: "Ardal Baten",
            role: "Web Developer",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image: "/person.jpg"
          },
          {
            name: "Tom Parkerman",
            role: "Web Developer",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image: "/person.jpg"
          },
          {
            name: "Anatolia Eva",
            role: "Blogger",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image: "/person.jpg"
          },
          {
            name: "Mokira",
            role: "Business Man",
            review: "Evad minim veniam, quis nostrud exercitatio ullamco laboris nisi ut aliquip ex ea commodo consequat.",
           image: "/person.jpg"
          }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .testimonials-section {
    position: relative;
    padding: 60px 20px;
    background-color: #f8f9ff;
    min-height: 100vh;
    overflow: hidden;
  }
  
  .decorative-elements {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;
  }
  
  .circle {
    position: absolute;
    border-radius: 50%;
  }
  
  .circle-teal {
    width: 80px;
    height: 80px;
    background: #2DD4BF;
    bottom: 20%;
    left: 5%;
    border-radius: 0 0 0 100%;
  }
  
  .circle-yellow {
    width: 40px;
    height: 40px;
    background: #FCD34D;
    top: 20%;
    right: 15%;
  }
  
  .circle-purple {
    width: 100px;
    height: 100px;
    background: rgba(167, 139, 250, 0.5);
    bottom: 15%;
    right: 20%;
  }
  
  .circle-pink {
    width: 60px;
    height: 60px;
    background: rgba(244, 114, 182, 0.5);
    top: 40%;
    right: 30%;
  }
  
  .content-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
  }
  
  .header {
    max-width: 600px;
    margin-bottom: 60px;
  }
  
  .section-title {
    font-size: 32px;
    font-weight: 500;
    margin-bottom: 16px;
  }
  
  .section-description {
    color: #666;
    line-height: 1.6;
  }
  
  .testimonials-container {
    display: flex;
    gap: 30px;
    justify-content: space-between;
  }
  
  .testimonial-column {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  
  .middle-column {
    margin-top: 60px;
  }
  
  .right-column {
    margin-top: 120px;
  }
  
  .testimonial-card {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    position: relative;
  }
  
  .quote-mark {
    position: absolute;
    top: -20px;
    left: -10px;
    font-size: 60px;
    color: #ddd;
    font-family: Georgia, serif;
  }
  
  .review {
    margin-bottom: 20px;
    color: #333;
    line-height: 1.6;
    font-size: 14px;
    position: relative;
  }
  
  .user-info {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .user-image {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .user-details {
    display: flex;
    flex-direction: column;
  }
  
  .user-name {
    font-weight: 600;
    font-size: 14px;
    margin: 0;
  }
  
  .user-role {
    color: #666;
    font-size: 12px;
    margin: 0;
  }
  
  @media (max-width: 1024px) {
    .testimonials-container {
      flex-direction: column;
    }
    
    .testimonial-column {
      margin-top: 0 !important;
    }
  }
  
  @media (max-width: 768px) {
    .header {
      text-align: center;
      margin-left: auto;
      margin-right: auto;
    }
  }
  </style>