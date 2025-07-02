<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="sneaker.get_image">
                </figure>

                <h1 class="title">{{ sneaker.name }}</h1>

                <p>{{ sneaker.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle mb-3">Product Details</h2>

                <p><strong>Price: </strong>KES{{ sneaker.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMainStore } from '@/stores'
import { useRoute } from 'vue-router'

const sneaker = ref({})
const quantity = ref(1)

const mainStore = useMainStore()
const route = useRoute()

const getSneaker = async () => {
  mainStore.setIsLoading(true)

  const category_slug = route.params.category_slug
  const sneaker_slug = route.params.sneaker_slug

  try {
    const response = await axios.get(`/api/v1/sneakers/${category_slug}/${sneaker_slug}`)
    sneaker.value = response.data
    document.title = sneaker.value.name + ' | Sneakers1000'
  } catch (error) {
    console.log(error)
  }

  mainStore.setIsLoading(false)
}

onMounted(() => {
  getSneaker()
})
</script>
