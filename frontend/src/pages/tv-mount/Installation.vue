<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <!-- 返回按钮 -->
    <button @click="router.back()" class="flex items-center text-gray-600 hover:text-gray-900 mb-8">
      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M10 19l-7-7m0 0l7-7m-7 7h18"
        />
      </svg>
      Back to TV Selection
    </button>

    <!-- 标题 -->
    <div class="text-center mb-12">
      <h1 class="text-3xl font-bold text-gray-900">
        TV Mount Installation<sup class="text-sm bg-purple-500 text-white px-1 rounded ml-1"
          >AI</sup
        >
      </h1>
      <p class="text-gray-600 mt-2">
        Configure your TV mount installation settings for optimal viewing experience
      </p>
    </div>

    <div class="grid grid-cols-2 gap-8">
      <!-- 左侧：电视信息 -->
      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-lg font-medium text-gray-900 mb-6">Selected TV Information</h2>
        <div class="space-y-6">
          <div class="flex items-center">
            <div class="w-32 h-32 bg-gray-100 rounded-lg flex items-center justify-center mr-6">
              <svg
                class="w-20 h-20 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                />
              </svg>
            </div>
            <div class="flex-1">
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <div class="text-sm text-gray-500">Brand</div>
                  <div class="font-medium text-lg">{{ tvModel?.brand || '-' }}</div>
                </div>
                <div>
                  <div class="text-sm text-gray-500">Model</div>
                  <div class="font-mono text-lg">{{ tvModel?.model || '-' }}</div>
                </div>
                <div>
                  <div class="text-sm text-gray-500">Screen Size</div>
                  <div class="font-medium text-lg">{{ tvModel?.size || '-' }}"</div>
                </div>
                <div>
                  <div class="text-sm text-gray-500">Aspect Ratio</div>
                  <div class="font-medium text-lg">{{ tvModel?.aspectRatio || '-' }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：安装位置配置 -->
      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-lg font-medium text-gray-900 mb-6">Installation Configuration</h2>

        <!-- 安装位置图 -->
        <div class="aspect-video bg-gray-100 rounded-lg flex items-center justify-center mb-6">
          <div class="relative w-full h-full">
            <!-- 墙壁示意图 -->
            <div class="absolute inset-0 bg-gray-200"></div>
            <!-- 电视机示意图 -->
            <div
              class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-3/4 h-1/2 border-4 border-gray-300 rounded-lg bg-white"
            ></div>
            <!-- 安装点 -->
            <div
              class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 grid grid-cols-2 gap-16"
            >
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
            </div>
            <!-- 测量线 -->
            <div
              class="absolute bottom-1/4 left-1/2 transform -translate-x-1/2 w-1 h-16 bg-red-500 border-l-2 border-dashed border-red-500"
            ></div>
          </div>
        </div>

        <!-- 测量输入 -->
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">
              Distance from Bottom Edge to Mounting Holes (mm)
            </label>
            <input
              type="number"
              v-model="mountingDistance"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Enter distance in millimeters"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"> Wall Height (cm) </label>
            <input
              type="number"
              v-model="wallHeight"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Enter wall height in centimeters"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">
              Viewing Distance (m)
            </label>
            <input
              type="number"
              v-model="viewingDistance"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Enter viewing distance in meters"
            />
          </div>
        </div>

        <!-- 提示信息 -->
        <p class="text-sm text-gray-600 mt-6">
          Please measure the distance between the bottom mounting holes and the bottom edge of your
          TV according to the diagram above. This will help us calculate the optimal mounting height
          for your viewing experience.
        </p>
      </div>
    </div>

    <!-- 操作按钮 -->
    <div class="flex justify-end mt-8">
      <button
        @click="calculateMountingHeight"
        class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
        :disabled="!isFormValid"
      >
        Calculate Mounting Height
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// 模拟测试数据
const mockTvModel = {
  brand: 'Samsung',
  model: 'QN65Q80B',
  size: 65,
  aspectRatio: '16:9',
  weight: '28.1 kg',
  image: '/images/tv/samsung-q80b.jpg'
}

// 获取从上一页传递的电视型号信息，如果没有则使用测试数据
const tvModel = computed(() => route.state?.model || mockTvModel)

// 表单数据 - 添加默认测试值
const mountingDistance = ref('200') // 默认200mm
const wallHeight = ref('280') // 默认280cm
const viewingDistance = ref('3.5') // 默认3.5m

// 表单验证
const isFormValid = computed(() => {
  return mountingDistance.value && wallHeight.value && viewingDistance.value
})

// 计算安装高度
const calculateMountingHeight = () => {
  // TODO: 实现计算逻辑
  router.push({
    name: 'mounting-result',
    state: {
      tvModel: tvModel.value,
      mountingDistance: mountingDistance.value,
      wallHeight: wallHeight.value,
      viewingDistance: viewingDistance.value
    }
  })
}
</script>

<style scoped>
.shadow {
  box-shadow:
    0 1px 3px 0 rgba(0, 0, 0, 0.1),
    0 1px 2px 0 rgba(0, 0, 0, 0.06);
}

input[type='number']::-webkit-inner-spin-button,
input[type='number']::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type='number'] {
  -moz-appearance: textfield;
}
</style>
