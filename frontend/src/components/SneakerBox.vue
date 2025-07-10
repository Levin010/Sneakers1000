<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="getImageUrl(sneaker.get_thumbnail)">
            </figure>

            <h3 class="is-size-4">{{ sneaker.name }}</h3>
            <p class="is-size-6 has-text-grey">KES{{ sneaker.price }}</p>

            <router-link v-bind:to="sneaker.get_absolute_url" class="button is-dark mt-4">View details</router-link>
        </div>
    </div>
</template>

<script setup>
defineOptions({ name: 'SneakerBox' })

defineProps({
  sneaker: Object
})

const backendURL = import.meta.env.VITE_API_URL

const getImageUrl = (imageUrl) => {
  if (imageUrl && imageUrl.startsWith('http')) {
    return imageUrl
  }
  return `${backendURL}${imageUrl}`
}

</script>


<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>