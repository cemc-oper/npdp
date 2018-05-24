import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(ElementUI);


const welcome_app = new Vue({
  el: "#app",
  data: {
    search_input: '',
    select: ''
  }
});