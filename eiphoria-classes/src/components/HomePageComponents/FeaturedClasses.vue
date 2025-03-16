<template>
  <section class="pathways-section">
    <!-- Animated Background Elements -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>
    
    <div class="container">
      <div class="section-header" v-motion 
           :initial="{ opacity: 0, y: 30 }" 
           :enter="{ opacity: 1, y: 0, transition: { duration: 800 } }">
        <h2 class="section-title">
          Learning <span class="gradient-text">Pathways</span>
        </h2>
        <p class="section-subtitle">
          Structured learning journeys designed to take you from beginner to expert
        </p>
      </div>
      
      <div class="pathways-container">
        <div v-for="(pathway, index) in pathways" 
             :key="pathway.id" 
             class="pathway-card"
             v-motion 
             :initial="{ opacity: 0, x: index % 2 === 0 ? -40 : 40 }" 
             :enter="{ opacity: 1, x: 0, transition: { duration: 800, delay: 200 + (index * 150) } }">
          
          <div class="pathway-content">
            <div class="pathway-icon-container">
              <div class="pathway-icon" v-html="pathway.icon"></div>
            </div>
            
            <div class="pathway-details">
              <h3 class="pathway-title">{{ pathway.title }}</h3>
              <p class="pathway-description">{{ pathway.description }}</p>
              
              <div class="pathway-stats">
                <div class="stat-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                  </svg>
                  <span>{{ pathway.courses }} Courses</span>
                </div>
                
                <div class="stat-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  <span>{{ pathway.duration }}</span>
                </div>
                
                <div class="stat-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                  </svg>
                  <span>{{ pathway.students }}+ Students</span>
                </div>
              </div>
              
              <ul class="pathway-modules">
                <li v-for="(module, moduleIndex) in pathway.modules" :key="moduleIndex" class="module-item">
                  <div class="module-checkmark">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </div>
                  <span>{{ module }}</span>
                </li>
              </ul>
              
              <div class="pathway-actions">
                <router-link :to="`/pathway/${pathway.id}`" class="btn-explore">
                  Explore Pathway
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </router-link>
              </div>
            </div>
          </div>
          
          <div class="pathway-progress-bar">
            <div class="progress-label">
              <span class="progress-text">Beginner</span>
              <span class="progress-text">Advanced</span>
            </div>
            <div class="progress-track">
              <div class="progress-nodes">
                <div class="node" v-for="n in 4" :key="n" :class="{ 'active': n <= pathway.progressNodes }"></div>
              </div>
              <div class="progress-line">
                <div class="progress-fill" :style="{ width: `${(pathway.progressNodes - 1) * 33.33}%` }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="cta-container" v-motion 
           :initial="{ opacity: 0, y: 20 }" 
           :enter="{ opacity: 1, y: 0, transition: { duration: 600, delay: 800 } }">
        <router-link to="/pathways" class="btn-all-pathways">
          View All Learning Paths
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 12h14M12 5l7 7-7 7"/>
          </svg>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
const pathways = [
  {
    id: 1,
    title: 'Web Development Mastery',
    description: 'A comprehensive journey from HTML basics to building full-stack applications with modern frameworks',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
    courses: 8,
    duration: '6 months',
    students: 2450,
    progressNodes: 4,
    modules: [
      'HTML, CSS & JavaScript Fundamentals',
      'Responsive Design & CSS Frameworks',
      'Modern JavaScript & API Integration',
      'React/Vue Frontend Development'
    ]
  },
  {
    id: 2,
    title: 'UI/UX Design Professional',
    description: 'Learn to create beautiful, intuitive interfaces and seamless user experiences that delight customers',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle><line x1="21.17" y1="8" x2="12" y2="8"></line><line x1="3.95" y1="6.06" x2="8.54" y2="14"></line><line x1="10.88" y1="21.94" x2="15.46" y2="14"></line></svg>',
    courses: 6,
    duration: '4 months',
    students: 1870,
    progressNodes: 3,
    modules: [
      'Design Principles & Color Theory',
      'Wireframing & Prototyping',
      'User Research & Testing',
      'Design Systems & Component Libraries'
    ]
  },
  {
    id: 3,
    title: 'Data Science & Analytics',
    description: 'Master the tools and techniques to analyze complex data and extract meaningful insights for decision making',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg>',
    courses: 7,
    duration: '5 months',
    students: 1250,
    progressNodes: 2,
    modules: [
      'Python for Data Analysis',
      'Statistical Methods & Visualization',
      'Machine Learning Fundamentals',
      'Big Data & Cloud Computing'
    ]
  }
];
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.pathways-section {
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.section-header {
  text-align: center;
  margin-bottom: 3.5rem;
}

.section-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
  color: #1e293b;
}

