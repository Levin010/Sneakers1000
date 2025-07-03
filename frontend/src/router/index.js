import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Sneaker from '@/views/Sneaker.vue'
import Category from '@/views/Category.vue'
import Search from '@/views/Search.vue'
import Cart from '@/views/Cart.vue'

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

export default router
