import axios from 'axios';
import "babel-polyfill";

export default {
  state: {
    products: [],
    destinations: []
  },
  mutations: {
    updateOperationSystemProducts(state, payload){
      state.products = payload.products;
    },
    updateOperationSystemDestinations(state, payload){
      state.destinations = payload.destinations;
    }
  },
  actions: {
    queryOperationSystemProductsById(context, payload){
      const {commit} = context;
      async function fetchAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/operation-system/ids/${id}/products`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {products} = data;
            commit('updateOperationSystemProducts', {
              products: products
            })
          }
        } catch (error) {
          console.error('[node_store.operation_system_node][queryOperationSystemProductsById]:', error);
        }
      }
      fetchAPI();
    },
    queryOperationSystemDestinationsById(context, payload){
      const {commit} = context;
      async function fetchAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/operation-system/ids/${id}/destinations`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {destinations} = data;
            commit('updateOperationSystemDestinations', {
              destinations: destinations
            })
          }
        } catch (error) {
          console.error('[node_store.operation_system_node][queryOperationSystemDestinationsById]:', error);
        }
      }
      fetchAPI();
    },
    queryDestinationProducts(context, payload){
      async function fetchAPI(){
        try{
          const {operation_system_id, destination_id, callback} = payload;
          const response = await axios.get(`/api/v1/operation-system/ids/${operation_system_id}` +
            `/destinations/${destination_id}/products`);
          const {data} = response;
          callback(data);
        } catch (error) {
          console.error('[node_store.operation_system_node][queryDestinationProducts]:', error);
        }
      }
      fetchAPI();
    },
    queryProductDestinations(context, payload){
      async function fetchAPI(){
        try{
          const {operation_system_id, product_set_id, callback} = payload;
          const response = await axios.get(`/api/v1/operation-system/ids/${operation_system_id}` +
            `/products/${product_set_id}/destinations`);
          const {data} = response;
          callback(data);
        } catch (error) {
          console.error('[node_store.operation_system_node][queryProductDestinations]:', error);
        }
      }
      fetchAPI();
    }
  }
}