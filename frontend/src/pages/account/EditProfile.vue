<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200">
          <div class="flex items-center">
            <router-link to="/account" class="text-gray-600 hover:text-gray-900 mr-4">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 19l-7-7 7-7"
                />
              </svg>
            </router-link>
            <h1 class="text-2xl font-semibold text-gray-900">编辑个人资料</h1>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-6">
          <div class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700">姓名</label>
              <input
                type="text"
                id="name"
                v-model="form.name"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
              />
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">邮箱</label>
              <input
                type="email"
                id="email"
                v-model="form.email"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
              />
            </div>

            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700">手机号码</label>
              <input
                type="tel"
                id="phone"
                v-model="form.phone"
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
                保存更改
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface FormData {
  name: string
  email: string
  phone: string
}

const form = ref<FormData>({
  name: '',
  email: '',
  phone: ''
})

onMounted(() => {
  // TODO: 从后端或本地存储获取用户信息
  const storedUser = localStorage.getItem('user')
  if (storedUser) {
    const user = JSON.parse(storedUser)
    form.value = {
      name: user.name || '',
      email: user.email || '',
      phone: user.phone || ''
    }
  }
})

const handleSubmit = () => {
  // TODO: 实现保存逻辑
  console.log('保存更改:', form.value)
  router.push('/account')
}
</script>
