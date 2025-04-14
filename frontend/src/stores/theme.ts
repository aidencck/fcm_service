import { defineStore } from 'pinia'
import { storage } from '@/utils'
import type { ThemeConfig } from '@/types'

const THEME_STORAGE_KEY = 'theme_config'

interface ThemeState {
  theme: ThemeConfig
  isDark: boolean
}

const defaultTheme: ThemeConfig = {
  primaryColor: '#4F46E5',
  backgroundColor: '#FFFFFF',
  textColor: '#1F2937',
  borderColor: '#E5E7EB',
}

const darkTheme: ThemeConfig = {
  primaryColor: '#6366F1',
  backgroundColor: '#1F2937',
  textColor: '#F9FAFB',
  borderColor: '#374151',
}

export const useThemeStore = defineStore('theme', {
  state: (): ThemeState => ({
    theme: defaultTheme,
    isDark: false,
  }),
  getters: {
    currentTheme: (state) => state.theme,
  },
  actions: {
    // 初始化主题
    initTheme() {
      const savedTheme = storage.get(THEME_STORAGE_KEY)
      if (savedTheme) {
        this.theme = savedTheme
        this.isDark = savedTheme.backgroundColor === darkTheme.backgroundColor
      }
    },
    // 切换主题
    toggleTheme() {
      this.isDark = !this.isDark
      this.theme = this.isDark ? darkTheme : defaultTheme
      storage.set(THEME_STORAGE_KEY, this.theme)
      this.applyTheme()
    },
    // 应用主题
    applyTheme() {
      const root = document.documentElement
      Object.entries(this.theme).forEach(([key, value]) => {
        root.style.setProperty(`--${key}`, value)
      })
    },
    // 设置主题
    setTheme(theme: ThemeConfig) {
      this.theme = theme
      this.isDark = theme.backgroundColor === darkTheme.backgroundColor
      storage.set(THEME_STORAGE_KEY, theme)
      this.applyTheme()
    },
  },
}) 