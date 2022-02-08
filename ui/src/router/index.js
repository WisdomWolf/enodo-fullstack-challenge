import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
    { path: '/', component: 'Landing' },
    { path: '*', component: 'NotFound' },
    { path: '/properties', name: 'Enodo Challenge', component: 'PropertiesTable' }
]

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
    }
})

Vue.use(Router)

export default new Router({
    routes,
    mode: 'history'
})