<template>
  <el-container id="app" class="npdp-cover-container">
    <el-header class="npdp-cover-header">
      <h1>NPDP</h1>
    </el-header>
    <el-main class="npdp-cover-main">
      <el-row style="width:80%">
        <el-col :span="24">
          <el-input placeholder="请输入内容" v-model="search_input">
            <el-select v-model="search_type" slot="prepend" placeholder="请选择">
              <el-option label="全部" value="all"></el-option>
              <el-option label="FTP" value="destination"></el-option>
              <el-option label="产品" value="product"></el-option>
              <el-option label="模式" value="operation_system"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
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

  export default {
    name: 'Welcome',
    computed: {
      search_input: {
        get() {
          return this.$store.state.search_input;
        },
        set(value) {
          this.$store.commit('updateSearchInput', value)
        }
      },

      search_type: {
        get() {
          return this.$store.state.search_type;
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