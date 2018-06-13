<template>
  <div>
    <h2>
      ProductSet
    </h2>
    <div>
      <h3>Destinations</h3>
      <DestinationTable
        :product_set_id="id"
        :destinations="destinations"
      />
    </div>
  </div>
</template>

<script>
  import DestinationTable from './product_set_node/destination_table.vue'

  export default {
    name: "ProductSetNode",
    components: {
      DestinationTable
    },
    props:[
      'id'
    ],
    data: function(){
      return {};
    },
    computed: {
      destinations(){
        return this.$store.state.node.product_set_node.destinations;
      }
    },
    methods:{
      queryInfo(payload){
        this.$store.dispatch('queryProductSetDestinationsById', payload);
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