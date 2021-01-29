<template>
    <div class="main-div">
        <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">Add Contract</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <div id="form-div">
             <form class="add-contract-form" @submit="saveContract">
               <div class="row">
                   <label class="col-lg-6 col-form-label add-contract-label">Company:</label>
                   <label class="col-lg-6 col-form-label add-contract-label">Coin:</label>
               </div>
               <div class="row form-group">
                   <div class="col-lg-6 add-contract-field">
                       <select class="form-control" v-model="contract.company">
                           <option v-for="c in companies" :key="c.id" v-bind:value="`${c.id}`">{{c.title}}</option>
                       </select>
                   </div>
                   <div class="col-lg-6 add-contract-field">
                       <select class="form-control" id="coin" v-model="contract.coin">
                           <option v-for="c in coins" :key="c.id" :value="`${c.id}`">{{c.name}}</option>
                       </select>
                   </div>
               </div>
               <div class="row">
                     <label class="col-lg-6 col-form-label add-contract-label">Name:</label>
                     <label class="col-lg-6 col-form-label add-contract-label">Image:</label>
               </div>
               <div class="row form-group">
                   <div class="col-lg-6 add-contract-field">
                        <input type="text" placeholder="Name" v-model="contract.name" class="form-control"/>
                   </div>

                   <div class="col-lg-6 add-contract-field">
                        <input type="text" placeholder="Image" v-model="contract.image" class="form-control"/>
                   </div>
               </div>
               <div class="row">
                     <label class="col-lg-4 col-form-label add-contract-label">Duration:</label>
                     <label class="col-lg-4 col-form-label add-contract-label">Price:</label>
                     <label class="col-lg-4 col-form-label add-contract-label">Hash Rate:</label>
               </div>

               <div class="row form-group">
                   <div class="col-lg-4 add-contract-field">
                        <input type="text" placeholder="Duration" v-model="contract.duration" class="form-control"/>
                   </div>

                   <div class="col-lg-4 add-contract-field">
                        <input type="text" placeholder="Price" v-model="contract.price" class="form-control"/>
                   </div>
                   <div class="col-lg-4 add-contract-field">
                        <input type="text" placeholder="Hash Rate" v-model="contract.hashRate" class="form-control"/>
                   </div>
               </div>
              <div class="form-group">
                <label for="exampleFormControlTextarea1">Description:</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="contract.description"></textarea>
              </div>

                 <button type="button" class="btn btn-dark admin-contract-button" v-on:click="cancelEdit()">Cancel</button>
                 <button type="submit" class="btn btn-info admin-contract-button">Save</button>
           </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    let companyRequestUrl = process.env.VUE_APP_DATA_URL+"/api/companies/";
    let coinRequestUrl = process.env.VUE_APP_DATA_URL+"/api/coins/";
    let contractRequestUrl = process.env.VUE_APP_DATA_URL+"/api/contract/";

    const companiesRequest = axios.get(companyRequestUrl);
    const coinRequest = axios.get(coinRequestUrl);
    // The third axios request must be within 'export default' in order to reach $route.params

    export default {
        name: "addContract",
        data(){
            return{
                companies:[],
                coins:[],
                contract:{}
            }
        },
        // Fetches posts when the component is created.
        async created() {
            await axios.all([companiesRequest, coinRequest, axios.get(contractRequestUrl+this.$route.params.id)]).then(axios.spread((...responses) => {
                this.companies = responses[0].data;
                this.coins = responses[1].data;
                // Do not Parse anything if it is a new contract
                if(this.$route.params.id!== undefined){
                    console.log(this.$route.params.id)
                    this.contract = JSON.parse(responses[2].data)
                    this.contract.coin = JSON.parse(responses[2].data).coin._id;
                    this.contract.company = JSON.parse(responses[2].data).company._id;
                }
            }))
            .catch(e => {
                console.log(e)
                this.errors.push(e)
            })
        },
        methods:{
            cancelEdit(){
                this.$router.push('/admin/contracts');
            },
            saveContract(){
                // If if route parameter ID is not present, save the contract
                if(this.$route.params.id==null || this.$route.params.id=='undefined') {
                    axios.post(process.env.VUE_APP_DATA_URL+'/api/contracts/', this.contract)
                        .then(response => {
                            console.log(response.status)
                            if(response.status==201){
                                //this.$router.replace('/admin/contracts')
                                window.location.href = '/admin/contracts'
                            }
                        })
                        .catch(e => {
                            this.errors.push(e)
                            alert('Error');
                        })
                // If there is route parameter ID, update the contract
                }else{
                     axios.put(process.env.VUE_APP_DATA_URL+'/api/contracts/', this.contract)
                        .then(response => {
                             console.log(response.status)
                             if(response.status==201) {
                                 //this.$router.go("/admin/contracts")
                                 window.location.href = '/admin/contracts'
                             }
                        })
                        .catch(e => {
                            this.errors.push(e)
                            alert('Error');
                        })
                }
            }
        }
    }
</script>

<style scoped>
    #form-div{
        text-align: center;
    }
    .add-contract-form{
        margin-top: 1rem;
        width: 50%;
        display: inline-block;
    }
    .admin-contract-button{
        min-width: 230px;
        margin-left: 1rem;
        margin-right: 1rem;
    }
</style>