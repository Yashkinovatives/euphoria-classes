<template>
  <div class="performance-section">
    <div class="section-header">
      <div class="badge">
        <span class="badge-icon">📊</span>
        <span>Academic Progress</span>
      </div>
      <h2>Performance Overview</h2>
    </div>

    <div class="charts-grid">
      <!-- Subject Performance Chart -->
      <div class="chart-card">
        <h3>Subject Performance</h3>
        <div class="chart-container">
          <canvas ref="subjectChart"></canvas>
        </div>
      </div>

      <!-- Progress Timeline -->
      <div class="chart-card">
        <h3>Progress Timeline</h3>
        <div class="chart-container">
          <canvas ref="progressChart"></canvas>
        </div>
      </div>

      <!-- Detailed Results -->
      <div class="results-card">
        <h3>Recent Assessments</h3>
        <div class="results-list">
          <div 
            v-for="(result, index) in latestResults" 
            :key="index"
            class="result-item"
          >
            <div class="result-info">
              <h4>{{ result.subject }}</h4>
              <p>{{ result.date }}</p>
            </div>
            <div class="result-score">
              <div class="score-value">{{ result.score }}%</div>
              <div class="progress-bar">
                <div class="progress" :style="{ width: `${result.score}%` }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, defineProps } from "vue";
import Chart from "chart.js/auto";

const props = defineProps({
  testResults: {
    type: Array,
    required: true
  }
});

const subjectChart = ref(null);
const progressChart = ref(null);

// Extract subject-wise performance
const subjectPerformance = computed(() => {
  const subjectScores = {};
  props.testResults.forEach(student => {
    student.results?.forEach(result => {
      const subject = result.subject;
      const score = Math.round((result.marks_obtained / result.total_marks) * 100);
      
      if (!subjectScores[subject]) {
        subjectScores[subject] = [];
      }
      subjectScores[subject].push(score);
    });
  });

  // Calculate average score for each subject
  const subjects = Object.keys(subjectScores);
  const scores = subjects.map(subject => {
    const avgScore = subjectScores[subject].reduce((a, b) => a + b, 0) / subjectScores[subject].length;
    return Math.round(avgScore);
  });

  return { subjects, scores };
});

// Extract performance trend over time
const progressTimeline = computed(() => {
  const monthlyScores = {};
  
  props.testResults.forEach(student => {
    student.results?.forEach(result => {
      const date = result.date || "Unknown"; // ✅ Provide fallback value
      const month = date.includes(" ") ? date.split(" ")[0] : date; // ✅ Ensure split() only applies if valid
      const score = Math.round((result.marks_obtained / result.total_marks) * 100);
      
      if (!monthlyScores[month]) {
        monthlyScores[month] = [];
      }
      monthlyScores[month].push(score);
    });
  });

  const months = Object.keys(monthlyScores).sort();
  const scores = months.map(month => {
    const avgScore = monthlyScores[month].reduce((a, b) => a + b, 0) / monthlyScores[month].length;
    return Math.round(avgScore);
  });

  return { months, scores };
});

// Extract latest test results
const latestResults = computed(() => {
  const results = [];
  
  props.testResults.forEach(student => {
    student.results?.forEach(result => {
      results.push({
        subject: result.subject,
        score: Math.round((result.marks_obtained / result.total_marks) * 100),
        date: result.date || "N/A"
      });
    });
  });

  return results.slice(0, 5); // Show the latest 5 results
});

onMounted(() => {
  // Subject Performance Chart
  if (subjectChart.value) {
    new Chart(subjectChart.value, {
      type: "radar",
      data: {
        labels: subjectPerformance.value.subjects,
        datasets: [
          {
            label: "Performance",
            data: subjectPerformance.value.scores,
            backgroundColor: "rgba(124, 58, 237, 0.2)",
            borderColor: "#7c3aed",
            borderWidth: 2,
            pointBackgroundColor: "#7c3aed"
          }
        ]
      },
      options: {
        scales: {
          r: {
            beginAtZero: true,
            max: 100,
            ticks: {
              stepSize: 20
            }
          }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });
  }

  // Progress Timeline Chart
  if (progressChart.value) {
    new Chart(progressChart.value, {
      type: "line",
      data: {
        labels: progressTimeline.value.months,
        datasets: [
          {
            label: "Average Score",
            data: progressTimeline.value.scores,
            borderColor: "#7c3aed",
            tension: 0.4,
            fill: true,
            backgroundColor: "rgba(124, 58, 237, 0.1)"
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            max: 100
          }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });
  }
});
</script>

<style scoped>
.performance-section {
  margin-top: 2rem;
}

.section-header {
  margin-bottom: 2rem;
  text-align: center;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: rgba(139, 92, 246, 0.15);
  border-radius: 100px;
  margin-bottom: 1rem;
  gap: 0.5rem;
  font-weight: 600;
  color: #6d28d9;
}

.badge-icon {
  font-size: 1.25rem;
}

h2 {
  font-family: "Space Grotesk", sans-serif;
  font-size: 2rem;
  color: #1e293b;
  margin: 0;
}

.charts-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.chart-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
}

.chart-container {
  height: 300px;
  position: relative;
}

.results-card {
  grid-column: span 2;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
}

h3 {
  font-family: "Space Grotesk", sans-serif;
  font-size: 1.25rem;
  color: #1e293b;
  margin: 0 0 1.5rem 0;
}
</style>
