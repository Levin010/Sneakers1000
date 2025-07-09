<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1>

                <p>Your order will be processed within the hour</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  document.title = 'Success | SNEAKERS1000'
})
</script>
