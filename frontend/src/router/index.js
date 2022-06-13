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
    name: 'admin_register',
    component: () => import('../views/Admin/SignUp.vue')
  },
  {
    path: '/patners/checkin',
    name: 'patner_checkin',
    component: () => import('../views/Patners/CheckIn.vue')
  },
  {
    path: '/user/register',
    name: 'enrolment',
    component: () => import('../views/User/RegisterView.vue')
  },
  {
    path: '/admin/upload-document',
    name: 'upload_document',
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/admin/requests',
    name: 'requests',
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/make-request',
    name: 'make-request',
    component: () => import('../views/User/RegisterView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
