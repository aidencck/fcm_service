<template>
  <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
    <div class="px-4 py-6 sm:px-0">
      <div class="bg-white dark:bg-gray-800 shadow rounded-lg">
        <div class="px-4 py-5 sm:p-6">
          <div class="flex items-center space-x-4">
            <img
              :src="userInfo?.avatar || '/default-avatar.png'"
              alt="User Avatar"
              class="h-16 w-16 rounded-full"
            />
            <div>
              <h3 class="text-lg font-medium text-gray-900 dark:text-white">
                {{ userInfo?.username }}
              </h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                {{ userInfo?.email }}
              </p>
            </div>
          </div>

          <div class="mt-6 border-t border-gray-200 dark:border-gray-700">
            <dl class="divide-y divide-gray-200 dark:divide-gray-700">
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4">
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400">
                  用户名
                </dt>
                <dd class="mt-1 text-sm text-gray-900 dark:text-white sm:mt-0 sm:col-span-2">
                  {{ userInfo?.username }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4">
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400">
                  邮箱
                </dt>
                <dd class="mt-1 text-sm text-gray-900 dark:text-white sm:mt-0 sm:col-span-2">
                  {{ userInfo?.email }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4">
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400">
                  角色
                </dt>
                <dd class="mt-1 text-sm text-gray-900 dark:text-white sm:mt-0 sm:col-span-2">
                  <span
                    v-for="role in userInfo?.roles"
                    :key="role"
                    class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-light text-primary-dark mr-2"
                  >
                    {{ role }}
                  </span>
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4">
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400">
                  权限
                </dt>
                <dd class="mt-1 text-sm text-gray-900 dark:text-white sm:mt-0 sm:col-span-2">
                  <span
                    v-for="permission in userInfo?.permissions"
                    :key="permission"
                    class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2"
                  >
                    {{ permission }}
                  </span>
                </dd>
              </div>
            </dl>
          </div>

          <div class="mt-6 flex space-x-4">
            <router-link
              to="/profile/edit"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            >
              编辑资料
            </router-link>
            <router-link
              to="/profile/change-password"
              class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-700 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            >
              修改密码
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useUserStore } from '@/stores'

const userStore = useUserStore()
const userInfo = computed(() => userStore.userInfo)
</script> 