<template>
    <div class="modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h2>View Uploaded Results</h2>
          <button @click="$emit('close')" class="close-modal-btn">&times;</button>
        </div>
  
        <div class="modal-body">
          <div v-if="loading" class="loading-section">
            <div class="loader"></div>
            <p>Loading your uploaded results...</p>
          </div>
  
          <div v-else-if="uploadedResults.length === 0" class="no-results">
            <p>No results uploaded yet.</p>
          </div>
  
          <div v-else class="results-container">
            <div 
              v-for="result in uploadedResults" 
              :key="result.id"
              class="result-card"
            >
              <h3>{{ result.student_name }}</h3>
              <p><strong>Semester:</strong> {{ result.semester }} ({{ result.year }})</p>
              <p><strong>Uploaded On:</strong> {{ formatDate(result.uploaded_at) }}</p>
  
              <table class="results-table">
                <thead>
                  <tr>
                    <th>Subject</th>
                    <th>Marks</th>
                    <th>Total</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="subject in result.subjects" :key="subject.subject">
                    <td>{{ subject.subject }}</td>
                    <td>{{ subject.marks_obtained }}</td>
                    <td>{{ subject.total_marks }}</td>
                  </tr>
                </tbody>
              </table>
  
              <a v-if="result.document_url" :href="result.document_url" target="_blank" class="view-document">
                📄 View Uploaded Document
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import axios from "axios";
  
  const uploadedResults = ref([]);
  const loading = ref(true);
  
  const fetchUploadedResults = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/parent/view-uploaded-results/", {
        headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` }
      });
      uploadedResults.value = response.data.uploaded_results || [];
    } catch (error) {
      console.error("Error fetching uploaded results:", error);
    } finally {
      loading.value = false;
    }
  };
  
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString();
  };
  
  onMounted(() => {
    fetchUploadedResults();
  });
  </script>
  
  <style scoped>
  /* 🔹 Modal Overlay */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  /* 🔹 Modal Box */
  .modal-content {
    background: white;
    width: 90%;
    max-width: 600px;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    animation: fadeIn 0.3s;
    max-height: 80vh;
    overflow-y: auto;
  }
  
  /* 🔹 Modal Header */
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #f3f4f6;
    padding-bottom: 10px;
  }
  
  .modal-header h2 {
    font-size: 1.5rem;
    color: #333;
  }
  
  .close-modal-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #888;
  }
  
  .close-modal-btn:hover {
    color: #333;
  }
  
  /* 🔹 Loading Section */
  .loading-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }
  
  .loader {
    width: 40px;
    height: 40px;
    border: 3px solid rgba(0, 0, 0, 0.1);
    border-top-color: #4f46e5;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 10px;
  }
  
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  
  /* 🔹 No Results */
  .no-results {
    text-align: center;
    color: #6b7280;
    font-size: 1rem;
    padding: 20px;
  }
  
  /* 🔹 Results Container */
  .results-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 10px;
  }
  
  /* 🔹 Individual Result Card */
  .result-card {
    background: #f9fafb;
    padding: 15px;
    border-radius: 8px;
    border-left: 5px solid #4f46e5;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .result-card h3 {
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 5px;
  }
  
  .result-card p {
    font-size: 0.9rem;
    color: #555;
    margin: 3px 0;
  }
  
  /* 🔹 Results Table */
  .results-table {
    width: 100%;
    margin-top: 10px;
    border-collapse: collapse;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .results-table th,
  .results-table td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .results-table th {
    background: #4f46e5;
    color: white;
  }
  
  .results-table tr:hover {
    background: #f3f4f6;
  }
  
  /* 🔹 View Document Link */
  .view-document {
    display: inline-block;
    margin-top: 10px;
    text-decoration: none;
    background: #4f46e5;
    color: white;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: 0.3s;
  }
  
  .view-document:hover {
    background: #3730a3;
  }
  
  /* 🔹 Responsive */
  @media (max-width: 480px) {
    .modal-content {
      width: 95%;
      max-width: 90%;
    }
  
    .results-table th,
    .results-table td {
      padding: 6px;
      font-size: 0.85rem;
    }
  }
  </style>
  