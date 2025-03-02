<!-- NoticeBoardModal.vue -->
<template>
    <div class="modal-overlay">
      <div class="modal-container">
        <div class="modal-header">
          <h2>Notice Board</h2>
          <button @click="$emit('close')" class="close-btn">&times;</button>
        </div>
        
        <div class="modal-body">
          <!-- Add Notice Form (Only for teachers) -->
          <div class="add-notice-form">
            <h3>{{ isEditing ? 'Update Notice' : 'Add New Notice' }}</h3>
            <div class="form-group">
              <label for="noticeTitle">Title</label>
              <input 
                id="noticeTitle" 
                v-model="newNotice.title" 
                type="text" 
                placeholder="Enter notice title"
                required
              >
            </div>
            <div class="form-group">
              <label for="noticeContent">Content</label>
              <textarea 
                id="noticeContent" 
                v-model="newNotice.content" 
                placeholder="Enter notice content" 
                rows="4"
                required
              ></textarea>
            </div>
            <div class="form-actions">
              <button 
                v-if="isEditing" 
                @click="cancelEdit" 
                class="cancel-btn"
              >
                Cancel
              </button>
              <button 
                @click="isEditing ? updateNotice() : addNotice()" 
                class="submit-btn"
                :disabled="!newNotice.title || !newNotice.content"
              >
                {{ isEditing ? 'Update' : 'Add' }} Notice
              </button>
            </div>
          </div>
  
          <div v-if="loading" class="notice-loader">
            <div class="loader-spinner"></div>
            <p>Loading notices...</p>
          </div>
  
          <!-- Notices List -->
          <div v-else class="notices-list">
            <h3>All Notices</h3>
            
            <div v-if="notices.length === 0" class="no-notices">
              <p>No notices available. Add your first notice!</p>
            </div>
            
            <div v-else class="notice-items">
              <div v-for="notice in notices" :key="notice.id" class="notice-item">
                <div class="notice-header">
                  <h4>{{ notice.title }}</h4>
                  <div class="notice-actions">
                    <button @click="editNotice(notice)" class="edit-btn">
                      <span class="edit-icon">✏️</span>
                    </button>
                    <button @click="deleteNotice(notice.id)" class="delete-btn">
                      <span class="delete-icon">🗑️</span>
                    </button>
                  </div>
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
  import { ref, onMounted, defineEmits,emit} from 'vue';
  import axios from 'axios';
  
  defineEmits(['close', 'update']);
  
  const loading = ref(true);
  const notices = ref([]);
  const newNotice = ref({
    title: '',
    content: ''
  });
  const editingNoticeId = ref(null);
  const isEditing = ref(false);
  
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
  
  const addNotice = async () => {
    try {
      const token = localStorage.getItem('access_token');
      await axios.post('http://127.0.0.1:8000/api/teacher/add-notice/', {
        title: newNotice.value.title,
        content: newNotice.value.content
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      // Reset form and refresh notices
      newNotice.value = { title: '', content: '' };
      await fetchNotices();
      emit('update');
    } catch (error) {
      console.error('Error adding notice:', error);
    }
  };
  
  const editNotice = (notice) => {
    newNotice.value = {
      title: notice.title,
      content: notice.content
    };
    editingNoticeId.value = notice.id;
    isEditing.value = true;
  };
  
  const cancelEdit = () => {
    newNotice.value = { title: '', content: '' };
    editingNoticeId.value = null;
    isEditing.value = false;
  };
  
  const updateNotice = async () => {
    try {
      const token = localStorage.getItem('access_token');
      await axios.put(`http://127.0.0.1:8000/api/teacher/update-notice/${editingNoticeId.value}/`, {
        title: newNotice.value.title,
        content: newNotice.value.content
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      // Reset form and refresh notices
      cancelEdit();
      await fetchNotices();
      emit('update');
    } catch (error) {
      console.error('Error updating notice:', error);
    }
  };
  
  const deleteNotice = async (noticeId) => {
    if (!confirm('Are you sure you want to delete this notice?')) return;
    
    try {
      const token = localStorage.getItem('access_token');
      await axios.delete(`http://127.0.0.1:8000/api/teacher/delete-notice/${noticeId}/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      await fetchNotices();
      emit('update');
    } catch (error) {
      console.error('Error deleting notice:', error);
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
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  
  .add-notice-form {
    background-color: #f8fafc;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
  }
  
  .add-notice-form h3 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: #334155;
    font-family: 'Space Grotesk', sans-serif;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #334155;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    transition: border-color 0.2s ease;
  }
  
  .form-group input:focus,
  .form-group textarea:focus {
    border-color: #8b5cf6;
    outline: none;
  }
  
  .form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.75rem;
    margin-top: 1rem;
  }
  
  .submit-btn {
    padding: 0.75rem 1.5rem;
    background-color: #8b5cf6;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  
  .submit-btn:hover {
    background-color: #7c3aed;
  }
  
  .submit-btn:disabled {
    background-color: #c4b5fd;
    cursor: not-allowed;
  }
  
  .cancel-btn {
    padding: 0.75rem 1.5rem;
    background-color: #f1f5f9;
    color: #64748b;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .cancel-btn:hover {
    background-color: #e2e8f0;
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
  
  .notices-list h3 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: #334155;
    font-family: 'Space Grotesk', sans-serif;
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
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
  }
  
  .notice-header h4 {
    margin: 0;
    color: #1e293b;
    font-size: 1.1rem;
  }
  
  .notice-actions {
    display: flex;
    gap: 0.5rem;
  }
  
  .edit-btn,
  .delete-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 4px;
    transition: background-color 0.2s ease;
  }
  
  .edit-btn {
    color: #0ea5e9;
  }
  
  .delete-btn {
    color: #ef4444;
  }
  
  .edit-btn:hover,
  .delete-btn:hover {
    background-color: #f1f5f9;
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
      font-size: in1.25rem;
    }
    
    .notice-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.5rem;
    }
    
    .notice-actions {
      align-self: flex-end;
    }
    
    .notice-meta {
      flex-direction: column;
      gap: 0.25rem;
    }
  }
  </style>