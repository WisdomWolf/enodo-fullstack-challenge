<template>
  <div class="container">
    <div class="row">
      <div class="el-col-sm-10">
        <h1>Real Estate Properties</h1>
        <hr><br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Full Address</th>
            <th scope="col">Class Description</th>
            <th scope="col">Remove?</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(asset, index) in assets" :key="index">
            <td>{{ asset.property_id }}</td>
            <td>{{ asset.class_description }}</td>
            <td>
              <button type="button" class="btn btn-warning btn-sm">Delete</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "PropertiesTable",
  data() {
    return {
      assets: []
    }
  },
  methods: {
    getSelectedProperties() {
      const path = '/api/properties/selected'
      axios.get(path)
            .then((res) => {
              this.assets = res.data
            })
            .catch((error) => {
              console.error(error)
            })
    }
  },
  created() {
    this.getSelectedProperties()
  }
}
</script>

<style scoped>

</style>