<template>
  <Layout id="app">
    <Header>
      <Row type="flex" align="middle">
        <Col span="2"><h1><router-link to="/" style="text-decoration:none;color:white">NPDP</router-link></h1></Col>
        <Col span="20">
          <SearchBar
            :search_input="search_input"
            :search_type="search_type"
            :search_types="search_types"
            @update-search-input="search_input=$event"
            @update-search-type="search_type=$event"
            @do-search="doSearch"
          />
        </Col>
      </Row>
    </Header>
    <Content>
      <h1>{{current_node.props?current_node.props.name:null}}</h1>
      <Row>
        <Col span="12">
          <LabelTag v-for="(label, index) in current_node.labels" :key="index"
                    :tag_color_map="tag_color_map"
                    :label="label"
          ></LabelTag>
        </Col>
      </Row>
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
    </Content>
    <Footer>
      <NPDPFooter/>
    </Footer>
  </Layout>

</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import NPDPFooter from '../../components/footer.vue'
  import LabelTag from '../../components/label_tag.vue'
  import RelationShipTableNode from '../../components/relation_ship_table_node.vue'
  import {generateTagColorMap} from '../../util/label.js'


  export default {
    name: 'NodeApp',
    components: {
      SearchBar,
      NPDPFooter,
      LabelTag
    },
    props: [
      'id'
    ],
    computed: {
      search_types() {
        return this.$store.state.search.search_types;
      },
      search_input: {
        get() {
          return this.$store.state.search.search_input;
        },
        set(value) {
          this.$store.commit('updateSearchInput', value)
        }
      },
      search_type: {
        get() {
          return this.$store.state.search.search_type;
        },
        set(value) {
          this.$store.commit('updateSearchType', value)
        }
      },
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
    },
    methods: {
      doSearch: function(payload) {
        this.$router.push({
          path: '/search',
          query: {
            type: payload.search_type,
            input: payload.search_input
          }
        });
      },
      executeQuery: function(payload){
        this.$store.dispatch('queryNodeById', payload);
        this.$store.dispatch('queryNodeRelationshipsById', payload);
      }
    },
    mounted: function(){
      const node_id = this.id;
      const payload = {
        id: node_id
      };
      // console.log('[NodeApp][mounted]', payload);
      this.executeQuery(payload);
    },
    beforeRouteUpdate(to, from, next){
      // console.log('[NodeApp][beforeRouteUpdate]');
      const payload = {
        id: to.params.id
      };
      this.executeQuery(payload);
      next();
    }
  }
</script>