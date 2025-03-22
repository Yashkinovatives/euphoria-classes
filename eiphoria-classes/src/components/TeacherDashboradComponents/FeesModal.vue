<template>
  <teleport to="body">
    <div class="modal-backdrop">
      <div class="modal-content">
        <div class="modal-header">
          <h3>Fees Management - {{ student.name }}</h3>
          <button @click="$emit('close')" class="close-btn">×</button>
        </div>

        <div class="modal-body">
          <!-- Success Message -->
          <div v-if="successMessage" class="success-message">
            {{ successMessage }}
          </div>

          <div class="fees-summary">
            <div class="summary-item">
              <span>Total Fees:</span>
              <span>₹{{ feeRecord?.total_fees || 0 }}</span>
            </div>
            <div class="summary-item">
              <span>Remaining Fees:</span>
              <span>₹{{ feeRecord?.remaining_fees || 0 }}</span>
            </div>
          </div>

          <!-- Set Total Fees Section -->
          <div class="fees-section">
            <h4>Set Total Fees</h4>
            <div class="input-group">
              <input 
                v-model="totalFees" 
                type="number" 
                placeholder="Enter total fees amount"
                class="fees-input"
                :disabled="isTotalFeesSet"
              />
              <button 
                @click="setTotalFees" 
                :disabled="!totalFees || isTotalFeesSet"
                class="btn btn-primary"
              >
                Set Total Fees
              </button>
            </div>
            <p v-if="isTotalFeesSet" class="help-text">Total fees can only be set once</p>
          </div>

          <!-- Add Monthly Payment Section -->
          <div class="fees-section">
            <h4>Add Monthly Payment</h4>
            <div class="payment-form">
              <select v-model="selectedMonth" class="month-select">
                <option value="">Select Month</option>
                <option 
                  v-for="month in availableMonths" 
                  :key="month"
                  :value="month"
                >
                  {{ month }}
                </option>
              </select>
              <input 
                v-model="monthlyPayment" 
                type="number" 
                placeholder="Enter payment amount"
                class="fees-input"
              />
              <button 
                @click="addMonthlyPayment"
                :disabled="!selectedMonth || !monthlyPayment"
                class="btn btn-primary"
              >
                Add Payment
              </button>
            </div>
          </div>

          <!-- Payment History -->
          <div class="fees-section">
            <h4>Payment History</h4>
            <div class="payment-history">
              <div v-if="payments.length === 0" class="no-payments">
                No payments recorded yet
              </div>
              <div 
                v-else
                v-for="payment in payments" 
                :key="payment.id" 
                class="payment-record"
              >
                <span class="payment-month">{{ payment.month }}</span>
                <span class="payment-amount">₹{{ payment.amount_paid }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, defineProps, defineEmits, computed } from 'vue';
import axios from 'axios';

