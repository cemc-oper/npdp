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
            v-on:update-search-input="search_input=$event"
            v-on:update-search-type="search_type=$event"
            v-on:do-search="doSearch"
          />
        </el-col>
      </el-row>
    </el-main>
    <el-footer class="npdp-cover-footer">
      <Footer/>
    </el-footer>
  </el-container>
</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import Footer from '../../components/footer.vue'

  export default {
    name: 'WelcomeApp',
    components: {
      SearchBar,
      Footer
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
      doSearch(payload){
        this.$router.push({
          path: 'search',
          query: {
            type: payload.search_type,
            input: payload.search_input
          }
        })
      }
    }
  }
</script>

<style scoped>
</style>