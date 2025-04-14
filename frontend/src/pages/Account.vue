<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow">
        <!-- Header -->
        <div class="px-6 py-4 border-b border-gray-200">
          <h1 class="text-2xl font-semibold text-gray-900">账号管理</h1>
          <p class="mt-1 text-sm text-gray-500">管理您的账号信息和设置</p>
        </div>

        <!-- Main Content -->
        <div class="divide-y divide-gray-200">
          <!-- Personal Info Section -->
          <div class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <h2 class="text-lg font-medium text-gray-900">个人信息</h2>
                <p class="mt-1 text-sm text-gray-500">管理您的个人资料和联系方式</p>
              </div>
              <router-link
                to="/account/edit-profile"
                class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
              >
                编辑
              </router-link>
            </div>
            <div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">姓名</label>
                <p class="mt-1 text-sm text-gray-900">
                  {{ accountStore.userInfo.name || '未设置' }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">邮箱</label>
                <p class="mt-1 text-sm text-gray-900">
                  {{ accountStore.userInfo.email || '未设置' }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">手机号码</label>
                <p class="mt-1 text-sm text-gray-900">
                  {{ accountStore.userInfo.phone || '未设置' }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">注册时间</label>
                <p class="mt-1 text-sm text-gray-900">{{ accountStore.formattedDate }}</p>
              </div>
            </div>
          </div>

          <!-- Security Section -->
          <div class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <h2 class="text-lg font-medium text-gray-900">安全</h2>
                <p class="mt-1 text-sm text-gray-500">管理您的账号安全设置</p>
              </div>
            </div>
            <div class="mt-6 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">密码</h3>
                  <p class="text-sm text-gray-500">定期更改密码以保护账号安全</p>
                </div>
                <router-link
                  to="/account/change-password"
                  class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                >
                  更改密码
                </router-link>
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">双重认证</h3>
                  <p class="text-sm text-gray-500">为您的账号添加额外的安全保护</p>
                </div>
                <router-link
                  to="/account/two-factor-auth"
                  class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                >
                  设置
                </router-link>
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">登录设备</h3>
                  <p class="text-sm text-gray-500">查看和管理您的登录设备</p>
                </div>
                <router-link
                  to="/account/devices"
                  class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                >
                  管理
                </router-link>
              </div>
            </div>
          </div>

          <!-- Privacy Section -->
          <div class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <h2 class="text-lg font-medium text-gray-900">隐私</h2>
                <p class="mt-1 text-sm text-gray-500">管理您的隐私设置</p>
              </div>
            </div>
            <div class="mt-6 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">数据收集</h3>
                  <p class="text-sm text-gray-500">管理我们如何收集和使用您的数据</p>
                </div>
                <router-link
                  to="/account/privacy"
                  class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                >
                  管理
                </router-link>
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">广告偏好</h3>
                  <p class="text-sm text-gray-500">管理您看到的广告</p>
                </div>
                <button class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700">
                  设置
                </button>
              </div>
            </div>
          </div>

          <!-- Preferences Section -->
          <div class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <h2 class="text-lg font-medium text-gray-900">偏好设置</h2>
                <p class="mt-1 text-sm text-gray-500">自定义您的使用体验</p>
              </div>
            </div>
            <div class="mt-6 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">语言</h3>
                  <p class="text-sm text-gray-500">选择您的首选语言</p>
                </div>
                <select
                  class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md"
                >
                  <option>简体中文</option>
                  <option>English</option>
                </select>
              </div>
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-medium text-gray-900">通知设置</h3>
                  <p class="text-sm text-gray-500">管理您接收的通知类型</p>
                </div>
                <router-link
                  to="/account/notifications"
                  class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                >
                  设置
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useAccountStore } from '../stores/account'

const accountStore = useAccountStore()

onMounted(() => {
  accountStore.initialize()
})
</script>
