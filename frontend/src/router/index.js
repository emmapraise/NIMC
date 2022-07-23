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
    meta: { title: 'NIMC - Login' },
    component: () => import('../views/User/LoginViews.vue')
  },
  {
    path: '/admin/register',
    name: 'admin_register',
    meta: { title: 'NIMC - Admin Sign Up' },
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
    meta: { title: 'NIMC - Enrol New User' },
    component: () => import('../views/User/RegisterView.vue')
  },
  {
    path: '/admin/enrolment/success',
    name: 'enrolment_success',
    meta: { title: 'NIMC - Enrol Success' },
    component: () => import('../views/Admin/SuccessView.vue')
  },
  {
    path: '/user/profile',
    name: 'user_profile',
    meta: { title: 'NIMC - User Profile' },
    component: () => import('../views/User/RegisterView.vue')
  },
  {
    path: '/admin/upload-document',
    name: 'upload_document',
    meta: { title: 'NIMC - Upload Documents' },
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/user/documents',
    name: 'documents',
    meta: { title: 'NIMC - Documents' },
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/admin/requests',
    name: 'requests',
    meta: { title: 'NIMC - Approve Request' },
    component: () => import('../views/Admin/DocumentView.vue')
  },
  {
    path: '/user/make-request',
    name: 'make-request',
    meta: { title: 'NIMC - Update Request' },
    component: () => import('../views/User/MakeRequestView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

const DEFAULT_TITLE = process.env.VUE_APP_TITLE;
router.afterEach((to) => {
    // Use next tick to handle router history correctly
    // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
    Vue.nextTick(() => {
        document.title = to.meta.title || DEFAULT_TITLE;
    });
});
