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
        value: 'ftp',
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
    ],
    search_results:[]
  },
  mutations: {
    updateSearchInput(state, payload){
      state.search_input = payload;
    },
    updateSearchType(state, payload){
      state.search_type = payload;
    },
    updateSearch(state, payload){
      state.search_input = payload.search_input;
      state.search_type = payload.search_type;
    },
    updateSearchResult(state, payload){
      state.search_results = payload.search_results;
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
          const {data} = response.data;
          const {status} = data;
          if(status==='ok'){
            const {results} = data;
            commit('updateSearchResult', {
              search_results: results
            })
          }
        } catch (error){
          console.error(error);
        }
      }

      fetchSearchAPI();
    }
  }
};