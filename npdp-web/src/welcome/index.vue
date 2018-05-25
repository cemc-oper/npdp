<template>
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
</template>

<script>
  export default {
    name: 'Welcome',
    data() {
      return {
        search_input: '',
        search_type: 'all'
      }
    }
  }
</script>