import Vue from 'vue';
import VueRouter from 'vue-router';
import Light from '../views/Login.vue'
import Quizzes from '../views/Quizzes.vue'
import Quiz from '../views/Quiz.vue'

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'Login',
            component: Light,
        },{
            path:'/quizzes',
            name:'Quizzes',
            component: Quizzes,
        },{
            path: '/quiz',
            name:'Quiz',
            component: Quiz,
        }

    ]
});