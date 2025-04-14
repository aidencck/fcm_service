import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'

// 环境变量中的 API URL
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1'

// 默认配置
export const defaultConfig: AxiosRequestConfig = {
  baseURL: API_BASE_URL,
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json'
  }
}

// 创建 axios 实例
const createAxiosInstance = (config: AxiosRequestConfig): AxiosInstance => {
  const instance = axios.create({
    ...defaultConfig,
    ...config
  })
  return instance
}

export default createAxiosInstance
