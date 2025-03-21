<template>
  <div class="testimonials-section">
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <div class="content-container">
      <div class="testimonials-header" v-motion 
           :initial="{ opacity: 0, y: 100 }" 
           :enter="{ opacity: 1, y: 0, transition: { type: 'spring', stiffness: 50, damping: 15 } }">
        
        <div class="badge-container">
          <div class="badge" v-motion 
               :initial="{ scale: 0, opacity: 0 }" 
               :enter="{ scale: 1, opacity: 1, transition: { delay: 300 } }">
            <span class="badge-icon">💬</span>
            <span>Success Stories</span>
          </div>
        </div>

        <h1 class="title">
          What <strong>People</strong> Say 
          <div class="gradient-text-wrapper">
            <span class="gradient-text">About Us</span>
          </div>
        </h1>

        <p class="description">
          Read experiences shared by our community of learners who have transformed their skills and careers with our platform.
        </p>
      </div>

      <div v-if="loading" class="loading-container">
        <div class="loading-spinner"></div>
        <p>Loading reviews...</p>
      </div>
      
      <div v-else-if="testimonials.length === 0" class="no-reviews">
        <p>No reviews available yet. Be the first to share your experience!</p>
      </div>

      <div v-else class="testimonials-grid">
        <div 
          v-for="(testimonial, index) in testimonials" 
          :key="index" 
          class="testimonial-card"
          v-motion
          :initial="{ opacity: 0, y: 50 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: index * 150 } }"
        >
          <div class="quote-mark">"</div>
          <p class="review">{{ testimonial.review }}</p>
          <div class="user-info">
            <div class="user-details">
              <h3 class="user-name">{{ testimonial.name }}</h3>
              <p class="user-role">{{ testimonial.role || "Learner" }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Fixed share story button outside content flow -->
    <button @click="showModal = true" class="add-review-btn">
      <span class="btn-icon">✏️</span>
      <span>Share Your Story</span>
    </button>

    <!-- Fixed modal overlay -->
    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
      <div class="modal-content">
        <button @click="showModal = false" class="close-modal-btn">×</button>
        <h2 class="modal-title">Share Your Experience</h2>
        
        <form @submit.prevent="submitReview" class="review-form">
          <div class="form-group">
            <label for="name">Your Name</label>
            <input type="text" id="name" v-model="newReview.name" placeholder="Enter your name" required />
          </div>
          
          <div class="form-group">
            <label for="role">Your Role</label>
            <input type="text" id="role" v-model="newReview.role" placeholder="Student, Professional, etc. (Optional)" />
          </div>
          
          <div class="form-group">
            <label for="review">Your Review</label>
            <textarea id="review" v-model="newReview.review" placeholder="Share your experience with our platform..." required></textarea>
          </div>
          
          <button type="submit" :disabled="submitting" class="submit-btn">
            <span v-if="submitting">Submitting...</span>
            <span v-else>Submit Review</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TestimonialsSection",
  data() {
    return {
      testimonials: [],
      loading: true,
      submitting: false,
      showModal: false,
      newReview: {
        name: "",
        role: "",
        review: ""
      }
    };
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/reviews/");
        this.testimonials = response.data;
      } catch (error) {
        console.error("Error fetching reviews:", error);
      } finally {
        this.loading = false;
      }
    },
    async submitReview() {
      if (!this.newReview.name || !this.newReview.review) {
        alert("Name and review are required.");
        return;
      }

      this.submitting = true;
      try {
        await axios.post("http://127.0.0.1:8000/api/reviews/add/", this.newReview);
        
        await this.fetchReviews();

        this.newReview.name = "";
        this.newReview.role = "";
        this.newReview.review = "";
        this.showModal = false;
        
        alert("Thank you! Your review has been submitted successfully.");
      } catch (error) {
        console.error("Error submitting review:", error);
        alert("Failed to submit review. Please try again later.");
      } finally {
        this.submitting = false;
      }
    }
  },
  mounted() {
    this.fetchReviews();
  }
};
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap');

/* Base Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.testimonials-section {
  min-height: 100vh;
  background: linear-gradient(135deg, #F0F7FF, #E6F2FF);
  position: relative;
  overflow: hidden;
  padding: 4rem 1rem;
  color: #2D3748;
  font-family: 'Nunito', sans-serif;
  letter-spacing: -0.01em;
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

/* Content Container */
.content-container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 3rem;
  padding: 0 1rem;
}

/* Testimonials Header */
.testimonials-header {
  max-width: 750px;
  margin: 0 auto;
  text-align: center;
  padding-top: 1rem;
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
}

.badge-icon {
  font-size: clamp(1rem, 3vw, 1.25rem);
}

.title {
  font-family: 'Quicksand', sans-serif;
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
  color: #2D3748;
}

.gradient-text-wrapper {
  display: inline-block;
  position: relative;
}

.gradient-text {
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
  position: relative;
}

.gradient-text::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  border-radius: 4px;
}

