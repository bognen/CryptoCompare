<template>
    <div class="main-div"  style="background-color: #f5f5f5">
         <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">Cloud Mining Contracts</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!----------------------------------------------------------------------------------->
        <tile :loading="isLoading" v-if="isLoading"></tile>
        <div class="container" style="margin: 25px auto 0; width:55%; background-color: white" :disabled="isLoading">
              <SingleContractComponent v-for="c in contracts" :key="c._id" :contractInfo="c" @cCheck="checkAction"></SingleContractComponent>
        </div>

    </div>
</template>

<script>
    import Vue from 'vue'
    import ContractComponent from "./ContractComponent";
    import axios from 'axios';
    import VueSpinners from 'vue-spinners'
    Vue.use(VueSpinners)

    export default {
        name: "ContractList",
        data() {
            return {
                contracts: [],
                isLoading: true,
            }
        },

       created() {
            axios.get(process.env.VUE_APP_DATA_URL+`/api/contracts`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.contracts = JSON.parse(response.data)
                    this.isLoading=false
                })
                .catch(e => {
                    this.errors.push(e)
                })
        },

        components:{
            SingleContractComponent: ContractComponent,
        },

        methods:{
            checkAction(contract){
                //this.$emit('contractChecked', contract);
                this.$root.$emit('toggle', contract);
            }
        }

    }
</script>

<style scoped>

</style>