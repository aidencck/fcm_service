import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface CartItem {
  id: string
  name: string
  price: number
  quantity: number
  image?: string
}

export const useCartStore = defineStore('cart', () => {
  const items = ref<CartItem[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // 计算总价
  const total = computed(() => {
    return items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  })

  // 计算商品总数
  const itemCount = computed(() => {
    return items.value.reduce((sum, item) => sum + item.quantity, 0)
  })

  // 添加商品到购物车
  const addItem = (item: Omit<CartItem, 'quantity'>) => {
    const existingItem = items.value.find(i => i.id === item.id)
    if (existingItem) {
      existingItem.quantity += 1
    } else {
      items.value.push({ ...item, quantity: 1 })
    }
    saveCart()
  }

  // 更新商品数量
  const updateQuantity = (itemId: string, quantity: number) => {
    const item = items.value.find(i => i.id === itemId)
    if (item) {
      if (quantity <= 0) {
        removeItem(itemId)
      } else {
        item.quantity = quantity
      }
      saveCart()
    }
  }

  // 移除商品
  const removeItem = (itemId: string) => {
    items.value = items.value.filter(item => item.id !== itemId)
    saveCart()
  }

  // 清空购物车
  const clearCart = () => {
    items.value = []
    saveCart()
  }

  // 保存购物车到本地存储
  const saveCart = () => {
    localStorage.setItem('cart', JSON.stringify(items.value))
  }

  // 从本地存储加载购物车
  const loadCart = () => {
    const savedCart = localStorage.getItem('cart')
    if (savedCart) {
      items.value = JSON.parse(savedCart)
    }
  }

  return {
    items,
    loading,
    error,
    total,
    itemCount,
    addItem,
    updateQuantity,
    removeItem,
    clearCart,
    loadCart
  }
}) 