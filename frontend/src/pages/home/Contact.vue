<template>
  <div class="bg-white py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-16 items-center">
        <!-- Contact Info -->
        <div>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">联系我们</h2>
          <p class="text-xl text-gray-600 mb-8">
            无论您有任何问题或需求，我们都随时准备为您提供帮助和支持。
          </p>

          <div class="space-y-6">
            <div class="flex items-start">
              <div class="flex-shrink-0">
                <svg
                  class="w-6 h-6 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div class="ml-4">
                <h3 class="text-lg font-medium text-gray-900">电子邮件</h3>
                <p class="mt-1 text-gray-600">support@example.com</p>
              </div>
            </div>

            <div class="flex items-start">
              <div class="flex-shrink-0">
                <svg
                  class="w-6 h-6 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                  />
                </svg>
              </div>
              <div class="ml-4">
                <h3 class="text-lg font-medium text-gray-900">电话</h3>
                <p class="mt-1 text-gray-600">+86 400-123-4567</p>
              </div>
            </div>

            <div class="flex items-start">
              <div class="flex-shrink-0">
                <svg
                  class="w-6 h-6 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
              </div>
              <div class="ml-4">
                <h3 class="text-lg font-medium text-gray-900">地址</h3>
                <p class="mt-1 text-gray-600">北京市朝阳区xxx大厦</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="bg-gray-50 rounded-xl p-8 shadow-md">
          <form class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-1">姓名</label>
              <input
                type="text"
                id="name"
                name="name"
                class="mt-1 block w-full rounded-lg border-gray-200 px-4 py-3 shadow-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition duration-150 ease-in-out"
                placeholder="请输入您的姓名"
              />
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-1">邮箱</label>
              <input
                type="email"
                id="email"
                name="email"
                class="mt-1 block w-full rounded-lg border-gray-200 px-4 py-3 shadow-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition duration-150 ease-in-out"
                placeholder="请输入您的邮箱地址"
              />
            </div>

            <div>
              <label for="subject" class="block text-sm font-medium text-gray-700 mb-1">主题</label>
              <input
                type="text"
                id="subject"
                name="subject"
                class="mt-1 block w-full rounded-lg border-gray-200 px-4 py-3 shadow-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition duration-150 ease-in-out"
                placeholder="请输入主题"
              />
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 mb-1">消息</label>
              <textarea
                id="message"
                name="message"
                rows="4"
                class="mt-1 block w-full rounded-lg border-gray-200 px-4 py-3 shadow-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition duration-150 ease-in-out resize-none"
                placeholder="请输入您的消息"
              ></textarea>
            </div>

            <div>
              <button
                type="submit"
                class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition duration-150 ease-in-out"
              >
                发送消息
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Component logic here
</script>
