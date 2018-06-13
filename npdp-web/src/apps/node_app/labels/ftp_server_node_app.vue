<template>
  <div>
    <h2>
      FtpServer
    </h2>
    <div>
      <h3>Product</h3>
      <ProductTable
        :ftp_server_id="id"
        :products="products"
      />
    </div>
  </div>
</template>

<script>
  import ProductTable from './ftp_server_node/product_table.vue'
  export default {
    name: "FtpServerNode",
    components: {
      ProductTable
    },
    props: [
      'id'
    ],
    data: function(){
      return {

      }
    },
    computed:{
      products() {
        return this.$store.state.node.ftp_server_node.products;
      }
    },
    methods:{
      queryInfo(payload){
        this.$store.dispatch('queryFTPServerProductsById', payload);
      }
    },
    mounted: function(){
      const payload = {
        id: this.id
      };
      this.queryInfo(payload);
    }
  }
</script>

<style scoped>

</style>