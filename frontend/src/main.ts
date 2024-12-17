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
//axios config
import custom_axios from './axios'
import UserAuth from './stores/login'


AOS.init();
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.use(custom_axios)

app.mount('#app')
const store = UserAuth()
const token = localStorage.getItem('token') || sessionStorage.getItem('token')
const superuser = localStorage.getItem('superuser')
if (token){
  store.token = token
  store.superuser = superuser || false
}
