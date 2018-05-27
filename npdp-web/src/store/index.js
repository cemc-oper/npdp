import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);

import search_store from './search.js'

export default new Vuex.Store({
  modules: {
    search: search_store
  }
});