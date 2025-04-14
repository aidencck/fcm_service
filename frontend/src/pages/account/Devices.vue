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
            <h1 class="text-2xl font-semibold text-gray-900">登录设备</h1>
          </div>
        </div>

        <div class="p-6">
          <div class="space-y-6">
            <div>
              <h2 class="text-lg font-medium text-gray-900">当前登录的设备</h2>
              <p class="mt-1 text-sm text-gray-500">
                这是您当前登录的所有设备。如果您发现任何可疑设备，请立即将其登出。
              </p>
            </div>

            <div class="space-y-4">
              <div 
                v-for="device in devices" 
                :key="device.id"
                class="flex items-center justify-between p-4 border rounded-lg"
              >
                <div class="flex items-center space-x-4">
                  <div class="flex-shrink-0">
                    <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div>
                    <h3 class="text-sm font-medium text-gray-900">{{ device.name }}</h3>
                    <p class="text-sm text-gray-500">
                      {{ device.location }} · {{ formatDate(device.lastActive) }}
                    </p>
                  </div>
                </div>
                <button
                  v-if="!device.isCurrent"
                  @click="logoutDevice(device.id)"
                  class="text-sm text-red-600 hover:text-red-700"
                >
                  登出
                </button>
                <span v-else class="text-sm text-green-600">当前设备</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Device {
  id: string
  name: string
  location: string
  lastActive: number
  isCurrent: boolean
}

const devices = ref<Device[]>([
  {
    id: '1',
    name: 'Windows PC',
    location: '中国，北京',
    lastActive: Date.now(),
    isCurrent: true
  },
  {
    id: '2',
    name: 'iPhone 13',
    location: '中国，上海',
    lastActive: Date.now() - 3600000 * 2,
    isCurrent: false
  },
  {
    id: '3',
    name: 'MacBook Pro',
    location: '中国，广州',
    lastActive: Date.now() - 3600000 * 24,
    isCurrent: false
  }
])

const formatDate = (timestamp: number) => {
  const date = new Date(timestamp)
  return date.toLocaleString('zh-CN', {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const logoutDevice = (deviceId: string) => {
  // TODO: 实现设备登出逻辑
  console.log('登出设备:', deviceId)
  devices.value = devices.value.filter(device => device.id !== deviceId)
}
</script> 