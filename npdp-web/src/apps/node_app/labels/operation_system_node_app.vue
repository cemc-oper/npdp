<template>
  <div>
    <h2>
      OperationSystem
    </h2>
    <div>
      <h3>Product</h3>
      <Row>
        <Col span="12">
          <Table :columns="products_table_data.columns" :data="products_table_data.data"></Table>
        </Col>
      </Row>
    </div>
    <div>
      <h3>Destination</h3>
      <Row>
        <Col span="18">
          <Table :columns="destinations_table_data.columns" :data="destinations_table_data.data"></Table>
        </Col>
      </Row>
    </div>
  </div>
</template>

<script>
  export default {
    name: "OperationSystemNode",
    components: {

    },
    props: [
      'id'
    ],
    computed:{
      products() {
        return this.$store.state.node.operation_system_node.products
      },
      destinations() {
        return this.$store.state.node.operation_system_node.destinations
      },
      products_table_data(){
        const columns = [
          {title: 'Product Name', key: 'name', sortable: true},
          {title: 'Actions'}
        ];

        const data = this.products.map((item, index)=>{
          return {
            name: item['props']['name'],
            id: item['id']
          }
        });

        return {
          columns,
          data
        }
      },
      destinations_table_data(){
        const columns = [
          {title: 'Destination Name', key: 'name', sortable: true},
          {title: 'Type', key: 'type', sortable: true},
          {title: 'Target', key: 'target', sortable: true},
          {title: 'Actions'}
        ];

        const data = this.destinations.map((item, index)=>{
          let des_type = 'Default';
          let target = null;
          const {props, labels} = item;
          if(labels.includes('FTPServer')){
            target = props['host'];
            des_type = 'FTP'
          }

          return {
            name: props['name'],
            id: item['id'],
            props: props,
            target: target,
            type: des_type
          }
        });

        return {
          columns,
          data
        }
      }
    },
    methods: {
      queryInfo(payload){
        this.$store.dispatch('queryOperationSystemProductsById', payload);
        this.$store.dispatch('queryOperationSystemDestinationsById', payload);
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