import { STORAGE_TOKEN_KEY, STORAGE_USER_KEY } from '@/constants'
import type { UserInfo } from '@/types'
import dayjs from 'dayjs'

// 存储相关工具函数
export const storage = {
  set: (key: string, value: any) => {
    localStorage.setItem(key, JSON.stringify(value))
  },
  get: (key: string) => {
    const value = localStorage.getItem(key)
    return value ? JSON.parse(value) : null
  },
  remove: (key: string) => {
    localStorage.removeItem(key)
  },
  clear: () => {
    localStorage.clear()
  },
}

// Token 相关工具函数
export const token = {
  set: (token: string) => {
    storage.set(STORAGE_TOKEN_KEY, token)
  },
  get: () => {
    return storage.get(STORAGE_TOKEN_KEY)
  },
  remove: () => {
    storage.remove(STORAGE_TOKEN_KEY)
  },
}

// 用户信息相关工具函数
export const user = {
  set: (userInfo: UserInfo) => {
    storage.set(STORAGE_USER_KEY, userInfo)
  },
  get: () => {
    return storage.get(STORAGE_USER_KEY)
  },
  remove: () => {
    storage.remove(STORAGE_USER_KEY)
  },
}

// 日期时间格式化
export const formatDate = (date: Date | string | number, format = 'YYYY-MM-DD HH:mm:ss') => {
  return dayjs(date).format(format)
}

// 防抖函数
export const debounce = (fn: Function, delay = 300) => {
  let timer: NodeJS.Timeout | null = null
  return function (this: any, ...args: any[]) {
    if (timer) clearTimeout(timer)
    timer = setTimeout(() => {
      fn.apply(this, args)
    }, delay)
  }
}

// 节流函数
export const throttle = (fn: Function, delay = 300) => {
  let timer: NodeJS.Timeout | null = null
  return function (this: any, ...args: any[]) {
    if (timer) return
    timer = setTimeout(() => {
      fn.apply(this, args)
      timer = null
    }, delay)
  }
}

// 深拷贝
export const deepClone = <T>(obj: T): T => {
  return JSON.parse(JSON.stringify(obj))
}

// 判断是否为移动设备
export const isMobile = () => {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent
  )
}

// 生成随机字符串
export const randomString = (length = 16) => {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  let result = ''
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length))
  }
  return result
} 