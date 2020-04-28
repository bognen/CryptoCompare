<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>
<script>
  import Footer from "./components/parts/Footer";
  import Header from "./components/parts/Header";
  export default {
    components: {Header, Footer}
  }
</script>

<style>
  #app{

  }
</style>