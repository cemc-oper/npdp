import axios from 'axios';
import "babel-polyfill";

export default {
  state: {
    current_node: {
      props: {},
      labels: [],
      id: null
    },
    relationships: []
  },
  mutations: {
    updateCurrentNode(state, payload){
      state.current_node = payload.current_node;
    },
    updateRelationships(state, payload){
      state.relationships = payload.relationships;
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
    },
    queryNodeRelationshipsById(context, payload){
      const {commit} = context;
      async function fetchQueryNodeRelationshipsAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/node/ids/${id}/relationships`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {relationships} = data;
            commit('updateRelationships', {
              relationships: relationships
            })
          }
        } catch (error) {
          console.error('[search_store][queryNodeRelationshipsById] error:', error);
        }
      }

      fetchQueryNodeRelationshipsAPI();
    }
  }
};