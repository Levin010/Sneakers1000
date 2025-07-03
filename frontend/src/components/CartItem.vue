<template>
    <tr>
        <td><router-link :to="item.sneaker.get_absolute_url">{{ item.sneaker.name }}</router-link></td>
        <td>KES {{ item.sneaker.price }}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">-</a>
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>KES {{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'
import { useMainStore } from '@/stores'

const props = defineProps({
  initialItem: Object
})

const emit = defineEmits(['removeFromCart'])

const mainStore = useMainStore()

const item = ref(props.initialItem)

const getItemTotal = (item) => {
  return item.quantity * item.sneaker.price
}

const decrementQuantity = (item) => {
  item.quantity -= 1

  if (item.quantity === 0) {
    emit('removeFromCart', item)
  }

  updateCart()
}

const incrementQuantity = (item) => {
  item.quantity += 1
  updateCart()
}

const updateCart = () => {
  localStorage.setItem('cart', JSON.stringify(mainStore.cart))
}

const removeFromCart = (item) => {
  emit('removeFromCart', item)
  updateCart()
}
</script>
