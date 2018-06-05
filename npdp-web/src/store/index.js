import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);

import search_store from './search.js'
import node_store from './node/index.js'

export default new Vuex.Store({
  modules: {
    search: search_store,
    node: node_store
  }
});