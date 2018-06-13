import axios from 'axios'
import 'babel-polyfill'

export default {
  state: {
    destinations: []
  },
  mutations: {
    updateProductSetDestinations(state, payload){
      state.destinations = payload.destinations;
    }
  },
  actions: {
    queryProductSetDestinationsById(context, payload){
      const {commit} = context;
      // console.log(payload);
      async function fetchAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/product-set/ids/${id}/destinations`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {destinations} = data;
            commit('updateProductSetDestinations', {
              destinations: destinations
            })
          }
        } catch (error){
          console.log('[node_store.product_set_node][queryProductSetDestinationsById]:', error);
        }
      }
      fetchAPI();
    }
  }
}