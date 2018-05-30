import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import iView from 'iview';

import 'iview/dist/styles/iview.css';
import './base.scss';

Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(iView);

import store from './store/index.js'
import routes from './routes/index.js'


const router = new VueRouter({
  routes
});

const app = new Vue({
  router,
  store
}).$mount('#app');
