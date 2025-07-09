import { createRouter, createWebHistory } from 'vue-router'
import { useMainStore } from '@/stores'

import HomeView from '../views/HomeView.vue'
import Sneaker from '@/views/Sneaker.vue'
import Category from '@/views/Category.vue'
import Search from '@/views/Search.vue'
import Cart from '@/views/Cart.vue'
import SignUp from '@/views/SignUp.vue'
import Login from '@/views/Login.vue'
import MyAccount from '@/views/MyAccount.vue'
import Checkout from '@/views/Checkout.vue'
import Success from '@/views/Success.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/search',
        name: 'Search',
        component: Search
    },
    {
        path: '/cart',
        name: 'Cart',
        component: Cart
    },
    {
        path: '/cart/success',
        name: 'Success',
        component: Success
    },
    {
        path: '/cart/checkout',
        name: 'Checkout',
        component: Checkout,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/:category_slug/:sneaker_slug',
        name: 'Sneaker',
        component: Sneaker
    },
    {
        path: '/:category_slug',
        name: 'Category',
        component: Category
    }
  ],
})

router.beforeEach((to, from, next) => {
  const store = useMainStore()

  if (to.matched.some(record => record.meta.requireLogin) && !store.isAuthenticated) {
    next({ name: 'Login', query: { to: to.path } })
  } else {
    next()
  }
})

export default router
