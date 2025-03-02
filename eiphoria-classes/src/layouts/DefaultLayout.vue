<template>
    <div>
      <AppHeader />  <!-- Add header here -->
      <main>
        <slot />
      </main>
      <AppFooter />  <!-- Add footer here -->
    </div>
  </template>
  
  <script>
  import AppHeader from '@/components/AppHeader.vue';
  import AppFooter from '@/components/AppFooter.vue';
  
  export default {
    components: { AppHeader, AppFooter }
  };
  </script>
  
  <style scoped>
  main {
    padding: 20px;
  }
  </style>
  