const props = defineProps({
  student: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['close', 'update']);

const totalFees = ref('');
const monthlyPayment = ref('');
const selectedMonth = ref('');
const feeRecord = ref(null);
const payments = ref([]);
const successMessage = ref('');
const isTotalFeesSet = computed(() => feeRecord.value?.total_fees > 0);

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

const availableMonths = computed(() => {
  const paidMonths = new Set(payments.value.map(p => p.month));
  return months.filter(month => !paidMonths.has(month));
});

// Lock body scrolling when modal is open
onMounted(() => {
  document.documentElement.style.overflow = 'hidden';
  document.body.style.overflow = 'hidden';
  document.body.style.position = 'fixed';
  document.body.style.width = '100%';
  document.body.style.top = `-${window.scrollY}px`;
  fetchFeeData();
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

// ✅ Fetch Fee Data from Teacher API
const fetchFeeData = async () => {
  try {
    const token = localStorage.getItem('access_token');
    const response = await axios.get(`http://127.0.0.1:8000/api/teacher/student-fees/${props.student.id}/`, {
      headers: { Authorization: `Bearer ${token}` }
    });

    feeRecord.value = {
      total_fees: response.data.total_fees,
      remaining_fees: response.data.remaining_fees
    };
    payments.value = response.data.monthly_payments || [];
  } catch (error) {
    console.error('Error fetching fee data:', error);
  }
};

// ✅ Set Total Fees
const setTotalFees = async () => {
  try {
    const token = localStorage.getItem('access_token');
    await axios.post('http://127.0.0.1:8000/api/teacher/set-total-fees/', {
      student_id: props.student.id,
      total_fees: totalFees.value
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    successMessage.value = "Total fees set successfully!";
    setTimeout(() => {
      successMessage.value = "";
    }, 3000);
    
    await fetchFeeData();
    totalFees.value = '';
    emit('update');
  } catch (error) {
    console.error('Error setting total fees:', error);
  }
};

// ✅ Add Monthly Fee Payment
const addMonthlyPayment = async () => {
  try {
    const token = localStorage.getItem('access_token');
    await axios.post('http://127.0.0.1:8000/api/teacher/add-monthly-fee/', {
      student_id: props.student.id,
      month: selectedMonth.value,
      amount_paid: monthlyPayment.value
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    successMessage.value = "Monthly fee uploaded successfully!";
    setTimeout(() => {
      successMessage.value = "";
    }, 3000);
    
    await fetchFeeData();
    selectedMonth.value = '';
    monthlyPayment.value = '';
    emit('update');
  } catch (error) {
    console.error('Error adding monthly payment:', error);
  }
};
</script>


<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999999;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  overflow: hidden !important;
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  position: relative;
  margin: 0 auto;
  box-shadow: 0 4px 20px rgba(75, 150, 243, 0.1);
  border: 1px solid rgba(75, 150, 243, 0.1);
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
  background: white;
  z-index: 5;
  border-radius: 16px 16px 0 0;
  flex-shrink: 0;
}

.modal-header h3 {
  margin: 0;
  color: #2D3748;
  font-family: 'Quicksand', sans-serif;
  font-size: 1.25rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: 700;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #64748b;
  cursor: pointer;
  padding: 0;
  margin-left: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 32px;
  min-height: 32px;
  flex-shrink: 0;
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  overflow-x: hidden;
  flex-grow: 1;
  -webkit-overflow-scrolling: touch;
}

.success-message {
  background-color: rgba(75, 150, 243, 0.15);
  color: #3178E6;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 600;
  animation: fadeIn 0.3s;
  border: 1px solid rgba(75, 150, 243, 0.2);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.fees-summary {
  background: rgba(75, 150, 243, 0.05);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.fees-section {
  margin-bottom: 2rem;
}

.fees-section h4 {
  color: #2D3748;
  margin-bottom: 1rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.help-text {
  color: #64748b;
  font-size: 0.85rem;
  margin-top: 0.5rem;
  font-style: italic;
}

.input-group {
  display: flex;
  gap: 1rem;
}

.fees-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  font-size: 16px; /* Prevents iOS zoom on focus */
  -webkit-appearance: none; /* Better appearance on iOS */
}

.fees-input:disabled {
  background-color: #f1f5f9;
  cursor: not-allowed;
}

.payment-form {
  display: grid;
  gap: 1rem;
}

.month-select {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(75, 150, 243, 0.2);
  border-radius: 8px;
  background-color: white;
  font-size: 16px;
  font-family: inherit;
  color: #2D3748;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%234B96F3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 2.5rem;
  transition: all 0.2s ease;
  box-sizing: border-box;
  height: 3.25rem;
}

.payment-history {
  background: rgba(75, 150, 243, 0.05);
  border-radius: 12px;
  padding: 1rem;
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid rgba(75, 150, 243, 0.1);
}

.payment-record {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem;
  border-bottom: 1px solid rgba(75, 150, 243, 0.1);
}

.payment-record:last-child {
  border-bottom: none;
}

.no-payments {
  text-align: center;
  color: #64748b;
  padding: 1rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  white-space: nowrap;
  text-align: center;
  height: 3.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-primary {
  background: linear-gradient(135deg, #4B96F3, #3178E6);
  color: white;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Touch-friendly adjustment for all interactive elements */
.btn, .close-btn, select, input {
  touch-action: manipulation;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .modal-content {
    width: 95%;
    max-height: 85vh;
  }
  
  .modal-header {
    padding: 1.25rem;
  }
  
  .modal-body {
    padding: 1.25rem;
  }
  
  .fees-summary {
    padding: 1.25rem;
  }
  
  .payment-history {
    max-height: 180px;
  }
}

@media (max-width: 640px) {
  .modal-content {
    width: 100%;
    max-height: 90vh;
    border-radius: 12px;
  }
  
  .modal-header {
    padding: 1rem;
    border-radius: 12px 12px 0 0;
  }
  
  .modal-header h3 {
    font-size: 1.15rem;
    max-width: 75%;
  }
  
  .modal-body {
    padding: 1rem;
  }
  
  .fees-summary {
    padding: 1rem;
    margin-bottom: 1.25rem;
  }
  
  .fees-section {
    margin-bottom: 1.5rem;
  }
  
  .input-group {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .btn {
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 0.95rem;
  }
  
  .payment-history {
    padding: 0.75rem;
  }
  
  .payment-record {
    padding: 0.6rem;
  }
}

@media (max-width: 480px) {
  .modal-backdrop {
    padding: 0 10px;
    align-items: center;
  }
  
  .modal-content {
    max-height: 85vh;
    border-radius: 20px;
    margin-bottom: 20px;
  }
  
  .modal-header {
    padding: 0.9rem;
    border-radius: 20px 20px 0 0;
  }
  
  .modal-header h3 {
    font-size: 1.1rem;
  }
  
  .modal-body {
    padding: 0.9rem;
  }
  
  .fees-section h4 {
    font-size: 1rem;
  }
  
  .payment-history {
    max-height: 160px;
  }
  
  .fees-input, .month-select {
    padding: 0.7rem 0.9rem;
  }
  
  /* Better tap targets on small screens */
  .payment-record {
    padding: 0.8rem 0.5rem;
  }
}

/* iOS safe areas */
@supports (padding: max(0px)) {
  .modal-backdrop {
    padding-bottom: max(15px, env(safe-area-inset-bottom));
    padding-top: max(15px, env(safe-area-inset-top));
  }
}

/* Height adjustments for very small devices */
@media (max-height: 600px) {
  .modal-content {
    max-height: 92vh;
  }
  
  .payment-history {
    max-height: 120px;
  }
  
  .fees-section {
    margin-bottom: 1.25rem;
  }
}
</style>