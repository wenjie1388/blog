import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('@/views/index.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/login/index.vue')
    },
    {
      path: '/article/:id',
      name: 'article',
      component: () => import('@/views/article/index.vue')
    },
    {
      path: '/error_400',
      name: '400',
      component: () => import('@/views/error/400.vue')
    },
    {
      path: '/error_404',
      name: '404',
      component: () => import('@/views/error/404.vue')
    },
    {
      path: '/error_500',
      name: '500',
      component: () => import('@/views/error/500.vue')
    }
  ]
})

export default router
