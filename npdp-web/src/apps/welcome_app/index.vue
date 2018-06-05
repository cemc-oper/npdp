<template>
  <Layout id="app" class="npdp-cover-container">
    <Header class="npdp-cover-header">
      <h1 style="color:white">NPDP</h1>
    </Header>
    <Content class="npdp-cover-main">
      <Row style="width:80%">
        <Col span="24">
          <Row style="text-align:center;margin:20px;">
            <h2>
              Search in NWPC Product Distribution Database.
            </h2>
          </Row>
          <Row>
            <SearchBar
              v-bind:search_input="search_input"
              v-bind:search_type="search_type"
              v-bind:search_types="search_types"
              v-on:update-search-input="search_input=$event"
              v-on:update-search-type="search_type=$event"
              v-on:do-search="doSearch"
            />

          </Row>
        </Col>
      </Row>
    </Content>
    <Footer class="npdp-cover-footer">
      <NPDPFooter/>
    </Footer>
  </Layout>
</template>

<script>
  import SearchBar from '../../components/search_bar.vue'
  import NPDPFooter from '../../components/footer.vue'

  export default {
    name: 'WelcomeApp',
    components: {
      SearchBar,
      NPDPFooter
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