import { defineStore } from 'pinia'

export const useLoadingStore = defineStore('loading', {
  state: () => ({
    isLoading: false
  }),
  actions: {
    setIsLoading(value) {
      this.isLoading = value
    }
  }
})