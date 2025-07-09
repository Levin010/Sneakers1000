<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useMainStore } from '@/stores'
import OrderSummary from '@/components/OrderSummary.vue'

const router = useRouter()
const store = useMainStore()

const orders = ref([])

const logout = () => {
  axios.defaults.headers.common["Authorization"] = ""

  localStorage.removeItem("token")
  localStorage.removeItem("username")
  localStorage.removeItem("userid")

  store.removeToken()

  router.push('/')
}

const getMyOrders = async () => {
  store.setIsLoading(true)

  await axios
    .get('/api/v1/orders/')
    .then(response => {
      orders.value = response.data
    })
    .catch(error => {
      console.log(error)
    })

  store.setIsLoading(false)
}

onMounted(() => {
  document.title = 'My account | SNEAKERS1000'
  getMyOrders()
})
</script>
