import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import VueAxios from "vue-axios";
import axios from 'axios'
import store from './store'

window.Vue = Vue;

// Vue.config.productionTip = false
Vue.use(VueAxios, axios);
axios.defaults.baseURL = process.env.VUE_APP_BACKEND_URL

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
