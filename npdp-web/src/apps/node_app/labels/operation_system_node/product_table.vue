<template>
  <div>
    <Row>
      <Col span="18">
        <Table :columns="table_data.columns" :data="table_data.data"></Table>
      </Col>
    </Row>
    <Modal
      v-model="info_modal.is_open"
      :title="info_modal.title"
    >
      <h2>Destinations</h2>
      <div>
        <p v-for="d in info_modal.product_info.destinations" :key="d.id">
          <router-link :to="{name:'node_by_id', params:{id: d.id}}">
            {{d.props.name}}
          </router-link>
        </p>
      </div>
    </Modal>
  </div>
</template>

<script>
  export default {
    name: "ProductTable",
    props: [
      'products',
      'operation_system_id'
    ],
    data: function(){
      return {
        info_modal: {
          is_open: false,
          title: 'Product info',
          product_info:{}
        },
        action_map: {}
      }
    },
    watch: {
      products: function(new_products, old_products){
        this.action_map = {};
        new_products.forEach((item, index)=>{
          this.action_map[item.id] = {
            view_destinations:{
              loading: false
            }
          }
        });
      }
    },
    computed:{
      table_data: function(){
        const columns = [
          {
            title: 'Product Name',
            key: 'name',
            sortable: true,
            render: (h, params) => {
              return h('router-link', {
                props:{
                  to: {
                    name: 'node_by_id',
                    params: {
                      id: params.row.id
                    }
                  }
                }
              }, params.row.name)
            }
          },
          {
            title: 'Actions',
            render: (h, params) => {
              // console.log(params.row);
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small',
                    // TODO: may cause error. need more analytics.
                    // loading: params.row.action_map.view_destinations.loading
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      const payload = {
                        operation_system_id: this.operation_system_id,
                        product_set_id: params.row.id
                      };
                      this.showProductInfo(payload);
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
            id: item['id'],
            action_map: this.action_map[item['id']]
          }
        });

        return {
          columns,
          data
        }
      }
    },
    methods:{
      showProductInfo: function(payload){
        const {product_set_id} = payload;
        this.action_map[product_set_id].view_destinations.loading = true;
        payload.callback = this.receiveProductDestinations;
        this.info_modal.product_info = {};
        this.$store.dispatch('queryProductDestinations', payload);

      },
      receiveProductDestinations: function(res){
        // console.log(res);
        this.info_modal.is_open = true;
        const {data} = res;
        const {status, request} = data;
        const {product_set_id} = request;
        this.action_map[product_set_id].view_destinations.loading = false;
        if(status === 'ok'){
          const {destinations} = data;
          this.info_modal.product_info.destinations = destinations;
        } else {
        }
      }
    }
  }
</script>

<style scoped>

</style>