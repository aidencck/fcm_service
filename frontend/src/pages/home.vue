<template>
  <div class="space-y-12">
    <!-- 英雄区域 -->
    <section class="relative bg-white dark:bg-gray-900 overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="relative z-10 pb-8 bg-white dark:bg-gray-900 sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
          <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
            <div class="sm:text-center lg:text-left">
              <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white sm:text-5xl md:text-6xl">
                <span class="block">构建现代化的</span>
                <span class="block text-primary">Web 应用</span>
              </h1>
              <p class="mt-3 text-base text-gray-500 dark:text-gray-400 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                使用 Vue 3、TypeScript 和 Tailwind CSS 构建高性能、可扩展的 Web 应用。我们的框架提供了完整的开发体验，包括路由、状态管理、主题切换等功能。
              </p>
              <div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
                <div class="rounded-md shadow">
                  <router-link
                    to="/docs"
                    class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primary-dark md:py-4 md:text-lg md:px-10"
                  >
                    开始使用
                  </router-link>
                </div>
                <div class="mt-3 sm:mt-0 sm:ml-3">
                  <router-link
                    to="/features"
                    class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-primary bg-primary-light hover:bg-primary-lighter md:py-4 md:text-lg md:px-10"
                  >
                    了解更多
                  </router-link>
                </div>
              </div>
            </div>
          </main>
        </div>
      </div>
      <div class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
        <img
          class="h-56 w-full object-cover sm:h-72 md:h-96 lg:w-full lg:h-full"
          src="@/assets/hero-image.jpg"
          alt="Hero Image"
        />
      </div>
    </section>

    <!-- 特性区域 -->
    <section class="py-12 bg-gray-50 dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:text-center">
          <h2 class="text-base text-primary font-semibold tracking-wide uppercase">特性</h2>
          <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 dark:text-white sm:text-4xl">
            为什么选择我们？
          </p>
          <p class="mt-4 max-w-2xl text-xl text-gray-500 dark:text-gray-400 lg:mx-auto">
            我们提供了一系列强大的特性，帮助您快速构建现代化的 Web 应用。
          </p>
        </div>

        <div class="mt-10">
          <div class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
            <div v-for="feature in features" :key="feature.name" class="relative">
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-primary text-white">
                <component :is="feature.icon" class="h-6 w-6" />
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900 dark:text-white">
                {{ feature.name }}
              </p>
              <p class="mt-2 ml-16 text-base text-gray-500 dark:text-gray-400">
                {{ feature.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 价格区域 -->
    <section class="py-12 bg-white dark:bg-gray-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:text-center">
          <h2 class="text-base text-primary font-semibold tracking-wide uppercase">价格</h2>
          <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 dark:text-white sm:text-4xl">
            选择适合您的计划
          </p>
          <p class="mt-4 max-w-2xl text-xl text-gray-500 dark:text-gray-400 lg:mx-auto">
            我们提供灵活的价格计划，满足不同规模团队的需求。
          </p>
        </div>

        <div class="mt-12 space-y-4 sm:mt-16 sm:space-y-0 sm:grid sm:grid-cols-2 sm:gap-6 lg:max-w-4xl lg:mx-auto xl:max-w-none xl:mx-0 xl:grid-cols-3">
          <div v-for="plan in plans" :key="plan.name" class="border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm divide-y divide-gray-200 dark:divide-gray-700">
            <div class="p-6">
              <h2 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">
                {{ plan.name }}
              </h2>
              <p class="mt-4 text-sm text-gray-500 dark:text-gray-400">
                {{ plan.description }}
              </p>
              <p class="mt-8">
                <span class="text-4xl font-extrabold text-gray-900 dark:text-white">
                  {{ plan.price }}
                </span>
                <span class="text-base font-medium text-gray-500 dark:text-gray-400">
                  /月
                </span>
              </p>
              <router-link
                :to="plan.href"
                class="mt-8 block w-full bg-primary border border-transparent rounded-md py-2 text-sm font-semibold text-white text-center hover:bg-primary-dark"
              >
                开始使用
              </router-link>
            </div>
            <div class="pt-6 pb-8 px-6">
              <h3 class="text-xs font-medium text-gray-900 dark:text-white tracking-wide uppercase">
                包含的功能
              </h3>
              <ul class="mt-6 space-y-4">
                <li v-for="feature in plan.features" :key="feature" class="flex space-x-3">
                  <svg class="flex-shrink-0 h-5 w-5 text-green-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span class="text-sm text-gray-500 dark:text-gray-400">
                    {{ feature }}
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 特性列表
const features = ref([
  {
    name: 'Vue 3 和 TypeScript',
    description: '使用最新的 Vue 3 和 TypeScript 构建类型安全的应用程序。',
    icon: 'CodeIcon',
  },
  {
    name: '响应式设计',
    description: '使用 Tailwind CSS 构建完全响应式的用户界面。',
    icon: 'DeviceMobileIcon',
  },
  {
    name: '主题切换',
    description: '支持亮色和暗色主题，提供更好的用户体验。',
    icon: 'SunIcon',
  },
  {
    name: '状态管理',
    description: '使用 Pinia 进行状态管理，提供更好的开发体验。',
    icon: 'DatabaseIcon',
  },
])

// 价格计划
const plans = ref([
  {
    name: '基础版',
    description: '适合个人开发者和小型团队。',
    price: '$9',
    href: '/pricing/basic',
    features: [
      '基础功能',
      '社区支持',
      '每月更新',
      '基础文档',
    ],
  },
  {
    name: '专业版',
    description: '适合中型团队和创业公司。',
    price: '$29',
    href: '/pricing/pro',
    features: [
      '所有基础功能',
      '优先支持',
      '每周更新',
      '完整文档',
      '团队协作',
    ],
  },
  {
    name: '企业版',
    description: '适合大型企业和组织。',
    price: '$99',
    href: '/pricing/enterprise',
    features: [
      '所有专业功能',
      '24/7 支持',
      '每日更新',
      '定制开发',
      '专属培训',
      'SLA 保障',
    ],
  },
])
</script> 