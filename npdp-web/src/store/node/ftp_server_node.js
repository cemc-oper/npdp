import axios from 'axios'
import 'babel-polyfill'

export default {
  state: {
    products: []
  },
  mutations: {
    updateFTPServerNodeProducts(state, payload){
      state.products = payload.products;
    }
  },
  actions: {
    queryFTPServerProductsById(context, payload){
      const {commit} = context;
      console.log(payload);
      async function fetchAPI(){
        try{
          const {id} = payload;
          const response = await axios.get(`/api/v1/ftp-server/ids/${id}/products`);
          const {data} = response.data;
          const {status} = data;
          if(status === "ok"){
            const {products} = data;
            commit('updateFTPServerNodeProducts', {
              products: products
            })
          }
        } catch (error){
          console.log('[node_store.ftp_server_node][queryFTPServerProductsById]:', error);
        }
      }
      fetchAPI();
    }
  }
}