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
      <h1>Node</h1>
      <p>{{id}}</p>
      <div>
        <h2>Props</h2>
      </div>
      <div>
        <h2>Chart</h2>
      </div>
      <div>
        <h2>Relationship</h2>
      </div>
    </Content>
    <Footer>
      <NPDPFooter/>
    </Footer>
  </Layout>

</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import NPDPFooter from '../../components/footer.vue'


  export default {
    name: 'NodeApp',
    components: {
      SearchBar,
      NPDPFooter
    },
    props: [
      'id'
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
    },
    methods: {
      doSearch: function(payload) {
        this.$router.push({
          path: '/search',
          query: {
            type: payload.search_type,
            input: payload.search_input
          }
        });
      }
    },
    mounted: function(){
      const node_id = this.id;
    }
  }
</script>