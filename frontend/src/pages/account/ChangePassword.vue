<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200">
          <div class="flex items-center">
            <router-link 
              to="/account" 
              class="text-gray-600 hover:text-gray-900 mr-4"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
            </router-link>
            <h1 class="text-2xl font-semibold text-gray-900">更改密码</h1>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-6">
          <div class="space-y-6">
            <div>
              <label for="currentPassword" class="block text-sm font-medium text-gray-700">当前密码</label>
              <input
                type="password"
                id="currentPassword"
                v-model="form.currentPassword"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
              />
            </div>

            <div>
              <label for="newPassword" class="block text-sm font-medium text-gray-700">新密码</label>
              <input
                type="password"
                id="newPassword"
                v-model="form.newPassword"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
              />
              <p class="mt-1 text-sm text-gray-500">密码长度至少8位，包含字母和数字</p>
            </div>

            <div>
              <label for="confirmPassword" class="block text-sm font-medium text-gray-700">确认新密码</label>
              <input
                type="password"
                id="confirmPassword"
                v-model="form.confirmPassword"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
              />
            </div>

            <div class="flex justify-end space-x-3">
              <router-link
                to="/account"
                class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                取消
              </router-link>
              <button
                type="submit"
                class="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                更改密码
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface FormData {
  currentPassword: string
  newPassword: string
  confirmPassword: string
}

const form = ref<FormData>({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
})

const handleSubmit = () => {
  // TODO: 实现密码更改逻辑
  console.log('更改密码:', form.value)
  router.push('/account')
}
</script> 