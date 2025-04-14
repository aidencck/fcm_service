import Http from '../http'
import type { BaseResponse } from '../types'

interface LoginParams {
  username: string
  password: string
}

interface LoginResponse {
  token: string
  user: {
    id: string
    username: string
    email: string
  }
}

interface UserInfo {
  id: string
  username: string
  email: string
  // ... 其他用户信息字段
}

export class UserApi {
  private static baseUrl = '/users'

  static async login(params: LoginParams): Promise<BaseResponse<LoginResponse>> {
    return Http.post(`${this.baseUrl}/login`, params)
  }

  static async getUserInfo(): Promise<BaseResponse<UserInfo>> {
    return Http.get(`${this.baseUrl}/me`)
  }

  static async updateUserInfo(data: Partial<UserInfo>): Promise<BaseResponse<UserInfo>> {
    return Http.put(`${this.baseUrl}/me`, data)
  }
}
