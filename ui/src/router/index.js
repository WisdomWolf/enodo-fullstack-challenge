import Vue from 'vue'

const routes = [
    { path: '/', component: 'Landing' },
    { path: '*', component: 'NotFound' },
    { path: '/properties', name: 'Enodo Challenge', component: 'PropertiesTable' }
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes,
})

const app = Vue.createApp()
app.use(router)
app.mount('#app')
