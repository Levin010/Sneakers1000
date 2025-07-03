<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>

            <SneakerBox 
                v-for="sneaker in category.sneakers"
                v-bind:key="sneaker.id"
                v-bind:sneaker="sneaker" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { toast } from 'bulma-toast'

import SneakerBox from '@/components/SneakerBox.vue'
import { useMainStore } from '@/stores'

const mainStore = useMainStore()
const route = useRoute()

const category = ref({
  sneakers: []
})

const getCategory = async () => {
  const categorySlug = route.params.category_slug

  mainStore.setIsLoading(true)

  try {
    const response = await axios.get(`/api/v1/sneakers/${categorySlug}/`)
    category.value = response.data

    document.title = `${category.value.name} | SNEAKERS1000`
  } catch (error) {
    console.error(error)

    toast({
      message: 'Something went wrong. Please try again.',
      type: 'is-danger',
      dismissible: true,
      pauseOnHover: true,
      duration: 2000,
      position: 'bottom-right',
    })
  }

  mainStore.setIsLoading(false)
}

onMounted(() => {
  getCategory()
})

// Watch for route change to re-fetch category
watch(
  () => route.name,
  (to) => {
    if (to === 'Category') {
      getCategory()
    }
  }
)
</script>
