// API 相关常量
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

// 路由相关常量
export const ROUTE_HOME = '/'
export const ROUTE_LOGIN = '/login'
export const ROUTE_REGISTER = '/register'

// 本地存储相关常量
export const STORAGE_TOKEN_KEY = 'auth_token'
export const STORAGE_USER_KEY = 'user_info'

// 请求相关常量
export const REQUEST_TIMEOUT = 10000
export const REQUEST_RETRY_COUNT = 3

// 分页相关常量
export const DEFAULT_PAGE_SIZE = 10
export const DEFAULT_PAGE_NUMBER = 1

// 主题相关常量
export const THEME_LIGHT = 'light'
export const THEME_DARK = 'dark'
export const DEFAULT_THEME = THEME_LIGHT

// 日期时间格式
export const DATE_FORMAT = 'YYYY-MM-DD'
export const DATETIME_FORMAT = 'YYYY-MM-DD HH:mm:ss'

// 其他全局常量
export const APP_NAME = 'Vue App'
export const APP_VERSION = '1.0.0' 
