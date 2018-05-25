import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);

const welcome_store = {
  state: {
    search_input: '',
    search_type: 'all'
  },
  mutations: {
    updateSearchInput(state, text){
      console.log('updateSearchInput:', text);
      state.search_input = text;
    },
    updateSearchType(state, stype){
      console.log('updateSearchType:', stype);
      state.search_type = stype;
    }
  }
};

export default new Vuex.Store({
  modules: {
    welcome: welcome_store
  }
});