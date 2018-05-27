<template>
  <el-container id="app">
    <el-header>
      <el-row type="flex" align="middle">
        <el-col :span="2"><h1>NPDP</h1></el-col>
        <el-col :span="20">
          <SearchBar
            :search_input="search_input"
            :search_type="search_type"
            :search_types="search_types"
            @update-search-input="search_input=$event"
            @update-search-type="search_type=$event"
            @do-search="doSearch"
          />
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      Search Results
    </el-main>
    <el-footer>
      <Footer/>
    </el-footer>
  </el-container>
</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import Footer from '../../components/footer.vue'

  export default {
    name: 'SearchApp',
    components: {
      SearchBar,
      Footer
    },
    props:[
      'type',
      'context'
    ],
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
      doSearch: function(payload){
        console.log('[SearchApp] doSearch', payload);
        this.$store.dispatch('executeSearch', payload);
      }
    },
    mounted: function(){
      const payload = {
        search_type: this.type,
        search_input: this.context
      };
      this.$store.commit('updateSearch', payload);
      this.doSearch(payload);
    }
  }
</script>

<style scoped>
</style>