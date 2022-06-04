import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/LandingPage/Home.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   redirect: '/home'
  // },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/LandingPage/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/User/LoginViews.vue')
  },
  {
    path: '/admin/register',
    name: 'admin-register',
    component: () => import('../views/Admin/SignUp.vue')
  },
  {
    path: '/patners/checkin',
    name: 'patner-checkin',
    component: () => import('../views/Patners/CheckIn.vue')
  },
  {
    path: '/user/register',
    name: 'entrolment',
    component: () => import('../views/User/Register.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
