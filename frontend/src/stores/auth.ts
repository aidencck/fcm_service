import { defineStore } from 'pinia'
import { ref } from 'vue'

interface User {
  id: string
  username: string
  email: string
  avatar?: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const isAuthenticated = ref(false)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // 登录
  const login = async (username: string, password: string) => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的登录逻辑
      const mockUser: User = {
        id: '1',
        username,
        email: `${username}@example.com`
      }
      user.value = mockUser
      isAuthenticated.value = true
      localStorage.setItem('user', JSON.stringify(mockUser))
    } catch (e) {
      error.value = e instanceof Error ? e.message : '登录失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 登出
  const logout = () => {
    user.value = null
    isAuthenticated.value = false
    localStorage.removeItem('user')
  }

  // 检查登录状态
  const checkAuth = () => {
    const storedUser = localStorage.getItem('user')
    if (storedUser) {
      user.value = JSON.parse(storedUser)
      isAuthenticated.value = true
    }
  }

  // 获取用户信息
  const getUser = () => user.value

  return {
    user,
    isAuthenticated,
    loading,
    error,
    login,
    logout,
    checkAuth,
    getUser
  }
}) 