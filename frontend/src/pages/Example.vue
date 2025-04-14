<template>
  <div class="p-4">
    <!-- 加载状态 -->
    <div v-if="loading" class="text-center py-4">
      <span class="text-gray-500">加载中...</span>
    </div>

    <!-- 错误提示 -->
    <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
      {{ error }}
    </div>

    <!-- 数据列表 -->
    <div v-if="!isEmpty" class="space-y-4">
      <div v-for="item in data" :key="item.id" class="border rounded p-4">
        <h3 class="text-lg font-semibold">{{ item.name }}</h3>
        <p class="text-gray-600">{{ item.description }}</p>
        <div class="mt-2 flex space-x-2">
          <button
            @click="handleEdit(item)"
            class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            编辑
          </button>
          <button
            @click="handleDelete(item.id)"
            class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
          >
            删除
          </button>
        </div>
      </div>
    </div>

    <!-- 空状态 -->
    <div v-else class="text-center py-8 text-gray-500">暂无数据</div>

    <!-- 创建表单 -->
    <div class="mt-8">
      <h2 class="text-xl font-semibold mb-4">创建新项目</h2>
      <form @submit.prevent="handleCreate" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">名称</label>
          <input
            v-model="newItem.name"
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            required
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">描述</label>
          <textarea
            v-model="newItem.description"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            rows="3"
            required
          ></textarea>
        </div>
        <button type="submit" class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
          创建
        </button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useExampleStore } from '../stores/example'
import type { ExampleData } from '../stores/example'

const store = useExampleStore()

// 状态
const loading = computed(() => store.loading)
const error = computed(() => store.error)
const data = computed(() => store.data)
const isEmpty = computed(() => store.isEmpty)

// 新项目表单
const newItem = ref({
  name: '',
  description: ''
})

// 生命周期钩子
onMounted(async () => {
  await store.fetchData()
})

// 方法
const handleCreate = async () => {
  try {
    await store.createItem(newItem.value)
    newItem.value = { name: '', description: '' }
  } catch (error) {
    console.error('创建失败:', error)
  }
}

const handleEdit = async (item: ExampleData) => {
  try {
    await store.fetchItem(item.id)
    // 这里可以打开编辑模态框或跳转到编辑页面
  } catch (error) {
    console.error('获取详情失败:', error)
  }
}

const handleDelete = async (id: string) => {
  if (confirm('确定要删除吗？')) {
    try {
      await store.deleteItem(id)
    } catch (error) {
      console.error('删除失败:', error)
    }
  }
}
</script>
