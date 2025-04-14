import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import Http from '../api/http'
import type { BaseResponse } from '../api/types'

// 定义数据类型
interface ExampleData {
  id: string
  name: string
  description: string
  createdAt: string
}

// 定义 store
export const useExampleStore = defineStore('example', () => {
  // 状态定义
  const data = ref<ExampleData[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const currentItem = ref<ExampleData | null>(null)

  // 计算属性
  const isEmpty = computed(() => data.value.length === 0)
  const totalCount = computed(() => data.value.length)

  // 获取数据列表
  const fetchData = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await Http.get<ExampleData[]>('/examples')
      if (response.code === 0) {
        data.value = response.data
      } else {
        throw new Error(response.message)
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取数据失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 获取单个数据
  const fetchItem = async (id: string) => {
    loading.value = true
    error.value = null
    try {
      const response = await Http.get<ExampleData>(`/examples/${id}`)
      if (response.code === 0) {
        currentItem.value = response.data
      } else {
        throw new Error(response.message)
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取数据失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 创建数据
  const createItem = async (item: Omit<ExampleData, 'id' | 'createdAt'>) => {
    loading.value = true
    error.value = null
    try {
      const response = await Http.post<ExampleData>('/examples', item)
      if (response.code === 0) {
        data.value.push(response.data)
        return response.data
      } else {
        throw new Error(response.message)
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '创建数据失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 更新数据
  const updateItem = async (id: string, item: Partial<ExampleData>) => {
    loading.value = true
    error.value = null
    try {
      const response = await Http.put<ExampleData>(`/examples/${id}`, item)
      if (response.code === 0) {
        const index = data.value.findIndex(d => d.id === id)
        if (index !== -1) {
          data.value[index] = { ...data.value[index], ...response.data }
        }
        if (currentItem.value?.id === id) {
          currentItem.value = { ...currentItem.value, ...response.data }
        }
        return response.data
      } else {
        throw new Error(response.message)
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '更新数据失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  // 删除数据
  const deleteItem = async (id: string) => {
    loading.value = true
    error.value = null
    try {
      const response = await Http.delete(`/examples/${id}`)
      if (response.code === 0) {
        const index = data.value.findIndex(d => d.id === id)
        if (index !== -1) {
          data.value.splice(index, 1)
        }
        if (currentItem.value?.id === id) {
          currentItem.value = null
        }
      } else {
        throw new Error(response.message)
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '删除数据失败'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    // 状态
    data,
    loading,
    error,
    currentItem,
    // 计算属性
    isEmpty,
    totalCount,
    // 方法
    fetchData,
    fetchItem,
    createItem,
    updateItem,
    deleteItem
  }
}) 