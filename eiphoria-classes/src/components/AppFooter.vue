<template>
  <footer class="footer-container">
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>
    
    <div class="footer-content">

      <div class="footer-grid">
        <!-- Brand Section -->
        <div class="brand-section">
          <router-link to="/" class="footer-logo">
            <span class="gradient-text">Euphoria</span>
            <span class="logo-dot">Tutorials</span>
          </router-link>
          <p class="brand-description">
            Empowering students through personalized education. Join our community of dedicated teachers and engaged parents.
          </p>
          <div class="social-links">
            <a v-for="social in socialLinks" 
               :key="social.name" 
               :href="social.url" 
               class="social-link" 
               :aria-label="social.name">
              <component :is="social.icon" />
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="links-section">
          <h3 class="section-title">Navigation</h3>
          <nav class="footer-nav">
            <ul class="footer-links">
              <li v-for="item in menuItems" :key="item.path">
                <router-link :to="item.path" class="footer-link">
                  {{ item.name }}
                </router-link>
              </li>
            </ul>
          </nav>
        </div>

        <!-- Contact Info -->
        <div class="contact-section">
          <h3 class="section-title">Contact</h3>
          <ul class="contact-list">
            <li class="contact-item">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/>
              </svg>
              <a href="tel:+1234567890" class="contact-link">+1 (234) 567-890</a>
            </li>
            <li class="contact-item">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <path d="M22 6l-10 7L2 6"/>
              </svg>
              <a href="mailto:info@classconnect.com" class="contact-link">info@classconnect.com</a>
            </li>
            <li class="contact-item">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
              <a href="https://maps.google.com" target="_blank" class="contact-link">123 Education St, Learning City</a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="bottom-bar">
        <p class="copyright-text">
          © {{ currentYear }} Euphoria Tutorials. All rights reserved.
        </p>
        <div class="legal-links">
          <a href="/privacy" class="legal-link">Privacy Policy</a>
          <a href="/terms" class="legal-link">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear()

const menuItems = [
  { name: 'Home', path: '/' },
  { name: 'About Us', path: '/about' },
  { name: 'Reviews', path: '/reviews' },
  { name: 'Contact', path: '/contact' },
  { name: 'Login', path: '/login' }
]

const socialLinks = [
  {
    name: 'Twitter',
    url: '#',
    icon: 'TwitterIcon'
  },
  {
    name: 'Facebook',
    url: '#',
    icon: 'FacebookIcon'
  },
  {
    name: 'Instagram',
    url: '#',
    icon: 'InstagramIcon'
  }
]
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.footer-container {
  background: linear-gradient(to bottom, #F0F7FF, #E6F2FF);
  color: #2D3748;
  padding: 6rem 1.5rem 2rem;
  position: relative;
  overflow: hidden;
  font-family: 'Nunito', sans-serif;
}

.footer-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(to right, transparent, #4B96F3, transparent);
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

.footer-content {
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

/* Footer Grid */
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 4rem;
  margin-bottom: 4rem;
}

.footer-logo {
  display: inline-block;
  font-size: 2.5rem;
  font-weight: 800;
  text-decoration: none;
  margin-bottom: 1.5rem;
  font-family: 'Quicksand', sans-serif;
}

.gradient-text {
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.logo-dot {
  color: #3178E6;
}

.brand-description {
  color: #4A5568;
  font-size: 1.1rem;
  line-height: 1.7;
  margin-bottom: 2rem;
}

.section-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 40px;
  height: 3px;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  border-radius: 2px;
}

.footer-links,
.contact-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-link {
  color: #4A5568;
  text-decoration: none;
  font-size: 1.1rem;
  display: block;
  padding: 0.5rem 0;
  transition: all 0.3s ease;
}

.footer-link:hover {
  color: #3178E6;
  transform: translateX(4px);
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.contact-icon {
  width: 1.25rem;
  height: 1.25rem;
  stroke: #4B96F3;
  stroke-width: 2;
}

.contact-link {
  color: #4A5568;
  text-decoration: none;
  transition: color 0.3s ease;
}

.contact-link:hover {
  color: #3178E6;
}

.social-links {
  display: flex;
  gap: 1.5rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.8);
  color: #4B96F3;
  border: 1px solid rgba(75, 150, 243, 0.3);
  transition: all 0.3s ease;
}

.social-link:hover {
  transform: translateY(-2px);
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  color: white;
  border-color: transparent;
  box-shadow: 0 4px 12px rgba(75, 150, 243, 0.3);
}

/* Bottom Bar */
.bottom-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(75, 150, 243, 0.2);
}

.copyright-text {
  color: #718096;
}

.legal-links {
  display: flex;
  gap: 2rem;
}

.legal-link {
  color: #718096;
  text-decoration: none;
  transition: color 0.3s ease;
}

.legal-link:hover {
  color: #3178E6;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
  }

  .brand-section {
    grid-column: span 2;
  }
}

@media (max-width: 768px) {
  .footer-container {
    padding: 4rem 1.5rem 2rem;
  }
  
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .brand-section {
    grid-column: span 1;
    text-align: center;
  }

  .social-links {
    justify-content: center;
  }

  .section-title {
    text-align: center;
    margin-top: 1rem;
    display: block;
    width: 100%;
  }
  
  .section-title::after {
    left: 50%;
    transform: translateX(-50%);
  }

  .footer-links,
  .contact-list {
    text-align: center;
  }

  .contact-item {
    justify-content: center;
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }
  
  .contact-link {
    display: block;
    width: 100%;
    text-align: center;
  }

  .bottom-bar {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .footer-container {
    padding: 3rem 1rem 1.5rem;
  }
  
  .footer-logo {
    font-size: 2rem;
  }
  
  .brand-description {
    font-size: 1rem;
  }
  
  .footer-link {
    font-size: 1rem;
    padding: 0.4rem 0;
  }
  
  .social-link {
    width: 2.2rem;
    height: 2.2rem;
  }
  
  .legal-links {
    gap: 1rem;
    font-size: 0.9rem;
  }
  
  .contact-item {
    margin-bottom: 1.5rem;
  }
  
  .contact-icon {
    margin-bottom: 0.25rem;
  }
}
</style>