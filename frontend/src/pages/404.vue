<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 text-center">
      <div>
        <h1 class="text-9xl font-extrabold text-primary">404</h1>
        <h2 class="mt-6 text-3xl font-extrabold text-gray-900 dark:text-white">
          页面未找到
        </h2>
        <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
          抱歉，您访问的页面不存在或已被移除。
        </p>
      </div>
      <div class="mt-8 space-y-4">
        <router-link
          to="/"
          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
        >
          返回首页
        </router-link>
        <button
          @click="goBack"
          class="w-full flex justify-center py-2 px-4 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
        >
          返回上一页
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  router.go(-1)
}
</script> 