<template>
  <div>
    <Row>
      <Col span="18" offset="2">
        <Row v-for="(record, index) in search_results" :key="index" class="search-record">
          <Col span="24">
            <Row>
              <h3>{{record.props.name}}</h3>
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
        console.log(search_results);
        return new Map();
      }
    }
  }
</script>

<style scoped>
  .search-record {
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>