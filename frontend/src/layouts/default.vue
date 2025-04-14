<template>
  <div class="min-h-screen bg-background text-text">
    <!-- 头部导航 -->
    <header class="sticky top-0 z-50 bg-white dark:bg-gray-800 shadow">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <router-link to="/" class="flex items-center">
            <img src="@/assets/logo.svg" alt="Logo" class="h-8 w-auto" />
            <span class="ml-2 text-xl font-bold">Vue App</span>
          </router-link>

          <!-- 导航菜单 -->
          <nav class="hidden md:flex space-x-8">
            <router-link
              v-for="item in navItems"
              :key="item.path"
              :to="item.path"
              class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary"
              active-class="text-primary dark:text-primary"
            >
              {{ item.title }}
            </router-link>
          </nav>

          <!-- 用户菜单 -->
          <div class="flex items-center space-x-4">
            <!-- 主题切换 -->
            <button
              @click="toggleTheme"
              class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              <svg
                v-if="isDark"
                class="w-5 h-5 text-gray-600 dark:text-gray-300"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
              <svg
                v-else
                class="w-5 h-5 text-gray-600 dark:text-gray-300"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                />
              </svg>
            </button>

            <!-- 用户头像 -->
            <div v-if="isLoggedIn" class="relative">
              <button
                @click="toggleUserMenu"
                class="flex items-center space-x-2 focus:outline-none"
              >
                <img
                  :src="userAvatar"
                  alt="User Avatar"
                  class="w-8 h-8 rounded-full"
                />
                <span class="text-gray-600 dark:text-gray-300">{{
                  username
                }}</span>
              </button>

              <!-- 用户下拉菜单 -->
              <div
                v-if="showUserMenu"
                class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg py-1"
              >
                <router-link
                  to="/profile"
                  class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  个人中心
                </router-link>
                <button
                  @click="handleLogout"
                  class="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  退出登录
                </button>
              </div>
            </div>

            <!-- 登录按钮 -->
            <router-link
              v-else
              to="/login"
              class="px-4 py-2 text-sm font-medium text-white bg-primary rounded-md hover:bg-primary-dark"
            >
              登录
            </router-link>
          </div>
        </div>
      </div>
    </header>

    <!-- 主要内容 -->
    <main class="container mx-auto px-4 py-8">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- 页脚 -->
    <footer class="bg-gray-100 dark:bg-gray-800 py-8">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="mb-4 md:mb-0">
            <p class="text-gray-600 dark:text-gray-300">
              © 2024 Vue App. All rights reserved.
            </p>
          </div>
          <div class="flex space-x-6">
            <a
              href="#"
              class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary"
            >
              关于我们
            </a>
            <a
              href="#"
              class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary"
            >
              隐私政策
            </a>
            <a
              href="#"
              class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary"
            >
              使用条款
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores'
import { useThemeStore } from '@/stores'

const router = useRouter()
const userStore = useUserStore()
const themeStore = useThemeStore()

// 导航菜单项
const navItems = [
  { path: '/', title: '首页' },
  { path: '/features', title: '功能' },
  { path: '/pricing', title: '价格' },
  { path: '/docs', title: '文档' },
]

// 用户菜单状态
const showUserMenu = ref(false)

// 计算属性
const isLoggedIn = computed(() => userStore.isLoggedIn)
const username = computed(() => userStore.username)
const userAvatar = computed(() => userStore.userInfo?.avatar || '/default-avatar.png')
const isDark = computed(() => themeStore.isDark)

// 方法
const toggleUserMenu = () => {
  showUserMenu.value = !showUserMenu.value
}

const toggleTheme = () => {
  themeStore.toggleTheme()
}

const handleLogout = async () => {
  await userStore.clearUserInfo()
  router.push('/login')
}

// 点击外部关闭用户菜单
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement
  if (!target.closest('.relative')) {
    showUserMenu.value = false
  }
}

// 监听点击事件
document.addEventListener('click', handleClickOutside)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style> 