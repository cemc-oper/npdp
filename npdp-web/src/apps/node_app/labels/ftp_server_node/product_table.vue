<template>
  <div>
    <Row>
      <Col span="18">
        <Table
          :columns="table_data.columns"
          :data="table_data.data"
        ></Table>
      </Col>
    </Row>
    <Modal>

    </Modal>
  </div>
</template>

<script>
  export default {
    name: "ProductTable",
    props: [
      'ftp_server_id',
      'products'
    ],
    data: function(){
      return {};
    },
    computed: {
      table_data: function(){
        const columns = [
          {
            title: 'Operation System Name',
            key: 'operation_system_name',
            sortable: true,
            render: (h, params)=>{
              return h('router-link', {
                props: {
                  to: {
                    name: 'node_by_id',
                    params: {
                      id: params.row.operation_system.id
                    }
                  }
                }
              }, params.row.operation_system.props.name)
            }
          },
          {
            title: 'Product Set Name',
            key: 'product_set_name',
            sortable: true,
            render: (h, params)=>{
              return h('router-link', {
                props: {
                  to: {
                    name: 'node_by_id',
                    params: {
                      id: params.row.product_set.id
                    }
                  }
                }
              }, params.row.product_set.props.name)
            }
          },
          {
            title: 'Actions',
            render: (h, params)=>{
              return h('div', [
                h('Button', {
                  props: {
                    type: 'default',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: ()=>{
                      console.log('Button Detail clicked');
                    }
                  }
                }, 'Detail')
              ]);
            }
          }
        ];

        const data = this.products.map((item, index)=>{
          const {operation_system, product_set} = item;
          return {
            operation_system: operation_system,
            product_set: product_set
          }
        });

        return {
          columns,
          data
        }
      },
    },
    methods: {

    }
  }
</script>

<style scoped>

</style>