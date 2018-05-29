<template>
  <Input
    v-model="current_search_input"
    placeholder="请输入内容"
    v-on:keyup.enter.native="doSearch">
    <Select v-model="current_search_type" slot="prepend" placeholder="请选择">
      <Option
        v-for="item in search_types"
        :key="item.value"
        :value="item.value">
        {{item.label}}
      </Option>
    </Select>
    <Button slot="append" icon="ios-search" v-on:click="doSearch"></Button>
  </Input>
</template>

<script>
  import "babel-polyfill";

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
          this.$emit('update-search-input', value);
        }
      },
      current_search_type: {
        get(){
          return this.search_type;
        },
        set(value){
          this.$emit('update-search-type', value);
        }
      }
    },
    methods: {
      doSearch: function(event){
        let search_type = this.current_search_type;
        let search_input = this.current_search_input;
        this.$emit('do-search', {
          search_type: search_type,
          search_input: search_input
        })
      }
    }
  }
</script>

<style scoped>
  .ivu-select {
    min-width: 100px;
  }
</style>