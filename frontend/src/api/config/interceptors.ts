import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import type { ApiError } from '../types'

export const setupInterceptors = (instance: AxiosInstance) => {
  // 请求拦截器
  instance.interceptors.request.use(
    (config: AxiosRequestConfig) => {
      // 从 localStorage 获取 token
      const token = localStorage.getItem('token')
      if (token) {
        config.headers = {
          ...config.headers,
          Authorization: `Bearer ${token}`
        }
      }
      return config
    },
    (error) => {
      return Promise.reject(error)
    }
  )

  // 响应拦截器
  instance.interceptors.response.use(
    (response: AxiosResponse) => {
      // 直接返回响应数据
      return response.data
    },
    (error) => {
      const { response } = error
      let errorMessage = '未知错误'

      if (response) {
        const { status } = response
        switch (status) {
          case 401:
            errorMessage = '未授权，请重新登录'
            // 处理登录过期
            handleUnauthorized()
            break
          case 403:
            errorMessage = '拒绝访问'
            break
          case 404:
            errorMessage = '请求的资源不存在'
            break
          case 500:
            errorMessage = '服务器错误'
            break
          default:
            errorMessage = `请求失败(${status})`
        }
      } else {
        if (error.message.includes('timeout')) {
          errorMessage = '请求超时'
        } else if (error.message.includes('Network')) {
          errorMessage = '网络连接失败'
        }
      }

      const apiError: ApiError = {
        code: response?.status || -1,
        message: errorMessage,
        details: response?.data
      }

      return Promise.reject(apiError)
    }
  )
}

// 处理未授权情况
const handleUnauthorized = () => {
  localStorage.removeItem('token')
  window.location.href = '/login'
} 