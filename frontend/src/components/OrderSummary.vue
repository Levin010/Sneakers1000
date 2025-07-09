<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

        <h4 class="is-size-5">Sneakers</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Sneaker</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.sneaker.id"
                >
                    <td>{{ item.sneaker.name }}</td>
                    <td>KES {{ item.sneaker.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>KES {{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
const props = defineProps({
  order: Object
})

const getItemTotal = (item) => {
  return item.quantity * item.sneaker.price
}

const orderTotalLength = (order) => {
  return order.items.reduce((acc, curVal) => acc + curVal.quantity, 0)
}
</script>
