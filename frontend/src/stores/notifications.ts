import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface Notification {
  id: string
  title: string
  message: string
  type: 'info' | 'success' | 'warning' | 'error'
  timestamp: number
  read: boolean
}

export const useNotificationsStore = defineStore('notifications', () => {
  const notifications = ref<Notification[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // 未读通知数量
  const unreadCount = computed(() => {
    return notifications.value.filter(n => !n.read).length
  })

  // 添加通知
  const addNotification = (notification: Omit<Notification, 'id' | 'timestamp' | 'read'>) => {
    const newNotification: Notification = {
      ...notification,
      id: Date.now().toString(),
      timestamp: Date.now(),
      read: false
    }
    notifications.value.unshift(newNotification)
    saveNotifications()
  }

  // 标记通知为已读
  const markAsRead = (id: string) => {
    const notification = notifications.value.find(n => n.id === id)
    if (notification) {
      notification.read = true
      saveNotifications()
    }
  }

  // 标记所有通知为已读
  const markAllAsRead = () => {
    notifications.value.forEach(notification => {
      notification.read = true
    })
    saveNotifications()
  }

  // 删除通知
  const removeNotification = (id: string) => {
    notifications.value = notifications.value.filter(n => n.id !== id)
    saveNotifications()
  }

  // 清空通知
  const clearNotifications = () => {
    notifications.value = []
    saveNotifications()
  }

  // 保存通知到本地存储
  const saveNotifications = () => {
    localStorage.setItem('notifications', JSON.stringify(notifications.value))
  }

  // 从本地存储加载通知
  const loadNotifications = () => {
    const savedNotifications = localStorage.getItem('notifications')
    if (savedNotifications) {
      notifications.value = JSON.parse(savedNotifications)
    } else {
      // 添加测试数据
      const testNotifications: Notification[] = [
        {
          id: '1',
          title: '欢迎使用系统',
          message: '感谢您使用我们的系统，祝您使用愉快！',
          type: 'info',
          timestamp: Date.now() - 3600000 * 24 * 2, // 2天前
          read: true
        },
        {
          id: '2',
          title: '系统更新通知',
          message: '系统将于今晚22:00进行维护更新，预计持续2小时。',
          type: 'warning',
          timestamp: Date.now() - 3600000 * 12, // 12小时前
          read: false
        },
        {
          id: '3',
          title: '订单发货通知',
          message: '您的订单 #12345 已发货，预计3天内送达。',
          type: 'success',
          timestamp: Date.now() - 3600000 * 6, // 6小时前
          read: false
        },
        {
          id: '4',
          title: '账户安全提醒',
          message: '检测到您的账户在异地登录，如非本人操作请及时修改密码。',
          type: 'error',
          timestamp: Date.now() - 3600000 * 2, // 2小时前
          read: false
        },
        {
          id: '5',
          title: '新功能上线',
          message: '系统新增了消息通知功能，您可以在这里查看所有系统通知。',
          type: 'info',
          timestamp: Date.now() - 3600000, // 1小时前
          read: false
        }
      ]
      notifications.value = testNotifications
      saveNotifications()
    }
  }

  return {
    notifications,
    loading,
    error,
    unreadCount,
    addNotification,
    markAsRead,
    markAllAsRead,
    removeNotification,
    clearNotifications,
    loadNotifications
  }
}) 