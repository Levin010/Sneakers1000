import { defineStore } from 'pinia'
import { ref, reactive, computed } from 'vue'

export const useMainStore = defineStore('main', () => {
  // 🛒 Cart state
  const cart = reactive({
    items: JSON.parse(localStorage.getItem('cart'))?.items || []
  })

  // 🔐 Auth state
  const token = ref(localStorage.getItem('token') || '')
  const isAuthenticated = computed(() => !!token.value)

  // ⏳ Loading state
  const isLoading = ref(false)

  // 🧠 Actions
  function initializeStore() {
    const cartData = localStorage.getItem('cart')
    if (cartData) {
      cart.items = JSON.parse(cartData).items || []
    } else {
      cart.items = []
    }

    const storedToken = localStorage.getItem('token')
    token.value = storedToken || ''
  }

  function addToCart(item) {
    const existing = cart.items.find(i => i.sneaker.id === item.sneaker.id)
    if (existing) {
      existing.quantity = parseInt(existing.quantity) + parseInt(item.quantity)
    } else {
      cart.items.push(item)
    }
    localStorage.setItem('cart', JSON.stringify({ items: cart.items }))
  }

  function clearCart() {
    cart.items = []
    localStorage.setItem('cart', JSON.stringify({ items: [] }))
  }

  function setIsLoading(status) {
    isLoading.value = status
  }

  function setToken(newToken) {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  function removeToken() {
    token.value = ''
    localStorage.removeItem('token')
  }

  return {
    // State
    cart,
    token,
    isAuthenticated,
    isLoading,

    // Actions
    initializeStore,
    addToCart,
    clearCart,
    setIsLoading,
    setToken,
    removeToken
  }
})
