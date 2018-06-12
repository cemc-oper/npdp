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

      <DestinationTable
        :operation_system_id="id"
        :destinations="destinations"
      />
    </div>
  </div>
</template>

<script>
  import DestinationTable from './operation_system_node/destination_table.vue'
  export default {
    name: "OperationSystemNode",
    components: {
      DestinationTable
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
        },
        destination_map:{

        }
      }
    },
    computed: {
      products() {
        return this.$store.state.node.operation_system_node.products
      },
      destinations() {
        return this.$store.state.node.operation_system_node.destinations
      },
      products_table_data() {
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

        const data = this.products.map((item, index) => {
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
    },
    methods: {
      queryInfo(payload){
        this.$store.dispatch('queryOperationSystemProductsById', payload);
        this.$store.dispatch('queryOperationSystemDestinationsById', payload);
      },
      showProductInfo(payload){
        const {id} = payload;
        this.product_info_modal.is_open = true;
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