<template>
  <div class="search-table">
    <div class="search">
      <el-select
          v-model="property"
          filterable
          placeholder="Enter an address"
          v-on:change="handleSelect"
          style="width: 30em"
      >
        <el-option
            v-for="property in unselectedProperties"
            :key="property.property_id"
            :value="property.property_id"
            :label="property.full_address"
        >
        </el-option>
      </el-select>
    </div>
    <div class="table">
      <el-table
          :data="selectedProperties"
          style="width: 100%"
      >
        <el-table-column prop="full_address" label="Full Address"/>
        <el-table-column prop="class_description" label="Class Description"/>
        <el-table-column label="Remove?">
          <template #default="scope">
            <el-button
                @click="handleDelete(scope)"
                type="danger"
            >
              Delete
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import http from "../http-common";

export default {
  name: "SelectionsTable",
  data() {
    return {
      searchAddress: '',
      unselectedProperties: [],
      selectedProperties: [],
      loading: false,
    }
  },
  mounted() {
    this.getUnselectedProperties()
    this.getSelectedProperties()
  },
  methods: {
    async getUnselectedProperties() {
      http
          .get(`/properties?selected=false`)
          .then(response => (
              this.unselectedProperties = response.data
          ))
          .catch((error) => {
            console.error(error)
          })
    },
    async getSelectedProperties() {
      http
          .get(`/properties?selected=true`)
          .then(response => (
              this.selectedProperties = response.data
          ))
          .catch((error) => {
            console.error(error)
          })
    },
    async handleDelete(scope) {
      try {
        await http
            .put(`/properties/${scope.row.property_id}`, {
              "selected": false
            })
      } finally {
        await this.getUnselectedProperties()
        await this.getSelectedProperties()
      }
    },
    async handleSelect(event) {
      try {
        await http
            .put(`/properties/${event}`, {
              "selected": true
            })
      } finally {
        await this.getUnselectedProperties()
        await this.getSelectedProperties()
        this.value = ''
      }
    }
  },
  props: {},
};
</script>

<style scoped lang="scss">
.search {
  margin: 1em;
}

.table-with-search {
  margin-left: auto;
  margin-right: auto;
  padding: 1em;
}
</style>
