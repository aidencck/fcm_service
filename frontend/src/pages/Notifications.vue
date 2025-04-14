<template>
  <div class="bg-white rounded-lg shadow">
    <div class="flex">
      <!-- 时间线 -->
      <div class="w-36 border-r border-gray-200 bg-gray-50">
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
          <div class="space-y-1">
            <button 
              v-for="(group, date) in groupedNotifications" 
              :key="date"
              @click="selectedDate = date"
              class="w-full text-left px-2 py-2 rounded-lg transition-colors duration-200"
              :class="{
                'bg-white shadow-sm border border-blue-200': selectedDate === date,
                'hover:bg-white hover:shadow-sm': selectedDate !== date
              }"
            >
              <div class="flex items-center justify-between">
                <div class="text-sm font-medium text-gray-900">{{ formatDateLabel(date) }}</div>
                <div 
                  class="text-xs px-1.5 py-0.5 rounded-full"
                  :class="{
                    'bg-blue-100 text-blue-700': selectedDate === date,
                    'bg-gray-100 text-gray-600': selectedDate !== date
                  }"
                >
                  {{ group.length }}
                </div>
              </div>
              <div 
                class="mt-0.5 text-xs"
                :class="{
                  'text-blue-600': selectedDate === date,
                  'text-gray-500': selectedDate !== date
                }"
              >
                {{ formatWeekday(date) }}
              </div>
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

// 格式化星期
const formatWeekday = (dateStr: string) => {
  const date = new Date(dateStr)
  const today = new Date()
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)

  if (date.toDateString() === today.toDateString()) {
    return '今天'
  } else if (date.toDateString() === yesterday.toDateString()) {
    return '昨天'
  } else {
    const weekdays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
    return weekdays[date.getDay()]
  }
}

// 格式化日期标签
const formatDateLabel = (dateStr: string) => {
  const date = new Date(dateStr)
  const today = new Date()
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)

  if (date.toDateString() === today.toDateString()) {
    return '今天'
  } else if (date.toDateString() === yesterday.toDateString()) {
    return '昨天'
  } else {
    return date.toLocaleDateString('zh-CN', {
      month: '2-digit',
      day: '2-digit'
    })
  }
}

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