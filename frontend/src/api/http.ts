import type { AxiosRequestConfig, AxiosResponse } from 'axios'
import createAxiosInstance from './config/axios.config'
import { setupInterceptors } from './config/interceptors'
import type { BaseResponse } from './types'

class Http {
  private static instance = createAxiosInstance({})

  static init() {
    setupInterceptors(this.instance)
  }

  static async get<T = any>(url: string, config?: AxiosRequestConfig): Promise<BaseResponse<T>> {
    return this.instance.get(url, config)
  }

  static async post<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<BaseResponse<T>> {
    return this.instance.post(url, data, config)
  }

  static async put<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<BaseResponse<T>> {
    return this.instance.put(url, data, config)
  }

  static async delete<T = any>(url: string, config?: AxiosRequestConfig): Promise<BaseResponse<T>> {
    return this.instance.delete(url, config)
  }

  static async patch<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<BaseResponse<T>> {
    return this.instance.patch(url, data, config)
  }
}

// 初始化拦截器
Http.init()

export default Http
