<template>
  <section class="contact-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>
    
    <div class="content-container">
      <div class="section-header">
        <div class="badge-container">
          <div class="badge">
            <span class="badge-icon">📞</span>
            <span>Get in Touch</span>
          </div>
        </div>
        <h2 class="section-title">Ready to <span class="accent-text">Connect</span>?</h2>
        <p class="section-description">Reach out to us and start your learning journey today</p>
      </div>
      
      <div class="contact-cards-container">
        <!-- Contact Info Card -->
        <div class="contact-info-card">
          <div class="card-header">
            <div class="header-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v5Z"></path>
                <path d="M18 9h2a2 2 0 0 1 2 2v11l-4-4h-6a2 2 0 0 1-2-2v-1"></path>
              </svg>
            </div>
            <h3 class="card-title">Contact Us</h3>
          </div>
          
          <div class="contact-methods">
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
              </div>
              <div class="method-details">
                <span class="method-label">Address</span>
                <span class="method-value">123 Learning Lane, Tech City</span>
              </div>
            </div>
            
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="4" width="20" height="16" rx="2"></rect>
                  <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                </svg>
              </div>
              <div class="method-details">
                <span class="method-label">Email</span>
                <a href="mailto:support@euphoriaclasses.com" class="method-value method-link">support@euphoriaclasses.com</a>
              </div>
            </div>
            
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </div>
              <div class="method-details">
                <span class="method-label">Phone</span>
                <a href="tel:+15551234567" class="method-value method-link">+1 (555) 123-4567</a>
              </div>
            </div>
          </div>
          
          <div class="social-links">
            <a href="#" class="social-link" aria-label="Facebook">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="Twitter">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="Instagram">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="LinkedIn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                <rect x="2" y="9" width="4" height="12"></rect>
                <circle cx="4" cy="4" r="2"></circle>
              </svg>
            </a>
          </div>
        </div>
        
        <!-- Contact Form Card -->
        <div class="contact-form-card">
          <form @submit.prevent="submitForm" class="contact-form">
            <div class="form-header">
              <h3 class="form-title">Send a Message</h3>
              <p class="form-subtitle">We'll get back to you as soon as possible</p>
            </div>
            
            <div class="form-group">
              <label for="name" class="form-label">Name</label>
              <input
                id="name"
                type="text"
                v-model="form.name"
                placeholder="Your name"
                required
                class="form-input"
              />
            </div>
            
            <div class="form-group">
              <label for="email" class="form-label">Email</label>
              <input
                id="email"
                type="email"
                v-model="form.email"
                placeholder="Your email address"
                required
                class="form-input"
              />
            </div>
            
            <div class="form-group">
              <label for="message" class="form-label">Message</label>
              <textarea
                id="message"
                v-model="form.message"
                placeholder="How can we help you?"
                required
                class="form-textarea"
              ></textarea>
            </div>
            
            <button type="submit" class="submit-button">
              <span>Send Message</span>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="send-icon">
                <path d="m22 2-7 20-4-9-9-4Z"></path>
                <path d="M22 2 11 13"></path>
              </svg>
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  name: '',
  email: '',
  message: ''
});

function submitForm() {
  alert('Thank you for your message! We will get back to you soon.');
  form.value = { name: '', email: '', message: '' };
}
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

.contact-section {
  position: relative;
  padding: 5rem 1.5rem;
  background: linear-gradient(135deg, #F0F7FF, #E6F2FF);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Nunito', sans-serif;
  overflow: hidden;
  color: #2D3748;
}

/* Animated Background */
.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  overflow: hidden;
}

