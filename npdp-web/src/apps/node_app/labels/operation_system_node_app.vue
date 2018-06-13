<template>
  <div>
    <h2>
      OperationSystem
    </h2>
    <div>
      <h3>Product</h3>
      <ProductTable
        :operation_system_id="id"
        :products="products"
      />
    </div>
    <div>
      <h3>Destination</h3>

      <DestinationTable
        :operation_system_id="id"
        :destinations="destinations"
      />
    </div>
  </div>
</template>

<script>
  import DestinationTable from './operation_system_node/destination_table.vue'
  import ProductTable from './operation_system_node/product_table.vue'

  export default {
    name: "OperationSystemNode",
    components: {
      DestinationTable,
      ProductTable
    },
    props: [
      'id'
    ],
    data: function() {
      return {}
    },
    computed: {
      products() {
        return this.$store.state.node.operation_system_node.products;
      },
      destinations() {
        return this.$store.state.node.operation_system_node.destinations;
      }
    },
    methods: {
      queryInfo(payload){
        this.$store.dispatch('queryOperationSystemProductsById', payload);
        this.$store.dispatch('queryOperationSystemDestinationsById', payload);
      },
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