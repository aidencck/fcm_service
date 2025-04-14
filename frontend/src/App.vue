// Start of Selection
<template>
  <!-- 
    这是App.vue的主要模板部分，包含页面的整体布局和导航栏以及主要内容的区域。
    使用了Tailwind CSS的一些类（如min-h-screen、bg-gray-100、max-w-7xl等）来控制布局和样式。
  -->
  <div class="app min-h-screen bg-gray-50">
    <header>
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
            <!-- 移动端菜单按钮和Logo -->
            <div class="flex items-center">
              <button
                @click="isDrawerOpen = true"
                class="inline-flex items-center justify-center p-2 rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500 md:hidden"
              >
                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              </button>
              <div class="ml-4 flex items-center">
                <!-- 替换文字Logo为SVG Logo -->
                <div class="flex items-center">
                  <svg
                    class="h-8 w-auto"
                    viewBox="0 0 120 40"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <!-- TV Mount Icon -->
                    <path
                      d="M20 8C13.3726 8 8 13.3726 8 20C8 26.6274 13.3726 32 20 32C26.6274 32 32 26.6274 32 20C32 13.3726 26.6274 8 20 8Z"
                      fill="#4F46E5"
                      fill-opacity="0.1"
                      stroke="#4F46E5"
                      stroke-width="2"
                    />
                    <path
                      d="M15 20H25M20 15V25"
                      stroke="#4F46E5"
                      stroke-width="2"
                      stroke-linecap="round"
                    />
                    <!-- Text Part -->
                    <path
                      d="M45 15H50L53 25L56 15H61L57 28H49L45 15Z"
                      stroke="#1F2937"
                      stroke-width="1.5"
                    />
                    <path
                      d="M63 15H75V18H67V20H74V23H67V25H75V28H63V15Z"
                      stroke="#1F2937"
                      stroke-width="1.5"
                    />
                    <path
                      d="M77 15H82L85 25L88 15H93L89 28H81L77 15Z"
                      stroke="#1F2937"
                      stroke-width="1.5"
                    />
                    <path
                      d="M95 15H107V18H99V20H106V23H99V25H107V28H95V15Z"
                      stroke="#1F2937"
                      stroke-width="1.5"
                    />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-900">Mount</span>
                </div>
              </div>
            </div>

            <!-- 桌面端导航链接 -->
            <div class="hidden md:flex md:items-center">
              <router-link
                to="/"
                class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                  />
                </svg>
                首页
              </router-link>
              <router-link
                to="/site"
                class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"
                  />
                </svg>
                站点
              </router-link>
              <router-link
                to="/cart"
                class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                  />
                </svg>
                购物车
              </router-link>
              <router-link
                to="/notifications"
                class="flex items-center px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50 relative"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                  />
                </svg>
                消息通知
                <span
                  v-if="notificationsStore.unreadCount > 0"
                  class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
                >
                  {{ notificationsStore.unreadCount }}
                </span>
              </router-link>
              <router-link
                to="/tv-mount"
                class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>
                TV Mount
              </router-link>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <!-- 移动端抽屉菜单 -->
    <div v-if="isDrawerOpen" class="fixed inset-0 z-50 md:hidden" role="dialog" aria-modal="true">
      <!-- 背景遮罩 -->
      <div
        class="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
        @click="isDrawerOpen = false"
      ></div>

      <!-- 抽屉面板 -->
      <div class="fixed inset-y-0 left-0 w-full max-w-xs bg-white shadow-xl">
        <!-- 抽屉头部 -->
        <div class="flex items-center justify-between px-4 h-16 border-b border-gray-200">
          <div class="text-lg font-semibold text-gray-900">菜单</div>
          <button
            @click="isDrawerOpen = false"
            class="p-2 rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
          >
            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <!-- 抽屉内容 -->
        <div class="px-2 py-3 space-y-1">
          <router-link
            v-for="item in menuItems"
            :key="item.path"
            :to="item.path"
            class="flex items-center px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-100"
            @click="isDrawerOpen = false"
          >
            <span class="mr-3" v-html="item.icon"></span>
            {{ item.name }}
          </router-link>
        </div>
      </div>
    </div>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <router-view></router-view>
    </main>

    <footer class="bg-white shadow-sm mt-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <p class="text-center text-gray-500 text-sm">
          © 2024 TV Mount. All rights reserved.
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNotificationsStore } from './stores/notifications'

const router = useRouter()
const notificationsStore = useNotificationsStore()
const isDrawerOpen = ref(false)

// 菜单项配置
const menuItems = [
  {
    name: '首页',
    path: '/',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>'
  },
  {
    name: '站点',
    path: '/site',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064" /></svg>'
  },
  {
    name: '购物车',
    path: '/cart',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" /></svg>'
  },
  {
    name: '消息通知',
    path: '/notifications',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>'
  },
  {
    name: 'TV Mount',
    path: '/tv-mount',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>'
  }
]

// 加载通知
onMounted(() => {
  notificationsStore.loadNotifications()
})
</script>

<style scoped>
/* 添加过渡动画效果 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
