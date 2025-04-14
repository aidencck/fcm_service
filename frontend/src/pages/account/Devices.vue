<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200">
          <router-link 
            to="/account" 
            class="text-sm font-medium text-blue-600 hover:text-blue-700"
          >
            &larr; 返回账号管理
          </router-link>
          <h1 class="mt-4 text-2xl font-semibold text-gray-900">登录设备</h1>
          <p class="mt-1 text-sm text-gray-500">查看和管理您的登录设备</p>
        </div>

        <div class="p-6">
          <div class="space-y-4">
            <div v-for="device in accountStore.devices" :key="device.id" class="flex items-center justify-between p-4 border border-gray-200 rounded-lg">
              <div>
                <h3 class="text-sm font-medium text-gray-900">{{ device.name }}</h3>
                <p class="text-sm text-gray-500">{{ device.location }}</p>
                <p class="text-sm text-gray-500">最后活动时间：{{ formatDate(device.lastActive) }}</p>
                <p v-if="device.isCurrent" class="text-sm text-green-600">当前设备</p>
              </div>
              <button 
                v-if="!device.isCurrent"
                @click="logoutDevice(device.id)"
                class="px-4 py-2 text-sm font-medium text-red-600 hover:text-red-700"
              >
                退出登录
              </button>
            </div>
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

const logoutDevice = (deviceId: string) => {
  accountStore.logoutDevice(deviceId)
}

const formatDate = (timestamp: number) => {
  const date = new Date(timestamp)
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script> 