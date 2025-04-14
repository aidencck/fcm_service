import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface UserInfo {
  name: string | null
  email: string | null
  phone: string | null
  createdAt: number | null
}

interface PrivacySettings {
  dataCollection: boolean
  errorReports: boolean
  personalizedAds: boolean
}

interface NotificationSettings {
  email: boolean
  inApp: boolean
  system: boolean
  security: boolean
  marketing: boolean
}

export const useAccountStore = defineStore('account', () => {
  // 用户信息状态
  const userInfo = ref<UserInfo>({
    name: '张三',
    email: 'zhangsan@example.com',
    phone: '13800138000',
    createdAt: Date.now() - 30 * 24 * 60 * 60 * 1000 // 30天前
  })

  // 隐私设置状态
  const privacySettings = ref<PrivacySettings>({
    dataCollection: true,
    errorReports: true,
    personalizedAds: false
  })

  // 通知设置状态
  const notificationSettings = ref<NotificationSettings>({
    email: true,
    inApp: true,
    system: true,
    security: true,
    marketing: false
  })

  // 登录设备状态
  const devices = ref([
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
      lastActive: Date.now() - 3600000 * 2, // 2小时前
      isCurrent: false
    },
    {
      id: '3',
      name: 'MacBook Pro',
      location: '中国，广州',
      lastActive: Date.now() - 3600000 * 24, // 24小时前
      isCurrent: false
    },
    {
      id: '4',
      name: 'iPad Pro',
      location: '中国，深圳',
      lastActive: Date.now() - 3600000 * 48, // 48小时前
      isCurrent: false
    }
  ])

  // 计算属性：格式化日期
  const formattedDate = computed(() => {
    if (!userInfo.value.createdAt) return '未知'
    const date = new Date(userInfo.value.createdAt)
    return date.toLocaleString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    })
  })

  // 计算属性：是否启用双重认证
  const isTwoFactorEnabled = ref(false)

  // 方法：更新用户信息
  const updateUserInfo = (newInfo: Partial<UserInfo>) => {
    userInfo.value = { ...userInfo.value, ...newInfo }
    localStorage.setItem('user', JSON.stringify(userInfo.value))
  }

  // 方法：更新隐私设置
  const updatePrivacySettings = (newSettings: Partial<PrivacySettings>) => {
    privacySettings.value = { ...privacySettings.value, ...newSettings }
    localStorage.setItem('privacySettings', JSON.stringify(privacySettings.value))
  }

  // 方法：更新通知设置
  const updateNotificationSettings = (newSettings: Partial<NotificationSettings>) => {
    notificationSettings.value = { ...notificationSettings.value, ...newSettings }
    localStorage.setItem('notificationSettings', JSON.stringify(notificationSettings.value))
  }

  // 方法：登出设备
  const logoutDevice = (deviceId: string) => {
    devices.value = devices.value.filter(device => device.id !== deviceId)
  }

  // 方法：启用/禁用双重认证
  const toggleTwoFactorAuth = (enabled: boolean) => {
    isTwoFactorEnabled.value = enabled
  }

  // 初始化：从本地存储加载数据
  const initialize = () => {
    const storedUser = localStorage.getItem('user')
    const storedPrivacy = localStorage.getItem('privacySettings')
    const storedNotifications = localStorage.getItem('notificationSettings')

    if (storedUser) {
      userInfo.value = JSON.parse(storedUser)
    }
    if (storedPrivacy) {
      privacySettings.value = JSON.parse(storedPrivacy)
    }
    if (storedNotifications) {
      notificationSettings.value = JSON.parse(storedNotifications)
    }
  }

  return {
    userInfo,
    privacySettings,
    notificationSettings,
    devices,
    formattedDate,
    isTwoFactorEnabled,
    updateUserInfo,
    updatePrivacySettings,
    updateNotificationSettings,
    logoutDevice,
    toggleTwoFactorAuth,
    initialize
  }
})
