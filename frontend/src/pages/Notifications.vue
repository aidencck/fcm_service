<template>
  <div class="bg-white rounded-lg shadow p-6">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">消息通知</h1>
      <button 
        v-if="notificationsStore.unreadCount > 0"
        @click="notificationsStore.markAllAsRead()"
        class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50 rounded-md"
      >
        全部标记为已读
      </button>
    </div>

    <div v-if="notificationsStore.notifications.length === 0" class="text-center py-12">
      <p class="text-gray-500">暂无消息通知</p>
    </div>

    <div v-else class="space-y-4">
      <div 
        v-for="notification in notificationsStore.notifications" 
        :key="notification.id"
        class="border rounded-lg p-4 hover:bg-gray-50 transition-colors cursor-pointer"
        :class="{ 'bg-gray-50': !notification.read }"
        @click="$router.push(`/notifications/${notification.id}`)"
      >
        <div class="flex justify-between items-start">
          <div class="flex-1">
            <div class="flex items-center space-x-2">
              <h3 class="font-medium text-gray-900">{{ notification.title }}</h3>
              <span 
                v-if="!notification.read" 
                class="inline-block h-2 w-2 rounded-full bg-red-500"
              ></span>
            </div>
            <p class="mt-1 text-gray-600 line-clamp-2">{{ notification.message }}</p>
            <p class="mt-2 text-xs text-gray-500">
              {{ formatDate(notification.timestamp) }}
            </p>
          </div>
          <div class="flex space-x-2">
            <button 
              v-if="!notification.read"
              @click.stop="notificationsStore.markAsRead(notification.id)"
              class="text-sm text-gray-500 hover:text-gray-700"
            >
              标记为已读
            </button>
            <button 
              @click.stop="notificationsStore.removeNotification(notification.id)"
              class="text-sm text-red-500 hover:text-red-700"
            >
              删除
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useNotificationsStore } from '../stores/notifications'

const notificationsStore = useNotificationsStore()

onMounted(() => {
  notificationsStore.loadNotifications()
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
</script> 