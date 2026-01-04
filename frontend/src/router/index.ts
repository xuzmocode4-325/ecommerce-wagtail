import { createRouter, createWebHistory } from 'vue-router'
import ProductPage from '@/components/ProductPage.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [],
})

export default router
