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
        if(this.$refs.child.contracts){
            this.$refs.child.contracts.forEach((contract) => {
            if(contract.checked) contract.checked=false;
        });
        }else if(this.$refs.child.coinContract){
            this.$refs.child.coinContract.forEach((item) => {
             item.Contracts.forEach((contract) =>{
                if(contract.checked){
                  contract.checked=false
                }
             })
        });
        }else{
          console.log("None of the child components was found")
        }


      }
    }
  }

</script>

<style>
  #app{

  }
</style>