.gradient-text {
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
}

.section-subtitle {
  font-size: 1.25rem;
  color: #475569;
  max-width: 600px;
  margin: 0 auto;
}

.pathways-container {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  margin-bottom: 3rem;
}

.pathway-card {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 12px 30px rgba(139, 92, 246, 0.08);
  transition: all 0.3s ease;
  padding: 2rem;
}

.pathway-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 40px rgba(139, 92, 246, 0.12);
}

.pathway-content {
  display: flex;
  gap: 2rem;
}

.pathway-icon-container {
  flex-shrink: 0;
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: linear-gradient(135deg, #7C3AED, #C084FC);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 20px rgba(139, 92, 246, 0.2);
}

.pathway-details {
  flex: 1;
}

.pathway-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.pathway-description {
  font-size: 1.125rem;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.pathway-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #6b7280;
  font-size: 0.95rem;
}

.stat-item svg {
  color: #7C3AED;
}

.pathway-modules {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem 0;
}

.module-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
  font-size: 1.05rem;
  color: #334155;
}

.module-checkmark {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(139, 92, 246, 0.1);
  color: #7C3AED;
}

.pathway-actions {
  display: flex;
  margin-top: 1rem;
}

.btn-explore {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(45deg, #7C3AED, #A855F7);
  color: white;
  font-weight: 600;
  border-radius: 100px;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.15);
}

.btn-explore:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(139, 92, 246, 0.25);
}

.btn-explore svg {
  transition: transform 0.3s ease;
}

.btn-explore:hover svg {
  transform: translateX(3px);
}

.pathway-progress-bar {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(139, 92, 246, 0.1);
}

.progress-label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.progress-text {
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
}

.progress-track {
  position: relative;
  height: 32px;
}

.progress-nodes {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 2;
}

.node {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #e9d5ff;
  position: relative;
  transition: all 0.3s ease;
}

.node.active {
  background: #7C3AED;
  box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.2);
}

.progress-line {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  width: 100%;
  height: 4px;
  background: #e9d5ff;
  border-radius: 4px;
  z-index: 1;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(45deg, #7C3AED, #C084FC);
  border-radius: 4px;
  transition: width 0.5s ease;
}

.cta-container {
  text-align: center;
  margin-top: 2rem;
}

.btn-all-pathways {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 2rem;
  background: linear-gradient(45deg, #7C3AED, #A855F7);
  color: white;
  font-weight: 600;
  border-radius: 100px;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(139, 92, 246, 0.2);
}

.btn-all-pathways:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(139, 92, 246, 0.3);
}

.btn-all-pathways svg {
  transition: transform 0.3s ease;
}

.btn-all-pathways:hover svg {
  transform: translateX(3px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .pathways-section {
    padding: 4rem 0;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .section-subtitle {
    font-size: 1.125rem;
  }
  
  .pathway-content {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .pathway-icon-container {
    margin: 0 auto;
  }
  
  .pathway-title {
    text-align: center;
  }
  
  .pathway-description {
    text-align: center;
  }
  
  .pathway-stats {
    justify-content: center;
  }
  
  .pathway-actions {
    justify-content: center;
  }
  
  .container {
    padding: 0 1.5rem;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 1.75rem;
  }
  
  .pathway-stats {
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
  }
}
</style>
