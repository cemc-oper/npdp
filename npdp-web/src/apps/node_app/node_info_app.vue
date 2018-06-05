<template>
  <div>
    <div>
      <h2>Props</h2>
      <Row>
        <Col span="12">
          <Table :columns="prop_table_data.columns1" :data="prop_table_data.data1"></Table>
        </Col>
      </Row>
    </div>
    <div>
      <h2>Chart</h2>
      <div>
        under construction...
      </div>
    </div>
    <div>
      <h2>Relationship</h2>
      <Row>
        <Col span="20">
          <Table :columns="relation_table_data.columns" :data="relation_table_data.data"></Table>
        </Col>
      </Row>
    </div>
  </div>
</template>

<script>
  import LabelTag from '../../components/label_tag.vue'
  import RelationShipTableNode from '../../components/relation_ship_table_node.vue'
  import {generateTagColorMap} from '../../util/label.js'


  export default {
    name: 'NodeInfoApp',
    components: {
      LabelTag
    },
    computed: {
      current_node() {
        return this.$store.state.node.current_node;
      },
      relationships() {
        return this.$store.state.node.relationships;
      },
      tag_color_map() {
        const labels = this.current_node.labels;
        let color_set = new Set();
        labels.forEach((item, i)=>{
          color_set.add(item);
        });
        const tag_color_map = generateTagColorMap(color_set);
        return tag_color_map;
      },
      prop_table_data() {
        const {props} = this.current_node;
        let columns1 = [
          {
            title: 'Prop name',
            key: 'name'
          },
          {
            title: 'Prop value',
            key: 'value'
          }
        ];
        let data1 = [];
        for(let prop in props){
          data1.push({
            name: prop,
            value: props[prop]
          })
        }
        return {
          columns1: columns1,
          data1: data1
        }
      },
      relation_table_data(){
        const relationships = this.relationships;
        let columns = [
          {
            title: 'Start Node',
            key: 'start_node',
            render: (h, params)=>{
              if(params.row.start_node === 'current'){
                return h('div', {}, 'current');
              }

              return h(RelationShipTableNode, {
                props:{
                  node: params.row.start_node
                }
              })
            }
          },
          {
            title: 'Relation Type',
            key:'type'
          },
          {
            title: 'End Node',
            key: 'end_node',
            render: (h, params)=>{
              if(params.row.end_node === 'current'){
                return h('div', {}, 'current');
              }

              return h(RelationShipTableNode, {
                props:{
                  node: params.row.end_node
                }
              })
            }
          }
        ];
        let data = [];
        relationships.forEach((relation, index)=>{
          let item = {
            type: relation['type'],
          };
          if('start_node' in relation){
            item['start_node'] = relation['start_node'];
            item['end_node'] = 'current';
          } else {
            item['end_node'] = relation['end_node'];
            item['start_node'] = 'current';
          }
          data.push(item);
        });
        return {
          columns: columns,
          data: data
        }
      }
    }
  }
</script>