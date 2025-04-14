<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <!-- 返回按钮 -->
    <button 
      @click="router.back()"
      class="flex items-center text-gray-600 hover:text-gray-900 mb-8"
    >
      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
      Back to Installation
    </button>

    <!-- 标题 -->
    <div class="text-center mb-12">
      <h1 class="text-3xl font-bold text-gray-900">Mounting Height Result<sup class="text-sm bg-purple-500 text-white px-1 rounded ml-1">AI</sup></h1>
      <p class="text-gray-600 mt-2">Optimal TV mounting height calculation based on your inputs</p>
    </div>

    <div class="grid grid-cols-2 gap-8">
      <!-- 左侧：计算结果 -->
      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-lg font-medium text-gray-900 mb-6">Calculation Results</h2>
        <div class="space-y-6">
          <!-- 推荐高度 -->
          <div class="text-center p-6 bg-blue-50 rounded-lg">
            <div class="text-sm text-blue-600 mb-2">Recommended Mounting Height</div>
            <div class="text-4xl font-bold text-blue-700">{{ calculateOptimalHeight() }} cm</div>
            <div class="text-sm text-blue-600 mt-2">from floor to bottom edge of TV</div>
          </div>

          <!-- 输入参数摘要 -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <div class="text-sm text-gray-500">TV Size</div>
              <div class="font-medium">{{ tvInfo.size }}"</div>
            </div>
            <div>
              <div class="text-sm text-gray-500">Viewing Distance</div>
              <div class="font-medium">{{ viewingDistance }} m</div>
            </div>
            <div>
              <div class="text-sm text-gray-500">Wall Height</div>
              <div class="font-medium">{{ wallHeight }} cm</div>
            </div>
            <div>
              <div class="text-sm text-gray-500">Mounting Distance</div>
              <div class="font-medium">{{ mountingDistance }} mm</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：安装示意图 -->
      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-lg font-medium text-gray-900 mb-6">Installation Guide</h2>
        <div class="aspect-video bg-gray-100 rounded-lg flex items-center justify-center mb-6">
          <div class="relative w-full h-full">
            <!-- 墙壁示意图 -->
            <div class="absolute inset-0 bg-gray-200"></div>
            <!-- 电视机示意图 -->
            <div class="absolute" :style="tvPositionStyle">
              <div class="border-4 border-gray-300 rounded-lg bg-white" :style="tvSizeStyle"></div>
            </div>
            <!-- 测量线 -->
            <div class="absolute left-1/2 transform -translate-x-1/2 w-1 bg-red-500 border-l-2 border-dashed border-red-500"
                 :style="measureLineStyle"></div>
          </div>
        </div>

        <!-- 安装提示 -->
        <div class="space-y-4">
          <h3 class="font-medium text-gray-900">Installation Tips:</h3>
          <ul class="list-disc list-inside space-y-2 text-sm text-gray-600">
            <li>Mark the recommended height on your wall</li>
            <li>Use a level to ensure straight mounting</li>
            <li>Verify wall material and use appropriate anchors</li>
            <li>Double-check all measurements before drilling</li>
            <li>Consider cable management solutions</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 操作按钮 -->
    <div class="flex justify-end mt-8 space-x-4">
      <button 
        @click="downloadGuide"
        class="px-6 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
      >
        Download Guide
      </button>
      <button 
        @click="router.push('/tv-mount')"
        class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
      >
        Start Over
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// 获取从上一页传递的数据
const tvInfo = computed(() => route.state?.tvModel || {})
const mountingDistance = computed(() => route.state?.mountingDistance || 0)
const wallHeight = computed(() => route.state?.wallHeight || 0)
const viewingDistance = computed(() => route.state?.viewingDistance || 0)

// 计算最佳观看高度
const calculateOptimalHeight = () => {
  // 这里使用简化的计算公式，实际可能需要更复杂的计算
  const screenHeight = (parseInt(tvInfo.value.size) * 24.5) / Math.sqrt(337) // 近似计算屏幕高度(cm)
  const viewingAngle = 15 // 理想观看角度（度）
  const optimalHeight = viewingDistance.value * Math.tan(viewingAngle * Math.PI / 180) + 120 // 120cm 是平均坐姿高度
  return Math.round(optimalHeight)
}

// 计算电视机位置和尺寸样式
const tvSizeStyle = computed(() => {
  const width = '75%'
  const height = '50%'
  return {
    width,
    height,
  }
})

const tvPositionStyle = computed(() => {
  const optimalHeight = calculateOptimalHeight()
  const top = `${(100 - (optimalHeight / wallHeight.value * 100))}%`
  return {
    top,
    left: '50%',
    transform: 'translate(-50%, -50%)',
  }
})

const measureLineStyle = computed(() => {
  const optimalHeight = calculateOptimalHeight()
  const height = `${optimalHeight / wallHeight.value * 100}%`
  const bottom = '0'
  return {
    height,
    bottom,
  }
})

// 下载安装指南
const downloadGuide = () => {
  // TODO: 实现下载功能
  console.log('Downloading installation guide...')
}
</script>

<style scoped>
.shadow {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}
</style> 