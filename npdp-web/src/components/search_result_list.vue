<template>
  <div>
    <el-row>
      <el-col :span="20">
        <el-row v-for="(record, index) in search_results" :key="index">
          <el-col :span="24">
            <el-row>
              <el-tag v-for="(label, index) in record.labels" :key="index">
                {{label}}
              </el-tag>
            </el-row>
            <el-row>
              {{record.props}}
            </el-row>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'SearchResultList',
    props: [
      'search_results'
    ]
  }
</script>

<style scoped>

</style>