import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import login from '@/components/login/login.vue'
import register from '@/components/login/register.vue'
import reservas from '../views/ReservasView.vue'
import ReservasCreate from '@/views/Reservas/ReservasCreate.vue'
import store from '@/stores/login'
import perfil from '@/components/login/perfil.vue'
import canchas from '@/components/canchas/CreateCancha.vue'
import GestionCanchas from '@/components/canchas/GestionCanchas.vue'
import NotFound from '@/components/404.vue'
import CreateLugar from '@/components/lugares/CreateLugar.vue'
import Lugares from '@/components/lugares/Lugares.vue'
const isUserAuthenticated = (): boolean => {
  return !!localStorage.getItem('token'); // Aquí puedes verificar si el usuario tiene un token
};

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
      beforeEnter: (to, from, next) => {
        if (isUserAuthenticated()) {
          next('/perfil'); // Redirige al perfil si el usuario está autenticado
        } else {
          next(); // Permite el acceso si no está autenticado
        }
      },
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
    {
      path: '/perfil',
      name: 'perfil',
      component: perfil,
      meta: { requiresAuth: true },
    },
    {
      path: '/canchascrear',
      name: 'canchascrear',
      component: canchas,
      meta: { requiresAuth: true },
    },
    {
      path: '/gestioncanchas',
      name: 'gestioncanchas',
      component: GestionCanchas,
      meta: { requiresAuth: true },
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: NotFound
    },
    {
      path: '/gestionlugares',
      name: 'gestionlugares',
      component: Lugares,
      meta: { requiresAuth: true },
    },
    {
      path: '/crearlugar',
      name: 'crearlugar',
      component: CreateLugar,
      meta: { requiresAuth: true },
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    // Siempre vuelves al top de la página al cambiar de ruta
    return { top: 0 };
  },
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
