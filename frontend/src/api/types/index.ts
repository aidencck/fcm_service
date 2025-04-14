// 基础响应格式
export interface BaseResponse<T = any> {
  code: number
  data: T
  message: string
}

// 错误响应格式
export interface ApiError {
  code: number
  message: string
  details?: any
}

// 分页请求参数
export interface PaginationParams {
  page?: number
  pageSize?: number
}

// 分页响应数据
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
  totalPages: number
}
