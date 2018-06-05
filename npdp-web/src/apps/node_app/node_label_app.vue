<script>
  import LabelTag from '../../components/label_tag.vue'
  import OperationSystemNode from './labels/operation_system_node_app.vue'

  export default {
    name: "NodeLabelApp",
    components: {
      LabelTag
    },
    props:[
      'label'
    ],
    computed:{
      current_node() {
        return this.$store.state.node.current_node;
      },
    },
    methods:{

    },
    render: function(createElement){
      const {labels} = this.current_node;
      if(labels.includes(this.label)) {
        if (this.label == "OperationSystem") {
          return createElement(OperationSystemNode);
        } else {
          return createElement('div', 'Current Label is not implemented.');
        }
      } else {
        return createElement('div', 'Current Node has no current label!');
      }

    }
  }
</script>

<style scoped>

</style>