// 用户信息类型
export interface UserInfo {
  id: number
  username: string
  email: string
  avatar?: string
  roles: string[]
  permissions: string[]
}

// API 响应类型
export interface ApiResponse<T = any> {
  code: number
  message: string
  data: T
}

// 分页参数类型
export interface PaginationParams {
  page: number
  pageSize: number
}

// 分页响应类型
export interface PaginationResponse<T = any> {
  total: number
  items: T[]
}

// 路由元信息类型
export interface RouteMeta {
  title: string
  icon?: string
  roles?: string[]
  permissions?: string[]
  hidden?: boolean
  keepAlive?: boolean
}

// 菜单项类型
export interface MenuItem {
  id: number
  parentId: number | null
  name: string
  path: string
  component?: string
  meta: RouteMeta
  children?: MenuItem[]
}

// 主题配置类型
export interface ThemeConfig {
  primaryColor: string
  backgroundColor: string
  textColor: string
  borderColor: string
}

// 系统配置类型
export interface SystemConfig {
  title: string
  logo: string
  copyright: string
  version: string
} 