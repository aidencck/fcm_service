<template>
  <div class="max-w-4xl mx-auto">
    <h1 class="text-2xl font-semibold text-gray-900 mb-8">设置</h1>

    <!-- 主题设置 -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
      <h2 class="text-lg font-medium text-gray-900 mb-4">主题设置</h2>
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">深色模式</h3>
            <p class="text-sm text-gray-500">切换到深色主题，减少眼睛疲劳</p>
          </div>
          <button
            class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            :class="isDarkMode ? 'bg-gray-900' : 'bg-gray-200'"
            @click="toggleDarkMode"
          >
            <span
              class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
              :class="isDarkMode ? 'translate-x-5' : 'translate-x-0'"
            />
          </button>
        </div>
      </div>
    </div>

    <!-- 语言设置 -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
      <h2 class="text-lg font-medium text-gray-900 mb-4">语言设置</h2>
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">界面语言</h3>
            <p class="text-sm text-gray-500">选择您偏好的界面显示语言</p>
          </div>
          <select
            v-model="selectedLanguage"
            class="mt-1 block w-48 rounded-md border-gray-300 py-2 pl-3 pr-10 text-base focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
            @change="updateLanguage"
          >
            <option value="zh-CN">简体中文</option>
            <option value="en-US">English</option>
          </select>
        </div>
      </div>
    </div>

    <!-- 通知设置 -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
      <h2 class="text-lg font-medium text-gray-900 mb-4">通知设置</h2>
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">系统通知</h3>
            <p class="text-sm text-gray-500">接收系统更新和维护通知</p>
          </div>
          <button
            class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            :class="systemNotifications ? 'bg-blue-600' : 'bg-gray-200'"
            @click="toggleSystemNotifications"
          >
            <span
              class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
              :class="systemNotifications ? 'translate-x-5' : 'translate-x-0'"
            />
          </button>
        </div>
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">邮件通知</h3>
            <p class="text-sm text-gray-500">接收重要通知到您的邮箱</p>
          </div>
          <button
            class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            :class="emailNotifications ? 'bg-blue-600' : 'bg-gray-200'"
            @click="toggleEmailNotifications"
          >
            <span
              class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
              :class="emailNotifications ? 'translate-x-5' : 'translate-x-0'"
            />
          </button>
        </div>
      </div>
    </div>

    <!-- 隐私设置 -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
      <h2 class="text-lg font-medium text-gray-900 mb-4">隐私设置</h2>
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-medium text-gray-900">数据收集</h3>
            <p class="text-sm text-gray-500">允许收集使用数据以改进服务</p>
          </div>
          <button
            class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            :class="dataCollection ? 'bg-blue-600' : 'bg-gray-200'"
            @click="toggleDataCollection"
          >
            <span
              class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
              :class="dataCollection ? 'translate-x-5' : 'translate-x-0'"
            />
          </button>
        </div>
      </div>
    </div>

    <!-- 保存按钮 -->
    <div class="flex justify-end">
      <button
        @click="saveSettings"
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        保存设置
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// 主题设置
const isDarkMode = ref(false)
const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  // 更新 HTML 的 class
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
  // 保存到 localStorage
  localStorage.setItem('darkMode', isDarkMode.value.toString())
}

// 语言设置
const selectedLanguage = ref('zh-CN')
const updateLanguage = () => {
  localStorage.setItem('language', selectedLanguage.value)
  // 这里可以添加语言切换的逻辑
}

// 通知设置
const systemNotifications = ref(true)
const emailNotifications = ref(true)
const toggleSystemNotifications = () => {
  systemNotifications.value = !systemNotifications.value
  localStorage.setItem('systemNotifications', systemNotifications.value.toString())
}
const toggleEmailNotifications = () => {
  emailNotifications.value = !emailNotifications.value
  localStorage.setItem('emailNotifications', emailNotifications.value.toString())
}

// 隐私设置
const dataCollection = ref(true)
const toggleDataCollection = () => {
  dataCollection.value = !dataCollection.value
  localStorage.setItem('dataCollection', dataCollection.value.toString())
}

// 保存设置
const saveSettings = () => {
  // 保存所有设置到 localStorage
  localStorage.setItem(
    'settings',
    JSON.stringify({
      isDarkMode: isDarkMode.value,
      language: selectedLanguage.value,
      systemNotifications: systemNotifications.value,
      emailNotifications: emailNotifications.value,
      dataCollection: dataCollection.value
    })
  )

  // 显示保存成功的提示
  alert('设置已保存')
}

// 初始化设置
onMounted(() => {
  // 从 localStorage 加载设置
  const savedSettings = localStorage.getItem('settings')
  if (savedSettings) {
    const settings = JSON.parse(savedSettings)
    isDarkMode.value = settings.isDarkMode
    selectedLanguage.value = settings.language
    systemNotifications.value = settings.systemNotifications
    emailNotifications.value = settings.emailNotifications
    dataCollection.value = settings.dataCollection
  }

  // 初始化深色模式
  const savedDarkMode = localStorage.getItem('darkMode')
  if (savedDarkMode === 'true') {
    isDarkMode.value = true
    document.documentElement.classList.add('dark')
  }
})
</script>

<style>
/* 深色模式样式 */
.dark {
  background-color: #1a1a1a;
  color: #ffffff;
}

.dark .bg-white {
  background-color: #2d2d2d;
}

.dark .text-gray-900 {
  color: #ffffff;
}

.dark .text-gray-500 {
  color: #a0a0a0;
}

.dark .border-gray-200 {
  border-color: #404040;
}
</style>
