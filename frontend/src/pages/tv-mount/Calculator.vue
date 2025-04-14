<template>
  <div class="max-w-6xl mx-auto px-3 py-4">
    <!-- 标题 -->
    <div class="text-center mb-6">
      <h1 class="text-lg font-bold text-gray-900">TV Mount<sup class="text-xs bg-purple-500 text-white px-1 rounded ml-1">AI</sup></h1>
      <p class="text-xs text-gray-600 mt-2">Ergonomically based smart choice TV mount installation is highly recommended, your TV starts</p>
    </div>

    <!-- 搜索框 -->
    <div class="relative mb-4">
      <input 
        type="text" 
        v-model="searchQuery"
        placeholder="Search TV Model"
        class="w-full h-10 px-3 pl-9 text-sm border border-gray-200 rounded-lg focus:ring-1 focus:ring-blue-500 focus:border-blue-500"
      />
      <span class="absolute left-3 top-3 text-gray-400">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
      </span>
    </div>

    <!-- 品牌选择 -->
    <div class="mb-4">
      <h2 class="text-sm font-medium text-gray-900 mb-2">Select Your TV Brand</h2>
      <div class="grid grid-cols-3 gap-2">
        <button 
          v-for="brand in brands" 
          :key="brand.name"
          @click="selectBrand(brand.name)"
          :class="[
            'px-2 py-2 rounded-lg border text-center transition-colors',
            selectedBrand === brand.name ? 'border-blue-500 bg-blue-50 text-blue-700' : 'border-gray-200 text-gray-700'
          ]"
        >
          <span class="text-xs">{{ brand.name }}</span>
        </button>
      </div>
      <button 
        class="w-full mt-2 px-3 py-2 text-xs text-left text-gray-600 border border-gray-200 rounded-lg"
      >
        Other Brands
      </button>
    </div>

    <!-- 尺寸选择 -->
    <div class="mb-4">
      <h2 class="text-sm font-medium text-gray-900 mb-2">Select Your TV Size</h2>
      <div class="grid grid-cols-4 gap-2">
        <button 
          v-for="size in tvSizes" 
          :key="size"
          @click="selectSize(size)"
          :class="[
            'px-2 py-2 rounded-lg border text-center transition-colors',
            selectedSize === size ? 'border-blue-500 bg-blue-50 text-blue-700' : 'border-gray-200 text-gray-700'
          ]"
        >
          <span class="text-xs">{{ size }}"</span>
        </button>
      </div>
      <button 
        class="w-full mt-2 px-3 py-2 text-xs text-left text-gray-600 border border-gray-200 rounded-lg"
      >
        Other Size
      </button>
    </div>

    <!-- 电视型号列表 -->
    <div class="bg-white rounded-lg border border-gray-200">
      <!-- 列表内容 -->
      <div class="divide-y divide-gray-200">
        <div 
          v-for="model in tvModels" 
          :key="model.id"
          class="flex items-center p-3 hover:bg-gray-50"
        >
          <!-- 图片 -->
          <div class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mr-3">
            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>

          <!-- 型号信息 -->
          <div class="flex-1 min-w-0">
            <div class="text-sm font-medium text-gray-900 truncate">{{ model.brand }}</div>
            <div class="text-xs text-gray-500 mt-0.5 font-mono truncate">{{ model.model }}</div>
            <div class="flex items-center mt-0.5 text-xs text-gray-500">
              <span>{{ model.size }}"</span>
              <span class="mx-1.5">•</span>
              <span>{{ model.aspectRatio }}</span>
            </div>
          </div>

          <!-- 选择按钮 -->
          <button 
            @click="goToInstallation(model)"
            class="ml-3 w-8 h-8 flex items-center justify-center bg-gray-900 text-white rounded-lg"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 搜索查询
const searchQuery = ref('')

// 品牌选择
const selectedBrand = ref('')
const brands = [
  { name: 'SAMSUNG' },
  { name: 'SONY' },
  { name: 'LG' },
  { name: 'TCL' },
  { name: 'ROKU' },
  { name: 'PHILIPS' }
]

// 尺寸选择
const selectedSize = ref('')
const tvSizes = ['75', '65', '60', '55', '46', '40', '32', '24']

// 电视型号数据
const tvModels = [
  {
    id: 1,
    brand: 'Samsung',
    model: 'QE65QN93CATXXU',
    size: '100',
    aspectRatio: '16:9'
  },
  {
    id: 2,
    brand: 'Samsung',
    model: 'UE32T4300AEXXU',
    size: '100',
    aspectRatio: '16:9'
  },
  {
    id: 3,
    brand: 'Samsung',
    model: 'QE65QBUUHOOTR',
    size: '100',
    aspectRatio: '16:9'
  },
  {
    id: 4,
    brand: 'Samsung',
    model: 'QE65QN93CATXXU',
    size: '100',
    aspectRatio: '16:9'
  },
  {
    id: 5,
    brand: 'Samsung',
    model: 'QE65QN93CATXXU',
    size: '100',
    aspectRatio: '16:9'
  }
]

// 选择品牌
const selectBrand = (brand: string) => {
  selectedBrand.value = brand
}

// 选择尺寸
const selectSize = (size: string) => {
  selectedSize.value = size
}

// 跳转到安装页面
const goToInstallation = (model: typeof tvModels[0]) => {
  router.push({
    name: 'installation',
    params: { id: model.id },
    state: { model }
  })
}
</script>

<style scoped>
/* 移除不需要的动画样式 */
</style> 