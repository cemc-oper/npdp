<script>
  import LabelTag from '../../components/label_tag.vue'
  import OperationSystemNode from './labels/operation_system_node_app.vue'
  import FtpServerNode from './labels/ftp_server_node_app.vue'
  import ProductSetNode from './labels/product_set_node_app.vue'

  export default {
    name: "NodeLabelApp",
    components: {
      LabelTag
    },
    props:[
      'label',
      'id'
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
        if (this.label === "OperationSystem") {
          return createElement(OperationSystemNode, {
            props: {
              id: this.id
            }
          });
        } else if (this.label === "FTPServer") {
          return createElement(FtpServerNode, {
            props: {
              id: this.id
            }
          });
        } else if (this.label === "ProductSet") {
          return createElement(ProductSetNode, {
            props: {
              id: this.id
            }
          });
        } else{
          return createElement('div', `Label ${this.label} is not implemented.`);
        }
      } else {
        return createElement('div', `Current Node has no label ${this.label}!`);
      }

    }
  }
</script>

<style scoped>

</style>