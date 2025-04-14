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
            <h1 class="text-2xl font-semibold text-gray-900">双重认证</h1>
          </div>
        </div>

        <div class="p-6">
          <div class="space-y-6">
            <div>
              <h2 class="text-lg font-medium text-gray-900">设置双重认证</h2>
              <p class="mt-1 text-sm text-gray-500">
                双重认证为您的账号提供额外的安全保护。启用后，除了密码外，您还需要输入通过手机应用生成的验证码才能登录。
              </p>
            </div>

            <div class="border rounded-lg p-4 bg-gray-50">
              <h3 class="text-sm font-medium text-gray-900">使用步骤</h3>
              <ol class="mt-2 text-sm text-gray-500 list-decimal list-inside space-y-2">
                <li>在手机上下载并安装 Google Authenticator 或其他认证应用</li>
                <li>扫描下方二维码或手动输入密钥</li>
                <li>输入应用生成的6位验证码</li>
              </ol>
            </div>

            <div class="flex justify-center">
              <div class="p-4 bg-white rounded-lg border">
                <!-- 这里应该显示实际的二维码 -->
                <div class="w-48 h-48 bg-gray-200 flex items-center justify-center">
                  <span class="text-gray-500">二维码将在这里显示</span>
                </div>
              </div>
            </div>

            <div>
              <label for="verificationCode" class="block text-sm font-medium text-gray-700"
                >验证码</label
              >
              <input
                type="text"
                id="verificationCode"
                v-model="verificationCode"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                placeholder="输入6位验证码"
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
                @click="enableTwoFactorAuth"
                class="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                启用双重认证
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const verificationCode = ref('')

const enableTwoFactorAuth = () => {
  // TODO: 实现双重认证启用逻辑
  console.log('启用双重认证:', verificationCode.value)
  router.push('/account')
}
</script>
