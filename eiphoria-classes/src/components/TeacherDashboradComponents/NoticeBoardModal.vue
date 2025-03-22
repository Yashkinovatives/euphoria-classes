<!-- NoticeBoardModal.vue -->
<template>
  <teleport to="body">
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
  </teleport>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, defineEmits } from 'vue';
import axios from 'axios';

const emit = defineEmits(['close', 'update']);

const loading = ref(true);
const notices = ref([]);
const newNotice = ref({
  title: '',
  content: ''
});
const editingNoticeId = ref(null);
const isEditing = ref(false);

// Lock body scrolling when modal is open
onMounted(() => {
  document.documentElement.style.overflow = 'hidden';
  document.body.style.overflow = 'hidden';
  document.body.style.position = 'fixed';
  document.body.style.width = '100%';
  document.body.style.top = `-${window.scrollY}px`;
  fetchNotices();
});

// Restore scrolling when modal is closed
onBeforeUnmount(() => {
  const scrollY = document.body.style.top;
  document.documentElement.style.overflow = '';
  document.body.style.overflow = '';
  document.body.style.position = '';
  document.body.style.width = '';
  document.body.style.top = '';
  window.scrollTo(0, parseInt(scrollY || '0') * -1);
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
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Quicksand:wght@300;400;500;600;700&display=swap");

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999999;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  overflow: hidden !important;
}

.modal-container {
  background-color: white;
  border-radius: 16px;
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  box-shadow: 0 4px 20px rgba(75, 150, 243, 0.2);
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(75, 150, 243, 0.1);
  font-family: "Nunito", sans-serif;
  z-index: 1000000;
  animation: modalFade 0.25s ease;
  overflow: hidden;
}

@keyframes modalFade {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  background-color: white;
  z-index: 10;
  border-top-left-radius: 16px;
  border-top-right-radius: 16px;
  flex-shrink: 0;
}

.modal-header h2 {
  margin: 0;
  font-family: 'Quicksand', sans-serif;
  color: #2D3748;
  font-size: 1.5rem;
  font-weight: 700;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #64748b;
  transition: color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  flex-shrink: 0;
}

.close-btn:hover {
  color: #ef4444;
  background-color: rgba(239, 68, 68, 0.1);
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  flex-grow: 1;
  -webkit-overflow-scrolling: touch;
}

.add-notice-form {
  background-color: rgba(75, 150, 243, 0.05);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.add-notice-form h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2D3748;
  font-family: 'Quicksand', sans-serif;
  font-weight: 700;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #2D3748;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  font-family: 'Nunito', sans-serif;
  font-size: 0.95rem;
  transition: border-color 0.2s ease;
  -webkit-appearance: none;
  font-size: 16px; /* Prevents iOS zoom on focus */
  box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #4B96F3;
  outline: none;
  box-shadow: 0 0 0 3px rgba(75, 150, 243, 0.1);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 1rem;
}

.submit-btn {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(75, 150, 243, 0.2);
}

.submit-btn:disabled {
  background: rgba(75, 150, 243, 0.4);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
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
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.cancel-btn:hover {
  background-color: #e2e8f0;
  transform: translateY(-2px);
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
  border: 3px solid rgba(75, 150, 243, 0.1);
  border-top-color: #3178E6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.notices-list h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2D3748;
  font-family: 'Quicksand', sans-serif;
  font-weight: 700;
}

.no-notices {
  text-align: center;
  padding: 2rem;
  background-color: rgba(75, 150, 243, 0.05);
  border-radius: 12px;
  color: #64748b;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.notice-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.notice-item {
  background-color: white;
  border: 1px solid rgba(75, 150, 243, 0.1);
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 2px 8px rgba(75, 150, 243, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.notice-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(75, 150, 243, 0.12);
}

.notice-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.75rem;
}

.notice-header h4 {
  margin: 0;
  color: #2D3748;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
  flex: 1;
  padding-right: 1rem;
}

.notice-actions {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.edit-btn,
.delete-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  transition: background-color 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.edit-btn {
  color: #3178E6;
}

.delete-btn {
  color: #ef4444;
}

.edit-btn:hover,
.delete-btn:hover {
  background-color: #f1f5f9;
}

.notice-content {
  margin: 0 0 1rem 0;
  color: #4A5568;
  line-height: 1.6;
  white-space: pre-line;
  word-wrap: break-word;
}

.notice-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.875rem;
  color: #64748b;
  flex-wrap: wrap;
  gap: 0.5rem;
}

/* Responsive styles */
@media (max-width: 768px) {
  .modal-container {
    width: 95%;
    max-height: 90vh;
    margin: 0 auto;
  }
  
  .modal-header {
    padding: 1.25rem;
  }
  
  .modal-header h2 {
    font-size: 1.25rem;
  }
  
  .modal-body {
    padding: 1.25rem;
    gap: 1.5rem;
  }
  
  .add-notice-form {
    padding: 1.25rem;
  }
  
  .form-actions {
    flex-direction: column-reverse;
    gap: 0.5rem;
  }
  
  .submit-btn, 
  .cancel-btn {
    width: 100%;
    padding: 0.75rem 1rem;
  }
  
  .notice-meta {
    flex-direction: column;
    gap: 0.5rem;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .modal-overlay {
    align-items: center;
    padding: 0 10px;
  }
  
  .modal-container {
    width: 100%;
    max-height: 85vh;
    border-radius: 20px;
    margin-bottom: 20px;
  }
  
  .modal-header {
    padding: 1rem;
    border-radius: 20px 20px 0 0;
  }
  
  .modal-body {
    padding: 1rem;
    gap: 1.25rem;
  }
  
  .add-notice-form {
    padding: 1rem;
    border-radius: 10px;
  }
  
  .form-group input,
  .form-group textarea {
    padding: 0.7rem;
  }
  
  .notice-item {
    padding: 1rem;
  }
  
  .notice-header {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .notice-actions {
    align-self: flex-end;
  }
  
  .edit-btn,
  .delete-btn {
    padding: 0.6rem;
  }
}

@media (max-width: 360px) {
  .modal-header h2 {
    font-size: 1.1rem;
  }
  
  .add-notice-form h3,
  .notices-list h3 {
    font-size: 1rem;
  }
  
  .notice-header h4 {
    font-size: 1rem;
  }
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .modal-overlay {
    padding-bottom: max(15px, env(safe-area-inset-bottom));
    padding-top: max(15px, env(safe-area-inset-top));
  }
}

/* Height adjustments for landscape mode */
@media (max-height: 600px) and (orientation: landscape) {
  .modal-container {
    max-height: 95vh;
  }
  
  .add-notice-form {
    padding: 1rem;
  }
  
  .form-group {
    margin-bottom: 0.75rem;
  }
  
  .form-group textarea {
    rows: 3;
  }
}
</style>