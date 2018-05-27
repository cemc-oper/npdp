<template>
  <el-input
    v-model="current_search_input"
    placeholder="请输入内容"
    v-on:keyup.enter.native="doSearch"
  >
    <el-select v-model="current_search_type" slot="prepend" placeholder="请选择">
      <el-option
        v-for="item in search_types"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
     </el-select>
    <el-button slot="append" icon="el-icon-search" v-on:click="doSearch"></el-button>
  </el-input>
</template>

<script>
  export default {
    name: 'SearchBar',
    props: [
      'search_types',
      'search_input',
      'search_type'
    ],
    computed: {
      current_search_input: {
        get() {
          return this.search_input;
        },
        set(value) {
          this.$emit('updateSearchInput', value);
        }
      },
      current_search_type: {
        get(){
          return this.search_type;
        },
        set(value){
          this.$emit('updateSearchType', value);
        }
      }
    },
    methods: {
      doSearch: function(event){
        let search_type = this.current_search_type;
        let search_context = this.current_search_input;
        console.log("search type:", search_type);
        console.log("search context:", search_context);
        this.$emit('doSearch', {
          type: search_type,
          context: search_context
        })
      }
    }
  }
</script>

<style scoped>
  .el-select {
    min-width: 100px;
  }
</style>