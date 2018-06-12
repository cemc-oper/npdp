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
      <h2>Products</h2>
      <div>
        <p v-for="ps in info_modal.destination_info.products_sets" :key="ps.id">
          {{ps.props.name}}
        </p>
      </div>
    </Modal>
  </div>
</template>

<script>
  export default {
    name: "DestinationTable",
    props: [
      'destinations',
      'operation_system_id'
    ],
    data: function(){
      return {
        info_modal: {
          is_open: false,
          title: 'Destination info',
          destination_info:{}
        },
        action_map: {

        }
      }
    },
    watch: {
      destinations: function(new_destinations, old_destinations){
        this.action_map = {};
        new_destinations.forEach((item, index)=>{
          this.action_map[item.id] = {
            view_products:{
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
                    size: 'small',
                    loading: params.row.action_map.view_products.loading
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: (event)=>{
                      console.log('Button view products clicked.');
                      const payload = {
                        operation_system_id: this.operation_system_id,
                        destination_id: params.row.id
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
            type: des_type,
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
      showDestinationInfo(payload){
        const {destination_id} = payload;
        this.action_map[destination_id].view_products.loading = true;
        payload.callback = this.receiveDestinationProducts;
        this.info_modal.destination_info = {};
        this.$store.dispatch('queryDestinationProducts', payload);
      },
      receiveDestinationProducts(res){
        console.log(res);
        this.info_modal.is_open = true;
        const {data} = res;
        const {status, request} = data;
        const {destination_id} = request;
        this.action_map[destination_id].view_products.loading = false;
        if(status === 'ok'){
          const {product_sets} = data;
          this.info_modal.destination_info.products_sets = product_sets;
        } else {
        }
      }
    }
  }
</script>

<style scoped>

</style>