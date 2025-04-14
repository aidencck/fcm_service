import { defineStore } from 'pinia'
import { user as userUtil, token as tokenUtil } from '@/utils'
import type { UserInfo } from '@/types'

interface UserState {
  userInfo: UserInfo | null
  token: string | null
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    userInfo: null,
    token: null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
    username: (state) => state.userInfo?.username || '',
    roles: (state) => state.userInfo?.roles || [],
    permissions: (state) => state.userInfo?.permissions || [],
  },
  actions: {
    // 设置用户信息
    setUserInfo(userInfo: UserInfo) {
      this.userInfo = userInfo
      userUtil.set(userInfo)
    },
    // 设置 token
    setToken(token: string) {
      this.token = token
      tokenUtil.set(token)
    },
    // 清除用户信息
    clearUserInfo() {
      this.userInfo = null
      this.token = null
      userUtil.remove()
      tokenUtil.remove()
    },
    // 初始化用户信息
    initUserInfo() {
      const userInfo = userUtil.get()
      const token = tokenUtil.get()
      if (userInfo && token) {
        this.userInfo = userInfo
        this.token = token
      }
    },
  },
}) 