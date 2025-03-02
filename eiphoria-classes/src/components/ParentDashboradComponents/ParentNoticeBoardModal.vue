<!-- ParentNoticeBoardModal.vue -->
<template>
    <div class="modal-overlay">
      <div class="modal-container">
        <div class="modal-header">
          <h2>School Notices</h2>
          <button @click="$emit('close')" class="close-btn">&times;</button>
        </div>
        
        <div class="modal-body">
          <div v-if="loading" class="notice-loader">
            <div class="loader-spinner"></div>
            <p>Loading notices...</p>
          </div>
  
          <!-- Notices List -->
          <div v-else class="notices-list">
            <div v-if="notices.length === 0" class="no-notices">
              <p>No notices available at this time.</p>
            </div>
            
            <div v-else class="notice-items">
              <div v-for="notice in notices" :key="notice.id" class="notice-item">
                <div class="notice-header">
                  <h4>{{ notice.title }}</h4>
                </div>
                <p class="notice-content">{{ notice.content }}</p>
                <div class="notice-meta">
                  <span class="notice-author">Posted by: {{ notice.created_by__first_name }}</span>
                  <span class="notice-date">{{ formatDate(notice.created_at) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted,defineEmits } from 'vue';
  import axios from 'axios';
  
  
defineEmits(['close']);
  
  const loading = ref(true);
  const notices = ref([]);
  
  onMounted(async () => {
    await fetchNotices();
  });
  
  const fetchNotices = async () => {
    try {
      loading.value = true;
      const token = localStorage.getItem('access_token');
      const response = await axios.get('http://127.0.0.1:8000/api/notices/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      notices.value = response.data.notices;
    } catch (error) {
      console.error('Error fetching notices:', error);
    } finally {
      loading.value = false;
    }
  };
  
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-container {
    background-color: white;
    border-radius: 16px;
    width: 90%;
    max-width: 800px;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
  }
  
  .modal-header {
    padding: 1.5rem;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    background-color: white;
    z-index: 10;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  
  .modal-header h2 {
    margin: 0;
    font-family: 'Space Grotesk', sans-serif;
    color: #1e293b;
    font-size: 1.5rem;
  }
  
  .close-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
    transition: color 0.2s ease;
  }
  
  .close-btn:hover {
    color: #ef4444;
  }
  
  .modal-body {
    padding: 1.5rem;
    overflow-y: auto;
  }
  
  .notice-loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 200px;
  }
  
  .loader-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #e9d5ff;
    border-top-color: #7c3aed;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
  
  .no-notices {
    text-align: center;
    padding: 2rem;
    background-color: #f8fafc;
    border-radius: 12px;
    color: #64748b;
  }
  
  .notice-items {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .notice-item {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.25rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .notice-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .notice-header {
    margin-bottom: 0.75rem;
  }
  
  .notice-header h4 {
    margin: 0;
    color: #1e293b;
    font-size: 1.1rem;
    font-weight: 600;
  }
  
  .notice-content {
    margin-bottom: 1rem;
    color: #334155;
    line-height: 1.5;
    white-space: pre-line;
  }
  
  .notice-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.875rem;
    color: #64748b;
  }
  
  @media (max-width: 768px) {
    .modal-container {
      width: 95%;
      max-height: 95vh;
    }
    
    .modal-header h2 {
      font-size: 1.25rem;
    }
    
    .notice-meta {
      flex-direction: column;
      gap: 0.25rem;
    }
  }
  </style>