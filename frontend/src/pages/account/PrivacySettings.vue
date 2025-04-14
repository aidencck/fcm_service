<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200">
          <div class="flex items-center">
            <router-link 
              to="/account" 
              class="text-gray-600 hover:text-gray-900 mr-4"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
            </router-link>
            <h1 class="text-2xl font-semibold text-gray-900">隐私设置</h1>
          </div>
        </div>

        <div class="p-6">
          <div class="space-y-8">
            <!-- 数据收集设置 -->
            <div>
              <h2 class="text-lg font-medium text-gray-900">数据收集</h2>
              <p class="mt-1 text-sm text-gray-500">
                管理我们如何收集和使用您的数据
              </p>
              <div class="mt-4 space-y-4">
                <div class="flex items-center justify-between">
                  <div>
                    <h3 class="text-sm font-medium text-gray-900">使用情况统计</h3>
                    <p class="text-sm text-gray-500">帮助我们改进产品和服务</p>
                  </div>
                  <label class="relative inline-flex items-center cursor-pointer">
                    <input type="checkbox" class="sr-only peer" v-model="settings.usageStats">
                    <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                  </label>
                </div>
                <div class="flex items-center justify-between">
                  <div>
                    <h3 class="text-sm font-medium text-gray-900">错误报告</h3>
                    <p class="text-sm text-gray-500">自动发送错误报告以帮助我们解决问题</p>
                  </div>
                  <label class="relative inline-flex items-center cursor-pointer">
                    <input type="checkbox" class="sr-only peer" v-model="settings.errorReports">
                    <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                  </label>
                </div>
              </div>
            </div>

            <!-- 广告偏好 -->
            <div>
              <h2 class="text-lg font-medium text-gray-900">广告偏好</h2>
              <p class="mt-1 text-sm text-gray-500">
                管理您看到的广告
              </p>
              <div class="mt-4 space-y-4">
                <div class="flex items-center justify-between">
                  <div>
                    <h3 class="text-sm font-medium text-gray-900">个性化广告</h3>
                    <p class="text-sm text-gray-500">根据您的兴趣显示相关广告</p>
                  </div>
                  <label class="relative inline-flex items-center cursor-pointer">
                    <input type="checkbox" class="sr-only peer" v-model="settings.personalizedAds">
                    <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                  </label>
                </div>
              </div>
            </div>

            <!-- 数据导出 -->
            <div>
              <h2 class="text-lg font-medium text-gray-900">数据管理</h2>
              <p class="mt-1 text-sm text-gray-500">
                导出或删除您的数据
              </p>
              <div class="mt-4 space-y-4">
                <button
                  @click="exportData"
                  class="px-4 py-2 text-sm font-medium text-blue-600 bg-white border border-blue-600 rounded-md hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                >
                  导出数据
                </button>
                <button
                  @click="deleteData"
                  class="px-4 py-2 text-sm font-medium text-red-600 bg-white border border-red-600 rounded-md hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                >
                  删除数据
                </button>
              </div>
            </div>

            <div class="flex justify-end">
              <button
                @click="saveSettings"
                class="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                保存设置
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface PrivacySettings {
  usageStats: boolean
  errorReports: boolean
  personalizedAds: boolean
}

const settings = ref<PrivacySettings>({
  usageStats: true,
  errorReports: true,
  personalizedAds: false
})

const saveSettings = () => {
  // TODO: 实现设置保存逻辑
  console.log('保存设置:', settings.value)
  router.push('/account')
}

const exportData = () => {
  // TODO: 实现数据导出逻辑
  console.log('导出数据')
}

const deleteData = () => {
  // TODO: 实现数据删除逻辑
  console.log('删除数据')
}
</script> 