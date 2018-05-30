<template>
  <Tag type="border" :color="label_color">
    {{label}}
  </Tag>
</template>

<script>
  export default {
    name: 'LabelTag',
    props: [
      'tag_color_map',
      'label'
    ],
    computed: {
      label_color: function(){
        if (this.tag_color_map.has(this.label)){
          return this.tag_color_map.get(this.label);
        } else {
          return 'blue';
        }
      }
    }
  }
</script>