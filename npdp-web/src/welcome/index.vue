<template>
  <el-container id="app" class="npdp-cover-container">
    <el-header class="npdp-cover-header">
      <h1>NPDP</h1>
    </el-header>
    <el-main class="npdp-cover-main">
      <el-row style="width:80%">
        <el-col :span="24">
          <SearchBar
            v-bind:search_input="search_input"
            v-bind:search_type="search_type"
            v-bind:search_types="search_types"
          />
        </el-col>
      </el-row>
    </el-main>
    <el-footer class="npdp-cover-footer">
      <el-row>
        <el-col :span="12">
          <p>Copyright 2018, NWPC</p>
        </el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>

<script>
  import SearchBar from './search_bar.vue'
  export default {
    name: 'Welcome',
    components: {
      SearchBar
    },
    computed: {
      search_types() {
        return this.$store.state.welcome.search_types;
      },
      search_input: {
        get() {
          return this.$store.state.welcome.search_input;
        },
        set(value) {
          this.$store.commit('updateSearchInput', value)
        }
      },
      search_type: {
        get() {
          return this.$store.state.welcome.search_type;
        },
        set(value) {
          this.$store.commit('updateSearchType', value)
        }
      }
    }
  }
</script>

<style scoped>
</style>