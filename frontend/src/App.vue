<template>
  <div id="app">
    <Header></Header>
        <router-view ref="child"/>
    <Footer></Footer>
    <keep-alive include="CompareContractToggle">
      <Toggle @deselectContracts="removeSelection"></Toggle>
    </keep-alive>
  </div>
</template>
<script>
  import Footer from "./components/parts/Footer";
  import Header from "./components/parts/Header";
  import Toggle from "./views/contracts/CompareContractToggle"


  export default {
    components: {Header, Footer, Toggle},
    methods:{
      removeSelection(){
        this.$refs.child.contracts.forEach((contract) => {
            if(contract.checked) contract.checked=false;
        });
      }
    }
  }

</script>

<style>
  #app{

  }
</style>