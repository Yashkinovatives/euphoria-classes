# FeeStatus.vue
<template>
  <div class="fee-status-section">
    <div class="section-header">
      <div class="title-badge">
        <span class="badge-icon">💰</span>
        <h2>Fee Status</h2>
      </div>
    </div>

    <div v-if="!feeStatus || feeStatus.length === 0" class="no-data">
      <p>No fee information available yet</p>
    </div>

    <div v-else class="fee-cards">
      <div v-for="status in feeStatus" :key="status.student_name" class="fee-card">
        <div class="student-info">
          <div class="student-avatar">
            {{ status.student_name[0] }}
          </div>
          <div class="student-details">
            <h3>{{ status.student_name }}</h3>
            <p>{{ status.class_section }}</p>
          </div>
        </div>

        <div class="fee-overview">
          <div class="fee-stat">
            <span class="stat-label">Total Fees</span>
            <span class="stat-value">₹{{ status.total_fees }}</span>
          </div>
          <div class="fee-stat">
            <span class="stat-label">Remaining</span>
            <span class="stat-value remaining">₹{{ status.remaining_fees }}</span>
          </div>
          <div class="fee-progress">
            <div 
              class="progress-bar" 
              :style="{ width: calculateProgress(status.total_fees, status.remaining_fees) + '%' }"
            ></div>
          </div>
        </div>

        <div class="payment-history">
          <h4>Payment History</h4>
          <div class="payment-list">
            <div v-if="!status.monthly_payments || status.monthly_payments.length === 0" class="no-payments">
              No payments recorded yet
            </div>
            <div 
              v-else
              v-for="payment in status.monthly_payments" 
              :key="payment.month"
              class="payment-item"
            >
              <div class="payment-details">
                <span class="payment-month">{{ payment.month }}</span>
                <span class="payment-date">{{ formatDate(payment.payment_date) }}</span>
              </div>
              <span class="payment-amount">₹{{ payment.amount_paid }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  feeStatus: {
    type: Array,
    required: true,
    default: () => []
  }
});

const calculateProgress = (total, remaining) => {
  if (!total) return 0;
  const paid = total - remaining;
  return (paid / total) * 100;
};

const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  
  try {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  } catch (error) {
    console.error('Error formatting date:', error);
    return 'Invalid date';
  }
};
</script>

<style scoped>
.fee-status-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.1);
  margin-bottom: 2rem;
}

.no-data {
  text-align: center;
  padding: 2rem;
  color: #64748b;
  font-size: 1rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 12px;
  margin: 1rem 0;
}

.section-header {
  margin-bottom: 1.5rem;
}

.title-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.badge-icon {
  font-size: 1.5rem;
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.5rem;
  margin: 0;
  color: #1e293b;
}

.fee-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.fee-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(139, 92, 246, 0.1);
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.25rem;
}

.student-details h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #1e293b;
}

.student-details p {
  margin: 0.25rem 0 0;
  font-size: 0.9rem;
  color: #64748b;
}

.fee-overview {
  padding: 1rem;
  background: #f8f7ff;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.fee-stat {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #64748b;
  font-size: 0.9rem;
}

.stat-value {
  font-weight: 600;
  color: #1e293b;
}

.stat-value.remaining {
  color: #7c3aed;
}

.fee-progress {
  height: 6px;
  background: rgba(139, 92, 246, 0.1);
  border-radius: 3px;
  overflow: hidden;
  margin-top: 1rem;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #7c3aed, #a855f7);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.payment-history h4 {
  font-size: 1rem;
  color: #1e293b;
  margin: 0 0 1rem;
}

.payment-list {
  display: grid;
  gap: 0.75rem;
}

.payment-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 8px;
}

.payment-details {
  display: flex;
  flex-direction: column;
}

.payment-month {
  font-weight: 500;
  color: #1e293b;
}

.payment-date {
  font-size: 0.8rem;
  color: #64748b;
}

.payment-amount {
  font-weight: 600;
  color: #10b981;
}

.no-payments {
  text-align: center;
  padding: 1rem;
  color: #64748b;
  font-size: 0.9rem;
  background: rgba(139, 92, 246, 0.05);
  border-radius: 8px;
}

@media (max-width: 768px) {
  .fee-status-section {
    padding: 1rem;
  }

  .fee-cards {
    grid-template-columns: 1fr;
  }
}
</style>