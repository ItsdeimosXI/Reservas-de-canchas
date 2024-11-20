import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
//AOS
import AOS from 'aos'
import 'aos/dist/aos.css'

AOS.init();
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.mount('#app')
