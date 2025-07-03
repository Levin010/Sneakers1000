<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Sneaker</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.sneaker.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </tbody>
                </table>

                <p v-else>You don't have any sneakers in your cart...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>

                <strong>KES {{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

                <hr>

                <router-link to="/cart/checkout" class="button is-dark">Proceed to checkout</router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import CartItem from '@/components/CartItem.vue'
import { useMainStore } from '@/stores'

const mainStore = useMainStore()

const cart = mainStore.cart

const removeFromCart = (item) => {
  cart.items = cart.items.filter(i => i.sneaker.id !== item.sneaker.id)
}

const cartTotalLength = computed(() => {
  return cart.items.reduce((acc, curVal) => acc + curVal.quantity, 0)
})

const cartTotalPrice = computed(() => {
  return cart.items.reduce((acc, curVal) => acc + curVal.sneaker.price * curVal.quantity, 0)
})
</script>