.floating-element {
  position: absolute;
  background: linear-gradient(45deg, rgba(75, 150, 243, 0.1), rgba(49, 120, 230, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.floating-element:nth-child(1) { width: 20%; height: 20vw; top: 5%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { width: 15%; height: 15vw; top: 65%; left: 85%; animation-delay: -4s; }
.floating-element:nth-child(3) { width: 25%; height: 25vw; top: 35%; left: 55%; animation-delay: -8s; }
.floating-element:nth-child(4) { width: 10%; height: 10vw; top: 75%; left: 15%; animation-delay: -12s; }
.floating-element:nth-child(5) { width: 18%; height: 18vw; top: 20%; left: 75%; animation-delay: -16s; }
.floating-element:nth-child(6) { width: 12%; height: 12vw; top: 80%; left: 45%; animation-delay: -5s; }
.floating-element:nth-child(7) { width: 14%; height: 14vw; top: 15%; left: 35%; animation-delay: -9s; }
.floating-element:nth-child(8) { width: 20%; height: 20vw; top: 60%; left: 70%; animation-delay: -13s; }

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(3deg); }
  100% { transform: translateY(-40px) rotate(-3deg); }
}

.content-container {
  max-width: 1200px;
  width: 100%;
  position: relative;
  z-index: 1;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.badge-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.badge {
  display: flex;
  align-items: center;
  padding: 0.6rem 1rem;
  background: rgba(75, 150, 243, 0.15);
  border-radius: 100px;
  backdrop-filter: blur(10px);
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(0.8rem, 2.5vw, 1rem);
  font-weight: 600;
  letter-spacing: 0.02em;
  border: 1px solid rgba(75, 150, 243, 0.3);
  box-shadow: 0 2px 10px rgba(75, 150, 243, 0.2);
  gap: 0.5rem;
  color: #3178E6;
  width: fit-content;
  margin: 0 auto;
}

.badge-icon {
  font-size: clamp(1rem, 3vw, 1.25rem);
}

.section-title {
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.accent-text {
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
  position: relative;
}

.accent-text::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  border-radius: 4px;
}

.section-description {
  font-size: clamp(1rem, 3vw, 1.25rem);
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.contact-cards-container {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 2rem;
}

/* Contact Info Card */
.contact-info-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2.5rem;
  box-shadow: 0 10px 30px rgba(75, 150, 243, 0.1);
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(75, 150, 243, 0.1);
  transition: all 0.3s ease;
}

.contact-info-card:hover {
  box-shadow: 0 15px 35px rgba(75, 150, 243, 0.15);
  border: 1px solid rgba(75, 150, 243, 0.2);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.header-icon {
  width: 3rem;
  height: 3rem;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-icon svg {
  width: 1.5rem;
  height: 1.5rem;
  color: white;
}

.card-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.5rem;
  font-weight: 600;
  color: #2D3748;
}

.contact-methods {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.contact-method {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.method-icon {
  width: 2.5rem;
  height: 2.5rem;
  background: rgba(75, 150, 243, 0.1);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.method-icon svg {
  width: 1.25rem;
  height: 1.25rem;
  color: #3178E6;
}

.method-details {
  display: flex;
  flex-direction: column;
}

.method-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.25rem;
}

.method-value {
  font-size: 1rem;
  color: #2D3748;
  line-height: 1.4;
}

.method-link {
  color: #3178E6;
  text-decoration: none;
  transition: color 0.3s ease;
}

.method-link:hover {
  color: #4B96F3;
  text-decoration: underline;
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: auto;
}

.social-link {
  width: 2.5rem;
  height: 2.5rem;
  background: #F0F7FF;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3178E6;
  transition: all 0.3s ease;
}

.social-link svg {
  width: 1.25rem;
  height: 1.25rem;
}

.social-link:hover {
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(75, 150, 243, 0.2);
}

/* Contact Form Card */
.contact-form-card {
  background: white;
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 5px 20px rgba(75, 150, 243, 0.08);
  border: none;
  transition: all 0.3s ease;
  max-width: 600px; /* Ensures form doesn't stretch too wide */
  margin: 0 auto; /* Centers the form */
  width: 100%;
}

.form-header {
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-title {
  font-family: 'Nunito', sans-serif;
  font-size: 1.75rem;
  font-weight: 600;
  color: #2D3748;
  margin-bottom: 0.5rem;
}

.form-subtitle {
  font-size: 1rem;
  color: #718096;
  line-height: 1.5;
}

.form-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.form-label {
  display: block;
  font-weight: 500;
  color: #4A5568;
  font-size: 0.9375rem;
  font-family: 'Nunito', sans-serif;
  margin-bottom: 0.5rem;
}

.form-input,
.form-textarea {
  width: 100%;
  max-width: 500px; /* Limits the input width */
  margin: 0 auto; /* Centers input boxes */
  padding: 0.875rem 1rem;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 1rem;
  color: #4A5568;
  transition: all 0.2s ease;
  box-shadow: none;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #4B96F3;
  box-shadow: 0 0 0 2px rgba(75, 150, 243, 0.2);
  background: white;
}

.form-textarea {
  resize: vertical;
  min-height: 130px;
  padding: 0.875rem 1rem;
}

.submit-button {
  width: 100%;
  padding: 0.875rem 0;
  background: #4B96F3;
  border: none;
  border-radius: 10px;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Quicksand', sans-serif;
  height: 48px;
  margin-top: 0.5rem;
  box-shadow: 0 4px 12px rgba(75, 150, 243, 0.2);
}

.send-icon {
  width: 1.125rem;
  height: 1.125rem;
  transition: transform 0.3s ease;
  margin-left: 0.125rem;
}

.submit-button:hover {
  background: #3178E6;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(75, 150, 243, 0.3);
}

.submit-button:hover .send-icon {
  transform: translateX(3px);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .section-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .contact-section {
    padding: 4rem 1.5rem;
  }
  
  .contact-cards-container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .section-title {
    font-size: 2.25rem;
  }
  
  .section-description {
    font-size: 1.125rem;
  }
}

@media (max-width: 480px) {
  .contact-section {
    padding: 3rem 1rem;
  }
  
  .contact-info-card {
    padding: 1.5rem;
  }
  
  .contact-form-card {
    max-width: 95%;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .card-header {
    margin-bottom: 1.5rem;
  }
  
  .header-icon {
    width: 2.5rem;
    height: 2.5rem;
  }
  
  .header-icon svg {
    width: 1.25rem;
    height: 1.25rem;
  }
  
  .card-title {
    font-size: 1.25rem;
  }
  
  .form-title {
    font-size: 1.5rem;
  }
  
  .form-subtitle {
    font-size: 0.9375rem;
  }
  
  .contact-methods {
    gap: 1.25rem;
  }
  
  .method-icon {
    width: 2rem;
    height: 2rem;
  }
  
  .social-links {
    justify-content: center;
  }
  
  .form-textarea {
    min-height: 100px;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  .form-input,
  .form-textarea {
    width: 100%;
    max-width: 100%;
  }
  
  .submit-button {
    height: 44px;
    font-size: 0.9375rem;
  }
}

@media (max-width: 768px) {
  .contact-form-card {
    max-width: 90%; /* Takes more space on mobile */
    padding: 1.5rem;
  }

  .form-input,
  .form-textarea {
    max-width: 100%; /* Full width for mobile */
    width: 100%;
  }
}

@media (max-width: 360px) {
  .contact-section {
    padding: 2rem 0.75rem;
  }
  
  .contact-info-card,
  .contact-form-card {
    padding: 1.5rem;
  }
  
  .section-title {
    font-size: 1.75rem;
  }
  
  .badge {
    font-size: 0.8rem;
    padding: 0.5rem 0.75rem;
  }
  
  .method-icon {
    width: 1.75rem;
    height: 1.75rem;
  }
  
  .method-icon svg {
    width: 1rem;
    height: 1rem;
  }
  
  .social-link {
    width: 2.25rem;
    height: 2.25rem;
  }
  
  .submit-button {
    padding: 0.875rem 1.5rem;
    font-size: 0.95rem;
  }
}
</style>