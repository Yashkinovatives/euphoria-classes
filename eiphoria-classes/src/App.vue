<template>
  <div id="app">
    <AppHeader />
    <main>
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  components: { AppHeader, AppFooter },
};
</script>

<style>
/* Remove unwanted margins & overflow */
html, body {
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Prevent horizontal scrolling */
  width: 100%;
}

/* Full-height layout */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Allow content to push footer down */
main {
  flex: 1;
  width: 100%;
  overflow-x: hidden; /* Avoid horizontal scroll */
}
</style>
