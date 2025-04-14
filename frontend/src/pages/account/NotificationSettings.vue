<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <!-- Header -->
        <div class="px-6 py-4 border-b border-gray-200">
          <router-link to="/account" class="text-sm font-medium text-blue-600 hover:text-blue-700">
            &larr; 返回账号管理
          </router-link>
          <h1 class="mt-4 text-2xl font-semibold text-gray-900">通知设置</h1>
          <p class="mt-1 text-sm text-gray-500">管理您接收的通知类型</p>
        </div>

        <!-- Main Content -->
        <div class="p-6">
          <!-- Notification Methods -->
          <div class="space-y-4">
            <h2 class="text-lg font-medium text-gray-900">通知方式</h2>
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">邮件通知</h3>
                  <p class="text-sm text-gray-500">通过电子邮件接收重要通知</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.notificationSettings.email"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">应用内通知</h3>
                  <p class="text-sm text-gray-500">在应用内接收通知</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.notificationSettings.inApp"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
            </div>
          </div>

          <!-- Notification Types -->
          <div class="mt-8 space-y-4">
            <h2 class="text-lg font-medium text-gray-900">通知类型</h2>
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">系统通知</h3>
                  <p class="text-sm text-gray-500">接收系统更新和维护通知</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.notificationSettings.system"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">安全通知</h3>
                  <p class="text-sm text-gray-500">接收账号安全相关通知</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.notificationSettings.security"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">营销通知</h3>
                  <p class="text-sm text-gray-500">接收产品更新和促销信息</p>
                </div>
                <input
                  type="checkbox"
                  v-model="accountStore.notificationSettings.marketing"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
              </div>
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
  accountStore.updateNotificationSettings(accountStore.notificationSettings)
  router.push('/account')
}
</script>
