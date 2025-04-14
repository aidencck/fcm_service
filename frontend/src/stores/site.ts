import { defineStore } from 'pinia'
import { ref } from 'vue'

interface Site {
  id: string
  name: string
  description: string
  url: string
  logo?: string
  status: 'active' | 'inactive' | 'maintenance'
}

export const useSiteStore = defineStore('site', () => {
  const sites = ref<Site[]>([])
  const currentSite = ref<Site | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // 获取所有站点
  const fetchSites = async () => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的API调用
      const mockSites: Site[] = [
        {
          id: '1',
          name: '示例站点1',
          description: '这是一个示例站点',
          url: 'https://example1.com',
          status: 'active'
        },
        {
          id: '2',
          name: '示例站点2',
          description: '这是另一个示例站点',
          url: 'https://example2.com',
          status: 'active'
        }
      ]
      sites.value = mockSites
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取站点列表失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 获取单个站点
  const fetchSite = async (id: string) => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的API调用
      const site = sites.value.find(s => s.id === id)
      if (site) {
        currentSite.value = site
      } else {
        throw new Error('站点不存在')
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取站点信息失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 添加站点
  const addSite = async (site: Omit<Site, 'id'>) => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的API调用
      const newSite: Site = {
        ...site,
        id: Date.now().toString()
      }
      sites.value.push(newSite)
    } catch (e) {
      error.value = e instanceof Error ? e.message : '添加站点失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 更新站点
  const updateSite = async (id: string, site: Partial<Site>) => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的API调用
      const index = sites.value.findIndex(s => s.id === id)
      if (index !== -1) {
        sites.value[index] = { ...sites.value[index], ...site }
        if (currentSite.value?.id === id) {
          currentSite.value = sites.value[index]
        }
      } else {
        throw new Error('站点不存在')
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '更新站点失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 删除站点
  const deleteSite = async (id: string) => {
    loading.value = true
    error.value = null
    try {
      // TODO: 实现实际的API调用
      const index = sites.value.findIndex(s => s.id === id)
      if (index !== -1) {
        sites.value.splice(index, 1)
        if (currentSite.value?.id === id) {
          currentSite.value = null
        }
      } else {
        throw new Error('站点不存在')
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '删除站点失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    sites,
    currentSite,
    loading,
    error,
    fetchSites,
    fetchSite,
    addSite,
    updateSite,
    deleteSite
  }
}) 