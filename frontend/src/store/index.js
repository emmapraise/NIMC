import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: '',
        isAuthenticated: false,
        user: {},
    },
    mutations: {
        initalizeStore(state){
            if(localStorage.getItem('token')){
                state.token = localStorage.getItem('token')
                state.user = localStorage.getItem('user')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
                state.user= {}
            }
        },
        setToken(state, token, user){
            state.token = token
            state.isAuthenticated = true
            state.user = user
        },
        removeToken(state){
            state.token = ''
            state.isAuthenticated = false
            state.user = {}
        }
    },
    actions: {},
    modules: {},
})