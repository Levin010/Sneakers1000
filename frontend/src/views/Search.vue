<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>

                <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
            </div>

            <SneakerBox 
                v-for="sneaker in sneakers"
                v-bind:key="sneaker.id"
                v-bind:sneaker="sneaker" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SneakerBox from '@/components/SneakerBox.vue'
import { useMainStore } from '@/stores'

const mainStore = useMainStore()

const sneakers = ref([])
const query = ref('')

const performSearch = async () => {
  mainStore.setIsLoading(true)

  try {
    const response = await axios.post('/api/v1/sneakers/search/', {
      query: query.value
    })
    sneakers.value = response.data
  } catch (error) {
    console.error(error)
  }

  mainStore.setIsLoading(false)
}

onMounted(() => {
  document.title = 'Search | SNEAKERS1000'

  const uri = window.location.search.substring(1)
  const params = new URLSearchParams(uri)

  const searchQuery = params.get('query')
  if (searchQuery) {
    query.value = searchQuery
    performSearch()
  }
})
</script>
