import Vue from 'vue';
import router from './router';
import App from './App.vue';
import Vuex from 'vuex';
require('./mock')

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    duration: 0,
    selectList:'',
  },
  mutations: {
    putSelectlist(state,test){
      state.selectList=test;
    },
    setDuration(state,value){
      state.duration=value;
    }
  },
  getters:{
    money : state =>  
      state.selectList.reduce((a, b) => (
        a + (('lights' in b) ? b.lights.reduce((x, y) => x + (y.num || 0) * ( y.price || 0), 0) : 0)
      ), 0)*state.duration,
    list : state =>
      [{state}],
  }
});

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App),
  mounted() {
    window.vue = this;
  },
}).$mount('#app');
