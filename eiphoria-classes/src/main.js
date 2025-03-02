import { createApp } from 'vue'
import { MotionPlugin } from '@vueuse/motion'
import VueLazyload from 'vue3-lazyload'
import App from './App.vue'
import router from './router'
import VueApexCharts from 'vue3-apexcharts'


const app = createApp(App)

app.use(MotionPlugin)  // Enables animations
app.use(VueLazyload)    // Enables lazy loading for images
app.use(router)
app.use(VueApexCharts)
app.mount('#app')