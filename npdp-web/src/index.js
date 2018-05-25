import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(ElementUI);

import store from './store/index.js'
import Welcome from './welcome/index.vue';

import './base.scss';

const routes = [
  {
    path: '/',
    component: Welcome
  }
];

const router = new VueRouter({
  routes
});

const app = new Vue({
  router,
  store
}).$mount('#app');