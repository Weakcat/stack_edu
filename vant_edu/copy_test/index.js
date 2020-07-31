import Vue from 'vue';
import VueRouter from 'vue-router';
import Light from '../views/Light.vue'
import Pay from '../views/Pay.vue'

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'Light',
            component: Light,
        }, {
            path: '/pay',
            name: 'Pay',
            component: Pay,
        }
    ]
});