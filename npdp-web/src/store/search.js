import axios from 'axios';

export default {
  state: {
    search_input: '',
    search_type: 'all',
    search_types: [
      {
        value: 'all',
        label: '全部'
      },
      {
        value: 'destination',
        label: 'FTP'
      },
      {
        value: 'product',
        label: '产品'
      },
      {
        value: 'operation_system',
        label: '模式'
      }
    ]
  },
  mutations: {
    updateSearchInput(state, text){
      state.search_input = text;
    },
    updateSearchType(state, stype){
      state.search_type = stype;
    },
    updateSearch(state, payload){
      state.search_input = payload.search_input;
      state.search_type = payload.search_type;
    }
  },
  actions: {
    executeSearch(context, payload){
      const {commit, state} = context;
      console.log("Execute search in actions.", payload);

      async function fetchSearchAPI(){
        try {
          const response = await axios.post('/api/v1/search', payload);
          console.log(response);
        } catch (error){
          console.error(error);
        }
      }

      fetchSearchAPI();

    }
  }
};