import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './styles/main.css'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// 初始化状态
import { useAuthStore } from './stores'
const authStore = useAuthStore()
authStore.checkAuth()

app.mount('#app') 