<template>
  <div class="app">
    <div class="header">
      <h1>Enodo Skills Assessment Challenge</h1>
    </div>
    <div>
      <Table/>
    </div>
  </div>
</template>

<script>

import Table from "./components/EstateTable.vue";

export default {
  name: "App",
  components: {
    Table
  },
};
</script>

<style lang="scss">
html {
  background-color: $primary;
}

h1 {
  color: $secondary;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
  height: 100%;
}
</style>
