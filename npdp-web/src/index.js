import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import Welcome from './welcome/index.vue';

Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(ElementUI);

import './base.scss';

const welcome_app = new Vue({
  el: "#app",
  components: {
    Welcome
  }
});