.description {
  font-size: clamp(1rem, 3vw, 1.25rem);
  font-weight: 400;
  color: #4A5568;
  margin-bottom: 2rem;
  line-height: 1.7;
  letter-spacing: -0.01em;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

/* Loading & No Reviews States */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 3rem;
  text-align: center;
  font-size: 1.125rem;
  color: #3178E6;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(75, 150, 243, 0.2);
  border-top: 4px solid #4B96F3;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.no-reviews {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  font-size: 1.125rem;
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid rgba(75, 150, 243, 0.2);
}

/* Testimonials Grid */
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.testimonial-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  position: relative;
  transition: all 0.3s ease;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(75, 150, 243, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.testimonial-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 35px rgba(75, 150, 243, 0.15);
  border: 1px solid rgba(75, 150, 243, 0.2);
}

.quote-mark {
  position: absolute;
  top: 20px;
  right: 25px;
  font-size: 60px;
  font-family: 'Georgia', serif;
  color: rgba(75, 150, 243, 0.15);
  line-height: 0;
}

.review {
  padding-top: 2rem;
  flex: 1;
  font-size: 1.125rem;
  line-height: 1.7;
  color: #4A5568;
  margin-bottom: 1.5rem;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  border-top: 1px solid rgba(75, 150, 243, 0.1);
  padding-top: 1.25rem;
}

.user-details {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.125rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 0.25rem;
}

.user-role {
  font-size: 0.875rem;
  color: #3178E6;
  font-weight: 500;
}

/* Fixed Add Review Button - Won't scroll with page */
.add-review-btn {
  position: fixed;
  bottom: 2.5rem; /* Adjusted position */
  right: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 50px;
  font-weight: 600;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s ease;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  color: white;
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.3);
  border: none;
  cursor: pointer;
  z-index: 1000;
}

.add-review-btn:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(75, 150, 243, 0.4);
}


.btn-icon {
  font-size: 1.25rem;
}

/* Fixed Modal - Won't scroll with page */
.modal-overlay {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: rgba(45, 55, 72, 0.7);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000 !important; /* Even higher than the button */
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 2.5rem;
  width: 100%;
  max-width: 600px;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  max-height: 90vh;
  overflow-y: auto;
}

.close-modal-btn {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  background: transparent;
  border: none;
  font-size: 1.75rem;
  cursor: pointer;
  color: #4A5568;
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-modal-btn:hover {
  background: #F0F7FF;
  color: #3178E6;
}

.modal-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.875rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: #2D3748;
  text-align: center;
}

/* Form Styles */
.review-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 500;
  color: #4A5568;
  font-size: 0.875rem;
}

.form-group input,
.form-group textarea {
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid #E2E8F0;
  font-size: 1rem;
  font-family: 'Nunito', sans-serif;
  background: #F8FAFC;
  transition: all 0.2s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #4B96F3;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
  background: white;
}

.form-group textarea {
  resize: vertical;
  min-height: 150px;
}

.submit-btn {
  padding: 1rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.125rem;
  transition: all 0.3s ease;
  background: linear-gradient(45deg, #4B96F3, #3178E6);
  color: white;
  box-shadow: 0 4px 15px rgba(75, 150, 243, 0.2);
  border: none;
  cursor: pointer;
  margin-top: 0.5rem;
  font-family: 'Quicksand', sans-serif;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(75, 150, 243, 0.3);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .testimonials-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
}

@media (max-width: 768px) {
  .testimonials-section {
    padding: 3rem 1rem;
  }

  .title {
    font-size: 2.5rem;
  }

  .description {
    font-size: 1.125rem;
  }

  .testimonials-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
  }

  /* Move button to the top right instead of bottom right on mobile */
  .add-review-btn {
    bottom: auto !important;
    top: 7rem !important;
    right: 1.5rem !important;
    padding: 0.75rem 1.25rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .testimonials-section {
    padding: 2rem 0.75rem;
  }

  .content-container {
    padding: 0 0.5rem;
  }

  .title {
    font-size: 2rem;
  }

  .badge {
    font-size: 0.875rem;
    padding: 0.5rem 0.875rem;
  }

  .testimonials-grid {
    grid-template-columns: 1fr;
  }

  .testimonial-card {
    padding: 1.75rem;
  }

  .modal-content {
    padding: 1.75rem;
  }

  .modal-title {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }

  @media (max-width: 768px) {
  .add-review-btn {
    bottom: 6rem; /* Move slightly up to avoid navbar */
    right: 1.5rem;
    padding: 0.75rem 1.25rem;
    font-size: 0.9rem;
  }
}
}

@media (max-width: 360px) {
  .testimonials-section {
    padding: 1.5rem 0.5rem;
  }
  
  .title {
    font-size: 1.75rem;
  }
  
  .description {
    font-size: 0.95rem;
  }
  
  .testimonial-card {
    padding: 1.5rem;
  }
  
  .review {
    font-size: 1rem;
  }
  
  @media (max-width: 480px) {
  .add-review-btn {
    bottom: 6.5rem; /* Move up more to avoid overlapping with navbar */
    right: 1rem;
    padding: 0.6rem 1rem;
    font-size: 0.85rem;
  }
}
}
</style>