<template>
  <el-container id="app">
    <el-header>
      <el-row type="flex" align="middle">
        <el-col :span="2"><h1>NPDP</h1></el-col>
        <el-col :span="20">
          <SearchBar
            v-bind:search_input="search_input"
            v-bind:search_type="search_type"
            v-bind:search_types="search_types"
            v-on:updateSearchInput="search_input=$event"
            v-on:updateSearchType="search_type=$event"
          />
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      Search Results
    </el-main>
    <el-footer>
      <el-row>
        <el-col :span="12">
          <p>Copyright 2018, NWPC</p>
        </el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  export default {
    name: 'SearchApp',
    components: {
      SearchBar
    },
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
      }
    },
    methods: {

    }
  }
</script>

<style scoped>
</style>