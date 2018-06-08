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
      <Modal
        v-model="product_info_modal.is_open"
        title="Product info"
      >
        <h1>Product info</h1>
        <h2>{{product_info_modal.product_info.id}}</h2>
      </Modal>
    </div>
    <div>
      <h3>Destination</h3>
      <Row>
        <Col span="18">
          <Table :columns="destinations_table_data.columns" :data="destinations_table_data.data"></Table>
        </Col>
      </Row>
      <Modal
        v-model="destination_info_modal.is_open"
        title="Destination info"
      >
        <h1>Destination info</h1>
        <h2>{{destination_info_modal.destination_info.id}}</h2>
      </Modal>
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
    data: function() {
      return {
        product_info_modal: {
          is_open: false,
          loading: false,
          product_info: {}
        },
        destination_info_modal: {
          is_open: false,
          loading: false,
          destination_info: {}
        }
      }
    },
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
          {
            title: 'Actions',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      console.log('Button view destinations C.');
                    }
                  }
                }, 'View destinations')
              ])
            }
          }
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
          {
            title: 'Destination Name',
            key: 'name',
            sortable: true
          },
          {
            title: 'Type',
            key: 'type',
            sortable: true
          },
          {
            title: 'Target',
            key: 'target',
            sortable: true
          },
          {
            title: 'Actions',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: (event)=>{
                      console.log('Button view products clicked.');
                      const payload = {
                        id: params.row.id
                      };
                      this.showDestinationInfo(payload);
                    }
                  }
                }, 'View products')
              ])
            }
          }
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
      },
      showProductInfo(payload){
        const {id} = payload;
        this.product_info_modal.is_open = true;
      },
      showDestinationInfo(payload){
        const {id} = payload;
        this.destination_info_modal.is_open = true;
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