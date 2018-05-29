<template>
  <div>
    <Row>
      <Col span="20">
        <Row v-for="(record, index) in search_results" :key="index">
          <Col span="24">
            <Row>
              <Tag color="blue" v-for="(label, index) in record.labels" :key="index">
                {{label}}
              </Tag>
            </Row>
            <Row>
              {{record.props}}
            </Row>
          </col>
        </Row>
      </Col>
    </Row>
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