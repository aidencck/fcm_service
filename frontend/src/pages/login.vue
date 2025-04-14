<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <img class="mx-auto h-12 w-auto" src="@/assets/logo.svg" alt="Logo" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-white">
          登录您的账号
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400">
          或
          <router-link
            to="/register"
            class="font-medium text-primary hover:text-primary-dark"
          >
            注册新账号
          </router-link>
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email" class="sr-only">邮箱地址</label>
            <input
              id="email"
              v-model="form.email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-700 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-t-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-sm dark:bg-gray-800"
              placeholder="邮箱地址"
            />
          </div>
          <div>
            <label for="password" class="sr-only">密码</label>
            <input
              id="password"
              v-model="form.password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-700 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-b-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-sm dark:bg-gray-800"
              placeholder="密码"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              v-model="form.remember"
              name="remember-me"
              type="checkbox"
              class="h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded"
            />
            <label
              for="remember-me"
              class="ml-2 block text-sm text-gray-900 dark:text-white"
            >
              记住我
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-medium text-primary hover:text-primary-dark"
            >
              忘记密码？
            </a>
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg
                class="h-5 w-5 text-primary-light group-hover:text-primary-lighter"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
            {{ loading ? '登录中...' : '登录' }}
          </button>
        </div>
      </form>

      <!-- 错误提示 -->
      <div
        v-if="error"
        class="mt-4 p-4 bg-red-50 dark:bg-red-900 text-red-700 dark:text-red-200 rounded-md"
      >
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores'
import { post } from '@/api/request'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

// 表单数据
const form = reactive({
  email: '',
  password: '',
  remember: false,
})

// 状态
const loading = ref(false)
const error = ref('')

// 处理表单提交
const handleSubmit = async () => {
  try {
    loading.value = true
    error.value = ''

    // 调用登录接口
    const response = await post('/auth/login', {
      email: form.email,
      password: form.password,
    })

    // 保存用户信息和 token
    userStore.setUserInfo(response.user)
    userStore.setToken(response.token)

    // 跳转到首页或之前的页面
    const redirect = route.query.redirect as string
    router.push(redirect || '/')
  } catch (err: any) {
    error.value = err.message || '登录失败，请重试'
  } finally {
    loading.value = false
  }
}
</script> 