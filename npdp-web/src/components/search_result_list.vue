<template>
  <div>
    <Row>
      <Col span="18" offset="2">
        <Row v-for="(record, index) in search_results" :key="index" class="search-record">
          <Col span="24">
            <Row>
              <h3><router-link :to="getNodeIdURL(record)">{{record.props.name}}</router-link></h3>
            </Row>
            <Row>
              <LabelTag v-for="(label, index) in record.labels" :key="index"
                        :tag_color_map="tagColorMap"
                        :label="label"
              ></LabelTag>
            </Row>
            <Row>
              {{record.props}}
            </Row>
          </col>
        </Row>
      </Col>
    </Row>
  </div>
</template>

<script>
  import {generateTagColorMap} from '../util/label.js'
  import LabelTag from './label_tag.vue'

  export default {
    name: 'SearchResultList',
    props: [
      'search_results'
    ],
    components: {
      LabelTag
    },
    computed: {
      tagColorMap: function(){
        const search_results = this.search_results;
        let color_set = new Set();
        search_results.forEach((item, i)=>{
          const {labels} = item;
          labels.forEach(label=>{
            color_set.add(label);
          })
        });
        const tag_color_map = generateTagColorMap(color_set);
        return tag_color_map;
      }
    },
    methods: {
      getNodeIdURL: function(record){
        const {id} = record;
        return `/node/ids/${id}`;
      }
    }
  }
</script>

<style lang="scss" scoped>
  .search-record {
    margin-top: 10px;
    margin-bottom: 10px;
    h3 {
      font-size: 18px;
    }
  }
</style>