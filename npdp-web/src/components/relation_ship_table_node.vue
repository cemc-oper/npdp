<template>
  <div>
    <Row>
      <router-link :to="{name:'node_by_id', params:{id: node.id}}">{{node.props.name}}</router-link>
    </Row>
    <Row>
      <LabelTag v-for="(label, index) in node.labels" :key="index"
                    :tag_color_map="tag_color_map"
                    :label="label"
      ></LabelTag>
    </Row>
  </div>
</template>

<script>
  import LabelTag from './label_tag.vue'
  import {generateTagColorMap} from '../util/label.js'

  export default {
    name: "RelationShipTableNode",
    components:{
      LabelTag
    },
    props:[
      'node',
    ],
    computed:{
      tag_color_map(){
        const labels = this.node.labels;
        let color_set = new Set();
        labels.forEach((item, i)=>{
          color_set.add(item);
        });
        const tag_color_map = generateTagColorMap(color_set);
        return tag_color_map;
      }

    }
  }
</script>

<style scoped>

</style>