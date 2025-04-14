import axios from 'axios'
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import { token } from '@/utils'
import { API_BASE_URL } from '@/constants'
import type { ApiResponse } from '@/types'

// 创建 axios 实例
const service: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    const t = token.get()
    if (t) {
      config.headers.Authorization = `Bearer ${t}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse<ApiResponse>) => {
    const { data } = response
    if (data.code === 200) {
      return data.data
    }
    // 处理业务错误
    return Promise.reject(new Error(data.message || '请求失败'))
  },
  (error) => {
    // 处理 HTTP 错误
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 未授权，清除 token 并跳转到登录页
          token.remove()
          window.location.href = '/login'
          break
        case 403:
          // 权限不足
          break
        case 404:
          // 资源不存在
          break
        case 500:
          // 服务器错误
          break
        default:
          break
      }
    }
    return Promise.reject(error)
  }
)

// 封装 GET 请求
export const get = <T = any>(url: string, params?: any, config?: AxiosRequestConfig): Promise<T> => {
  return service.get(url, { params, ...config })
}

// 封装 POST 请求
export const post = <T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> => {
  return service.post(url, data, config)
}

// 封装 PUT 请求
export const put = <T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> => {
  return service.put(url, data, config)
}

// 封装 DELETE 请求
export const del = <T = any>(url: string, params?: any, config?: AxiosRequestConfig): Promise<T> => {
  return service.delete(url, { params, ...config })
}

export default service 