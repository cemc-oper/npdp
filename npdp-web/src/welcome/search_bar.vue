<template>
  <el-input placeholder="请输入内容" v-model="c_search_input">
    <el-select v-model="c_search_type" slot="prepend" placeholder="请选择">
      <el-option
        v-for="item in search_types"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
     </el-select>
    <el-button slot="append" icon="el-icon-search"></el-button>
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
      c_search_input: {
        get() {
          return this.search_input;
        },
        set(value) {
          this.$emit('updateSearchInput', value);
        }
      },
      c_search_type: {
        get(){
          return this.search_type;
        },
        set(value){
          this.$emit('updateSearchType', value);
        }
      }
    }
  }
</script>