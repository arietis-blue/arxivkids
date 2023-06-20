import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import DetailPaper from '../views/DetailPaper.vue'

const routes = [
  {
    path: '/',
    name: Home,
    component: Home
  },
  {
    path: '/detailpaper',
    name: DetailPaper,
    component: DetailPaper
  }
]

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  // vite不用process.env
  // 报错看developer tool的Console的error
  // https://vitejs.dev/guide/env-and-mode.html 写法看文档
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router