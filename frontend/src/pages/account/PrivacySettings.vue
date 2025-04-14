<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <!-- Header -->
        <div class="px-6 py-4 border-b border-gray-200">
          <router-link to="/account" class="text-sm font-medium text-blue-600 hover:text-blue-700">
            &larr; 返回账号管理
          </router-link>
          <h1 class="mt-4 text-2xl font-semibold text-gray-900">隐私设置</h1>
          <p class="mt-1 text-sm text-gray-500">管理您的隐私和数据设置</p>
        </div>

        <!-- Main Content -->
        <div class="p-6">
          <!-- Data Collection Section -->
          <div class="space-y-4">
            <h2 class="text-lg font-medium text-gray-900">数据收集</h2>
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">使用统计</h3>
                  <p class="text-sm text-gray-500">帮助我们改进产品和服务</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.privacySettings.dataCollection"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">错误报告</h3>
                  <p class="text-sm text-gray-500">自动发送错误报告以帮助我们修复问题</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.privacySettings.errorReports"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
            </div>
          </div>

          <!-- Advertising Section -->
          <div class="mt-8 space-y-4">
            <h2 class="text-lg font-medium text-gray-900">广告偏好</h2>
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-sm font-medium text-gray-900">个性化广告</h3>
                <p class="text-sm text-gray-500">根据您的兴趣显示相关广告</p>
              </div>
              <input
                type="checkbox"
                v-model="accountStore.privacySettings.personalizedAds"
                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
            </div>
          </div>

          <!-- Data Management Section -->
          <div class="mt-8 space-y-4">
            <h2 class="text-lg font-medium text-gray-900">数据管理</h2>
            <div class="space-y-4">
              <div class="bg-blue-50 p-4 rounded-lg">
                <h3 class="text-sm font-medium text-blue-900">导出数据说明</h3>
                <p class="mt-1 text-sm text-blue-700">
                  导出的数据将包含您的个人信息、隐私设置、通知设置和登录设备信息。数据将以 JSON
                  格式下载到您的设备。
                </p>
              </div>
              <button
                @click="exportData"
                class="w-full px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700 border border-blue-600 rounded-md flex items-center justify-center"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                  />
                </svg>
                导出我的数据
              </button>
              <button
                @click="deleteData"
                class="w-full px-4 py-2 text-sm font-medium text-red-600 hover:text-red-700 border border-red-600 rounded-md"
              >
                删除我的数据
              </button>
            </div>
          </div>

          <!-- Save Button -->
          <div class="mt-8 flex justify-end">
            <button
              @click="saveSettings"
              class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md"
            >
              保存设置
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useAccountStore } from '../../stores/account'

const router = useRouter()
const accountStore = useAccountStore()

const saveSettings = () => {
  accountStore.updatePrivacySettings(accountStore.privacySettings)
  router.push('/account')
}

const exportData = () => {
  // 准备导出的数据
  const exportData = {
    userInfo: accountStore.userInfo,
    privacySettings: accountStore.privacySettings,
    notificationSettings: accountStore.notificationSettings,
    devices: accountStore.devices,
    exportTime: new Date().toISOString()
  }

  // 将数据转换为 JSON 字符串
  const dataStr = JSON.stringify(exportData, null, 2)

  // 创建 Blob 对象
  const blob = new Blob([dataStr], { type: 'application/json' })

  // 创建下载链接
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `user_data_${new Date().toISOString().split('T')[0]}.json`

  // 触发下载
  document.body.appendChild(link)
  link.click()

  // 清理
  document.body.removeChild(link)
  URL.revokeObjectURL(url)
}

const deleteData = () => {
  // TODO: 实现数据删除功能
  console.log('Deleting data...')
}
</script>
