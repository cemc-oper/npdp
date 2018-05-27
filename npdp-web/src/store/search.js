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
  }
};