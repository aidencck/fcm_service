<template>
  <div class="bg-white rounded-lg shadow p-6">
    <div class="mb-6">
      <router-link
        to="/notifications"
        class="inline-flex items-center text-gray-600 hover:text-gray-900"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 19l-7-7 7-7"
          />
        </svg>
        返回消息列表
      </router-link>
    </div>

    <div v-if="notification" class="space-y-6">
      <div class="flex justify-between items-start">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">{{ notification.title }}</h1>
          <p class="mt-2 text-sm text-gray-500">
            {{ formatDate(notification.timestamp) }}
          </p>
        </div>
        <div class="flex space-x-2">
          <button
            v-if="!notification.read"
            @click="markAsRead"
            class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50 rounded-md"
          >
            标记为已读
          </button>
          <button
            @click="deleteNotification"
            class="px-4 py-2 text-sm font-medium text-red-600 hover:text-red-700 hover:bg-red-50 rounded-md"
          >
            删除消息
          </button>
        </div>
      </div>

      <div class="prose max-w-none">
        <p class="text-gray-600">{{ notification.message }}</p>
      </div>

      <div class="flex items-center space-x-2">
        <span
          class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
          :class="{
            'bg-blue-100 text-blue-800': notification.type === 'info',
            'bg-green-100 text-green-800': notification.type === 'success',
            'bg-yellow-100 text-yellow-800': notification.type === 'warning',
            'bg-red-100 text-red-800': notification.type === 'error'
          }"
        >
          {{ getTypeText(notification.type) }}
        </span>
        <span
          v-if="!notification.read"
          class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800"
        >
          未读
        </span>
      </div>
    </div>

    <div v-else class="text-center py-12">
      <p class="text-gray-500">消息不存在或已被删除</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useNotificationsStore } from '../stores/notifications'

const route = useRoute()
const router = useRouter()
const notificationsStore = useNotificationsStore()

const notification = computed(() => {
  return notificationsStore.notifications.find(n => n.id === route.params.id)
})

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

const getTypeText = (type: string) => {
  const typeMap: Record<string, string> = {
    info: '信息',
    success: '成功',
    warning: '警告',
    error: '错误'
  }
  return typeMap[type] || type
}

const markAsRead = () => {
  if (notification.value) {
    notificationsStore.markAsRead(notification.value.id)
  }
}

const deleteNotification = () => {
  if (notification.value) {
    notificationsStore.removeNotification(notification.value.id)
    router.push('/notifications')
  }
}

onMounted(() => {
  if (!notification.value) {
    router.push('/notifications')
  }
})
</script>
