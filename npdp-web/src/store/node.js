import axios from 'axios';
import "babel-polyfill";

export default {
  state: {
    current_node: {
      props: {},
      labels: [],
      id: null
    }
  },
  mutations: {
    updateCurrentNode(state, payload){
      state.current_node = payload.current_node;
    }
  },
  actions: {
    queryNodeById(context, payload){
      const {commit} = context;
      async function fetchQueryNodeAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/node/ids/${id}`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {node} = data;
            commit('updateCurrentNode', {
              current_node: node
            })
          }
        } catch (error) {
          console.error('[search_store][queryNode] error:', error);
        }
      }

      fetchQueryNodeAPI();
    }
  }
};