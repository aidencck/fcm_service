<template>
  <div class="bg-gray-50 py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
          成功案例
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          看看其他企业是如何使用我们的平台来构建他们的应用程序
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Case 1 -->
        <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow">
          <div class="aspect-video bg-gradient-to-br from-blue-50 to-blue-100 relative flex items-center justify-center">
            <div class="text-blue-600">
              <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z" />
              </svg>
            </div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-2">智能家居控制系统</h3>
            <p class="text-gray-600 mb-4">
              使用 Firebase 和 AI 技术打造的新一代智能家居控制系统，为用户提供更智能、更便捷的居家体验。
            </p>
            <div class="flex items-center text-sm text-gray-500">
              <span class="mr-4">⭐ 4.9/5 评分</span>
              <span>📱 100万+ 用户</span>
            </div>
          </div>
        </div>

        <!-- Case 2 -->
        <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow">
          <div class="aspect-video bg-gradient-to-br from-green-50 to-green-100 relative flex items-center justify-center">
            <div class="text-green-600">
              <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-2">企业数据分析平台</h3>
            <p class="text-gray-600 mb-4">
              基于 Firebase 构建的企业级数据分析平台，帮助企业实现数据驱动决策。
            </p>
            <div class="flex items-center text-sm text-gray-500">
              <span class="mr-4">⭐ 4.8/5 评分</span>
              <span>🏢 5000+ 企业用户</span>
            </div>
          </div>
        </div>

        <!-- Case 3 -->
        <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow">
          <div class="aspect-video bg-gradient-to-br from-purple-50 to-purple-100 relative flex items-center justify-center">
            <div class="text-purple-600">
              <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-2">在线教育平台</h3>
            <p class="text-gray-600 mb-4">
              结合 AI 技术的在线教育平台，为学习者提供个性化的学习体验。
            </p>
            <div class="flex items-center text-sm text-gray-500">
              <span class="mr-4">⭐ 4.7/5 评分</span>
              <span>👥 50万+ 学习者</span>
            </div>
          </div>
        </div>
      </div>

      <div class="text-center mt-12">
        <a href="#" class="inline-flex items-center text-blue-600 hover:text-blue-700 font-medium">
          查看更多案例
          <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Component logic here
</script>

<style scoped>
.aspect-video {
  aspect-ratio: 16 / 9;
}
</style> 