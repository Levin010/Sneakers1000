<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Sneakers1000
            </p>
            <p class="subtitle">
                The best sneaker store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest sneakers</h2>
      </div>

      <SneakerBox 
        v-for="sneaker in latestSneakers"
        v-bind:key="sneaker.id"
        v-bind:sneaker="sneaker" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SneakerBox from '@/components/SneakerBox.vue'
import { useLoadingStore } from '@/stores/loading'

export default {
  name: 'Home',
  components: {
    SneakerBox
  },
  data() {
    return {
      latestSneakers: []
    }
  },
  mounted() {
    this.getLatestSneakers()
    document.title = 'Home | Sneakers1000'
  },
  methods: {
    async getLatestSneakers() {
      const loading = useLoadingStore()
      loading.setIsLoading(true)

      try {
        const response = await axios.get('/api/v1/latest-sneakers/')
        this.latestSneakers = response.data
      } catch (error) {
        console.log(error)
      }

      loading.setIsLoading(false)
    }
  }
}
</script>
