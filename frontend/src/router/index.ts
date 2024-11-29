import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import login from '@/components/login/login.vue'
import register from '@/components/login/register.vue'
import reservas from '../views/ReservasView.vue'
import ReservasCreate from '@/views/Reservas/ReservasCreate.vue'
import store from '@/stores/login'
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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/register',
      name: 'register',
      component: register,
    },
    {
      path: '/reservas',
      name: 'reservas',
      component: reservas,
    },
    {
      path: '/reservas/crear/:id',
      name: 'reservasCreate',
      component: ReservasCreate,
      meta: { requiresAuth: true },
    },
  ],
})
router.beforeEach((to, from, next) => {
  const auth = store()
  const isAuth = auth.token
  if (to.meta.requiresAuth && isAuth === null) {
    next('/login')
  }
   else {
    next()
  }
})
export default router
