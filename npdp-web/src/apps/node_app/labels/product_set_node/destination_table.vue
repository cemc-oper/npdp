<template>
  <div>
    <Row>
      <Col span="18">
        <Table :columns="table_data.columns" :data="table_data.data"></Table>
      </Col>
    </Row>
  </div>
</template>

<script>
  export default {
    name: "DestinationTable",
    props: [
      'destinations',
      'product_set_id'
    ],
    data: function(){
      return {};
    },
    computed:{
      table_data: function(){
        const columns = [
          {
            title: 'Destination Name',
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
                    type: 'default',
                    size: 'small',
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: (event)=>{

                    }
                  }
                }, 'Detail')
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
    methods:{

    }
  }
</script>

<style scoped>

</style>