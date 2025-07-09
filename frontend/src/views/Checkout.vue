<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
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
                            v-for="item in cart.items"
                            v-bind:key="item.sneaker.id"
                        >
                            <td>{{ item.sneaker.name }}</td>
                            <td>${{ item.sneaker.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zip code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMainStore } from '@/stores'
import axios from 'axios'

const store = useMainStore()
const router = useRouter()

const cart = ref({
  items: []
})

const stripe = ref({})
const card = ref({})

const first_name = ref('')
const last_name = ref('')
const email = ref('')
const phone = ref('')
const address = ref('')
const zipcode = ref('')
const place = ref('')
const errors = ref([])

const cartTotalPrice = computed(() => {
  return cart.value.items.reduce((acc, curVal) => {
    return acc + curVal.sneaker.price * curVal.quantity
  }, 0)
})

const cartTotalLength = computed(() => {
  return cart.value.items.reduce((acc, curVal) => {
    return acc + curVal.quantity
  }, 0)
})

onMounted(() => {
  document.title = 'Checkout | SNEAKER1000'

  cart.value = store.cart

  if (cartTotalLength.value > 0) {
    stripe.value = Stripe('pk_test_51RiA31C2ItTnnQrILwjoHnh4VydpzIIOJ6MVDIENknflUByfJD1X9JYkto4uKs0usnKiIdmwkPibL0rBF6azXEvC00QTlg3Dt2')
    const elements = stripe.value.elements()
    card.value = elements.create('card', { hidePostalCode: true })

    card.value.mount('#card-element')
  }
})

const getItemTotal = (item) => {
  return item.quantity * item.sneaker.price
}

const submitForm = () => {
  errors.value = []

  if (first_name.value === '') errors.value.push('The first name field is missing!')
  if (last_name.value === '') errors.value.push('The last name field is missing!')
  if (email.value === '') errors.value.push('The email field is missing!')
  if (phone.value === '') errors.value.push('The phone field is missing!')
  if (address.value === '') errors.value.push('The address field is missing!')
  if (zipcode.value === '') errors.value.push('The zip code field is missing!')
  if (place.value === '') errors.value.push('The place field is missing!')

  if (!errors.value.length) {
    store.setIsLoading(true)

    stripe.value.createToken(card.value).then(result => {
      if (result.error) {
        store.setIsLoading(false)
        errors.value.push('Something went wrong with Stripe. Please try again')
        console.log(result.error.message)
      } else {
        stripeTokenHandler(result.token)
      }
    })
  }
}

const stripeTokenHandler = async (token) => {
  const items = cart.value.items.map(item => ({
    sneaker: item.sneaker.id,
    quantity: item.quantity,
    price: item.sneaker.price * item.quantity
  }))

  const data = {
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    address: address.value,
    zipcode: zipcode.value,
    place: place.value,
    phone: phone.value,
    items,
    stripe_token: token.id
  }

  await axios
    .post('/api/v1/checkout/', data)
    .then(() => {
      store.clearCart()
      router.push('/cart/success')
    })
    .catch(error => {
      errors.value.push('Something went wrong. Please try again')
      console.log(error)
    })

  store.setIsLoading(false)
}
</script>
