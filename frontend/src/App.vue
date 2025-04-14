// Start of Selection
<template>
  <!-- 
    这是App.vue的主要模板部分，包含页面的整体布局和导航栏以及主要内容的区域。
    使用了Tailwind CSS的一些类（如min-h-screen、bg-gray-100、max-w-7xl等）来控制布局和样式。
  -->
  <div class="min-h-screen bg-gray-50">
    <!--
      导航栏部分，使用了bg-white和shadow-sm等Tailwind CSS类名来设置背景和阴影效果。
    -->
    <nav class="bg-white shadow-sm">
      <!--
        这里对导航栏的内容进行布局：使用最大宽度、水平内边距（px-4等），并让其自动居中。
      -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- 
          flex justify-between: 通过Flexbox将子元素左右分布
          h-16: 导航条高度
        -->
        <div class="flex justify-between h-16">
          <div class="flex">
            <!--
              router-link 用于导航到指定路由的链接，这里跳转到"/"作为首页。
              class="flex items-center": 让链接内文字在垂直方向居中。
            -->
            <router-link to="/" class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50">
              首页
            </router-link>
            <router-link to="/site" class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50">
              站点
            </router-link>
            <router-link to="/cart" class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50">
              购物车
            </router-link>
            <router-link to="/notifications" class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50 relative">
              消息通知
              <span v-if="notificationsStore.unreadCount > 0" 
                class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                {{ notificationsStore.unreadCount }}
              </span>
            </router-link>
            <router-link to="/account" class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50">
              账号
            </router-link>
          </div>

          <!-- 右侧登录按钮 -->
          <div class="flex items-center">
            <router-link 
              v-if="!isLoggedIn"
              to="/login" 
              class="ml-4 px-4 py-2 rounded-md text-sm font-medium text-white bg-[#FF6B35] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
            >
              登录
            </router-link>
            <div v-else class="flex items-center">
              <span class="text-sm text-gray-700">{{ username }}</span>
              <button 
                @click="handleLogout" 
                class="ml-4 px-4 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
              >
                退出
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!--
      main元素是主要内容区域，设置了宽度、上下内边距，使用router-view来动态渲染对应路由的组件。
    -->
    <main class="mx-auto py-6 sm:px-6 lg:px-8 bg-white rounded-lg shadow">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNotificationsStore } from './stores/notifications'

const router = useRouter()
const isLoggedIn = ref(false)
const username = ref('')
const notificationsStore = useNotificationsStore()

// 检查登录状态
onMounted(() => {
  // TODO: 从本地存储或状态管理中获取登录状态
  const storedUsername = localStorage.getItem('username')
  if (storedUsername) {
    isLoggedIn.value = true
    username.value = storedUsername
  }
  // 加载通知
  notificationsStore.loadNotifications()
})

// 退出登录
const handleLogout = () => {
  isLoggedIn.value = false
  username.value = ''
  localStorage.removeItem('username')
  // 跳转到登录页
  router.push('/login')
}
</script> 