<template>
  <Layout id="app">
    <Header>
      <Row type="flex" align="middle">
        <Col span="2"><h1><router-link to="/" style="text-decoration:none;color:white">NPDP</router-link></h1></Col>
        <Col span="20">
          <SearchBar
            :search_input="search_input"
            :search_type="search_type"
            :search_types="search_types"
            @update-search-input="search_input=$event"
            @update-search-type="search_type=$event"
            @do-search="doSearch"
          />
        </Col>
      </Row>
    </Header>
    <Content>
      <SearchResultList
        :search_results="search_results"
      />
    </Content>
    <Footer>
      <NPDPFooter/>
    </Footer>
  </Layout>
</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import NPDPFooter from '../../components/footer.vue'
  import SearchResultList from '../../components/search_result_list.vue'

  export default {
    name: 'SearchApp',
    components: {
      SearchBar,
      NPDPFooter,
      SearchResultList
    },
    props:[
      'type',
      'input'
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
      },
      search_results: {
        get(){
          return this.$store.state.search.search_results;
        }
      }
    },
    methods: {
      doSearch: function(payload){
        this.$router.push({
          path: 'search',
          query: {
            type: payload.search_type,
            input: payload.search_input
          }
        });
        this.executeSearch(payload);
      },
      executeSearch: function(payload){
        console.log('[SearchApp][executeSearch]', payload);
        this.$store.dispatch('executeSearch', payload);
      }
    },
    mounted: function(){
      const payload = {
        search_type: this.type,
        search_input: this.input
      };
      this.$store.commit('updateSearch', payload);
      this.executeSearch(payload);
    }
  }
</script>

<style scoped>
</style>