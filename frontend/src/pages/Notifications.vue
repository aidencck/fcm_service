<template>
  <div class="bg-white rounded-lg shadow">
    <div class="flex">
      <!-- 时间线 -->
      <div class="w-40 border-r border-gray-200 bg-gray-50 relative hidden">
        <div class="sticky top-0 p-4">
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-sm font-semibold text-gray-900">时间线</h2>
            <button
              @click="selectedDate = ''"
              class="text-xs text-blue-600 hover:text-blue-700"
              :class="{ 'opacity-50 cursor-not-allowed': !selectedDate }"
              :disabled="!selectedDate"
            >
              全部
            </button>
          </div>
          <div class="space-y-1 relative">
            <!-- Vertical line -->
            <div class="absolute left-4 top-2 bottom-2 w-0.5 bg-gray-200"></div>

            <button
              v-for="(group, date, index) in groupedNotifications"
              :key="date"
              @click="selectedDate = date"
              class="relative w-full text-left px-2 py-2 rounded-lg transition-colors duration-200 group"
              :class="{
                'bg-white shadow-sm border border-blue-200': selectedDate === date,
                'hover:bg-white hover:shadow-sm': selectedDate !== date
              }"
            >
              <!-- Timeline Node -->
              <div
                class="absolute left-4 top-1/2 -translate-x-1/2 -translate-y-1/2 w-3 h-3 rounded-full border-2 z-10"
                :class="{
                  'bg-blue-500 border-white': selectedDate === date,
                  'bg-gray-300 border-gray-50 group-hover:bg-gray-400': selectedDate !== date
                }"
              ></div>

            </button>
          </div>
        </div>
      </div>

      <!-- 消息列表 -->
      <div class="flex-1 p-6">
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

        <div v-if="filteredNotifications.length === 0" class="text-center py-12">
          <p class="text-gray-500">暂无消息通知</p>
        </div>

        <div v-else class="space-y-4">
          <div
            v-for="notification in filteredNotifications"
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
                  {{ formatTime(notification.timestamp) }}
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
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useNotificationsStore } from '../stores/notifications'

const notificationsStore = useNotificationsStore()
const selectedDate = ref<string>('')

onMounted(() => {
  notificationsStore.loadNotifications()
})

// 按日期分组通知
const groupedNotifications = computed(() => {
  const groups: { [key: string]: any[] } = {}
  notificationsStore.notifications.forEach(notification => {
    const date = new Date(notification.timestamp).toISOString().split('T')[0]
    if (!groups[date]) {
      groups[date] = []
    }
    groups[date].push(notification)
  })
  return groups
})

// 获取当前选中日期的通知
const filteredNotifications = computed(() => {
  if (!selectedDate.value) {
    return notificationsStore.notifications
  }
  return groupedNotifications.value[selectedDate.value] || []
})

// 格式化时间
const formatTime = (timestamp: number) => {
  const date = new Date(timestamp)
  return date.toLocaleTimeString('zh-CN', {
    hour: '2-digit',
    minute: '2-digit'
  })
}

// 格式化完整日期
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
