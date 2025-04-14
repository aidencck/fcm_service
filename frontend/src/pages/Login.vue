<template>
  <div>
    <!-- 背景图层 -->
    <!-- <div class="absolute inset-0 bg-gradient-to-br from-black to-gray-900">
      <div class="absolute inset-0 bg-[url('/tuya-bg.jpg')] bg-cover bg-center opacity-20"></div>
    </div> -->

    <!-- 右侧登录表单区域 -->
    <div
      class="w-full md:w-[480px] h-screen overflow-y-auto flex items-center justify-center bg-white/95 backdrop-blur-sm"
    >
      <div class="w-full max-w-[400px] px-8 py-8">
        <!-- <div class="text-center mb-8">
          <select v-model="language" class="text-sm text-gray-600 bg-transparent">
            <option value="zh">简体中文</option>
            <option value="en">English</option>
          </select>
        </div> -->

        <div class="mb-12">
          <h2 class="text-2xl font-semibold text-gray-900">账号登录</h2>
        </div>

        <!-- 错误消息显示 -->
        <div v-if="errorMessage" class="mb-4 p-4 bg-red-50 text-red-600 rounded-md text-center">
          {{ errorMessage }}
        </div>

        <form @submit.prevent="handleLogin" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 text-center">账号</label>
            <div class="mt-1 relative">
              <input
                type="text"
                v-model="username"
                placeholder="手机号或邮箱"
                class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-orange-500 focus:border-orange-500 text-center"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 text-center">密码</label>
            <div class="mt-1 relative">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                placeholder="密码"
                class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-orange-500 focus:border-orange-500 text-center"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 px-3 flex items-center text-gray-400"
              >
                {{ showPassword ? '隐藏' : '显示' }}
              </button>
            </div>
          </div>

          <div class="flex items-center justify-center space-x-4">
            <div class="flex items-center">
              <input
                type="checkbox"
                v-model="rememberMe"
                class="h-4 w-4 text-orange-600 focus:ring-orange-500 border-gray-300 rounded"
              />
              <label class="ml-2 block text-sm text-gray-900">记住密码</label>
            </div>
            <div class="text-sm">
              <a href="#" class="text-orange-600 hover:text-orange-500">忘记密码？</a>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#FF6B35] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
            >
              登录
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Start Generation Here
/**
 * 这段代码在登录页面中使用了 Vue 3 的组合式 API（setup 语法）来管理登录流程：
 * 1. 定义了多个响应式变量（username、password、showPassword、rememberMe、errorMessage）用来存储输入和相关状态。
 * 2. handleLogin 函数负责表单验证和“登录”逻辑：
 *    - 如果用户名或密码为空，则提示“请输入用户名和密码”。
 *    - 否则将用户名存储到 localStorage 中表示“登录成功”。
 *    - 如果选中了“记住密码”，则将用户名和密码持久化到 localStorage。
 *    - 登录后跳转到首页。
 * 3. checkRememberedLogin 函数在页面加载时调用，以检测本地是否存储了登录信息，如果存在就自动填写用户名和密码并设置复选状态。
 * 4. 同时，使用了 ref 定义了一些响应式变量，比如是否显示密码（showPassword），以便可以在输入框中来回切换明文与密文显示。
 * 5. 整合了路由（useRouter）来在登录成功后跳转到首页。
 */

import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const language = ref('zh')
/* 
  这两个变量分别表示“用户名”和“密码”，使用 Vue 的 ref() 创建为响应式数据。
  用户名和密码的初始值目前都为空字符串。
*/
// Start of Selection
const username = ref('') // 用户名
const password = ref('') // 密码
const showPassword = ref(false)
const rememberMe = ref(false)
const errorMessage = ref('')

const handleLogin = async () => {
  try {
    // 简单的表单验证
    if (!username.value || !password.value) {
      errorMessage.value = '请输入用户名和密码'
      return
    }

    // TODO: 实现实际的登录 API 调用
    // 这里模拟登录成功
    localStorage.setItem('username', username.value)

    if (rememberMe.value) {
      localStorage.setItem('rememberedUsername', username.value)
      localStorage.setItem('rememberedPassword', password.value)
    } else {
      localStorage.removeItem('rememberedUsername')
      localStorage.removeItem('rememberedPassword')
    }

    // 登录成功后跳转到首页
    router.push('/')
  } catch (error) {
    console.error('登录失败：', error)
    errorMessage.value = '登录失败，请检查用户名和密码'
  }
}

// 检查是否有记住的登录信息
const checkRememberedLogin = () => {
  const rememberedUsername = localStorage.getItem('rememberedUsername')
  const rememberedPassword = localStorage.getItem('rememberedPassword')

  if (rememberedUsername && rememberedPassword) {
    username.value = rememberedUsername
    password.value = rememberedPassword
    rememberMe.value = true
  }
}

// 在组件挂载时检查记住的登录信息
checkRememberedLogin()
</script>

<style>
/* 确保页面没有默认边距和滚动条 */
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

/* 添加平滑过渡效果 */
.bg-white\/95 {
  transition: background-color 0.3s ease;
}

/* 自定义滚动条样式 */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.2);
}
</style>
