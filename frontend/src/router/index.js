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
    component: () => import('../views/LandingPage/AboutView.vue')
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
    path: '/patners/user/profile',
    name: 'patner_user_profile',
    component: () => import('../views/Patners/Profile.vue')
  },

  {
    path: '/patners/user/documents',
    name: 'patner_user_documents',
    component: () => import('../views/Patners/Documents.vue')
  },
  {
    path: '/admin/enrolment',
    name: 'enrolment',
    component: () => import('../views/User/RegisterView.vue')
  },
  {
    path: '/user/profile',
    name: 'user_profile',
    component: () => import('../views/User/RegisterView.vue')
  },
  {
    path: '/admin/upload-document',
    name: 'upload_document',
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/user/documents',
    name: 'documents',
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/admin/requests',
    name: 'requests',
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/user/make-request',
    name: 'make-request',
    component: () => import('../views/User/MakeRequestView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
