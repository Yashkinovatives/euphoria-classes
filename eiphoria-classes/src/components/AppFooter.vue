<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-grid">
        <!-- Brand Section -->
        <div class="brand-section">
          <router-link to="/" class="footer-logo">
            <span class="logo-text">Euphoria</span>
            <span class="logo-separator">|</span>
            <span class="logo-subtext">Tutorials</span>
          </router-link>
          <p class="brand-description">
            Empowering students through personalized education. Join our community of dedicated teachers and engaged parents.
          </p>
          <div class="social-links">
            <a v-for="social in socialLinks" 
               :key="social.name" 
               :href="social.url" 
               class="social-link">
              <i :class="social.icon"></i>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="links-section">
          <h3 class="section-title">Quick Links</h3>
          <ul class="footer-links">
            <li v-for="item in menuItems" :key="item.path">
              <router-link :to="item.path" class="footer-link">
                {{ item.name }}
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div class="contact-section">
          <h3 class="section-title">Contact Us</h3>
          <ul class="contact-list">
            <li class="contact-item">
              <i class="contact-icon fas fa-phone"></i>
              <a href="tel:+1234567890" class="contact-link">+1 (234) 567-890</a>
            </li>
            <li class="contact-item">
              <i class="contact-icon fas fa-envelope"></i>
              <a href="mailto:info@euphoria.com" class="contact-link">info@euphoria.com</a>
            </li>
            <li class="contact-item">
              <i class="contact-icon fas fa-map-marker-alt"></i>
              <span class="contact-text">123 Education Street, City</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="bottom-bar">
        <p class="copyright">© {{ new Date().getFullYear() }} Euphoria Tutorials. All rights reserved.</p>
        <div class="legal-links">
          <a href="/privacy" class="legal-link">Privacy Policy</a>
          <a href="/terms" class="legal-link">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const menuItems = [
  { name: 'Home', path: '/' },
  { name: 'About Us', path: '/about' },
  { name: 'Contact', path: '/contact' },
  { name: 'Parent Login', path: '/login' }
];

const socialLinks = [
  { name: 'Facebook', url: '#', icon: 'fab fa-facebook-f' },
  { name: 'Twitter', url: '#', icon: 'fab fa-twitter' },
  { name: 'Instagram', url: '#', icon: 'fab fa-instagram' }
];
</script>

<style scoped>
.footer-container {
  background-color: #000;
  color: #fff;
  padding: 4rem 1.5rem 2rem;
  font-family: 'Arial', sans-serif;
}

.footer-logo {
  font-size: 1.5rem;
  font-weight: 700;
  text-decoration: none;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-text {
  color: #fff;
}

.logo-separator {
  color: #888;
  margin: 0 0.25rem;
}

.logo-subtext {
  color: #ccc;
  font-weight: 500;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 4rem;
  margin-bottom: 3rem;
  border-bottom: 1px solid #333;
  padding-bottom: 3rem;
}

.section-title {
  font-weight: 600;
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 1rem;
}

.brand-description {
  margin: 1.5rem 0;
  line-height: 1.6;
  color: #ccc;
}

.footer-links, .contact-list {
  list-style: none;
  padding: 0;
}

.footer-link {
  display: block;
  padding: 0.5rem 0;
  text-decoration: none;
  color: #ccc;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #fff;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.contact-icon {
  width: 20px;
  text-align: center;
  color: #888;
}

.contact-link, .contact-text {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s ease;
}

.contact-link:hover {
  color: #fff;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-link {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 2px solid #333;
  color: #ccc;
  transition: all 0.3s ease;
}

.social-link:hover {
  background-color: #222;
  color: #fff;
  border-color: #ccc;
}

.bottom-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 2rem;
  color: #888;
}

.copyright {
  margin: 0;
}

.legal-links {
  display: flex;
  gap: 2rem;
}

.legal-link {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s ease;
}

.legal-link:hover {
  color: #fff;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .bottom-bar {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .social-links {
    justify-content: center;
  }
  
  .legal-links {
    gap: 1rem;
  }
  
  .section-title {
    text-align: center;
  }
  
  .footer-links {
    text-align: center;
  }
  
  .contact-list {
    max-width: 300px;
    margin: 0 auto;
  }
}
</style>