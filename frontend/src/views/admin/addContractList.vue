<template>
   <div>
       <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">List of Contracts</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
       <div class="container" style="margin-top: 1rem; width: 90%!important">
           <div class="row">
                <h2>Existing Contracts</h2>
                <button type="button" class="btn btn-primary ml-auto" v-on:click="createContract()">Add New</button>
           </div>
           <table class="table table-striped table-hover mt-5 mb-5">
                 <thead>
                    <tr>
                      <th scope="col">Company</th>
                      <th scope="col">Coin</th>
                      <th scope="col">Name</th>
                      <th scope="col">Duration</th>
                      <th scope="col">Price</th>
                      <th scope="col">Hash Rate</th>
                      <th scope="col">Description</th>
                      <th></th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="c in contracts" :key="c.id"  @dblclick="activateContract(c)">
                      <td>{{c.company.title}}</td>
                      <td>{{c.coin.name}}</td>
                      <td>{{c.name}}</td>
                      <td>{{c.duration}}</td>
                      <td>{{c.price}}</td>
                      <td>{{c.hashRate}}</td>
                      <td>{{c.description.substring(0,35)+"..."}}</td>
                      <td>
                            <a :href="`contract/${c._id}`"><i class="fa fa-pencil-square-o fa-lg" aria-hidden="true"></i></a>
                      </td>
                      <td>
                            <span class="admin-contract-delete-span" v-on:click="deleteContract(c._id)"><i class="fa fa-trash fa-lg"></i></span>
                      </td>
                    </tr>
                  </tbody>
           </table>
       </div>
   </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "addContractList",
        data(){
            return{
                contracts: [],
            }
        },
        // Fetches posts when the component is created.
        created() {
            //axios.all([companiesRequest, coinRequest, contractRequest]).then(axios.spread((...responses) => {
            axios.get("http://localhost:8000/api/contracts").then(response => {
                //this.companies = responses[0].data;
                //this.coins = responses[1].data;
                this.contracts = JSON.parse(response.data);
                console.log(this.contracts)
            })
                .catch(e => {
                    this.errors.push(e)
                })
        },
       methods:{
          async createContract(){
                this.$router.push('/admin/contract')
            },
           async  deleteContract(id){
                console.log(id)
                alert('');
                axios.delete('http://localhost:8000/api/deletecontract/'+id).then(response => {
                       console.log(response.data);
                       //this.$router.push({ path: this.$route.path })
                       window.location.href = '/admin/contracts'
                    }).catch(e => {
                        this.errors.push(e);
                })
            }
        }
    }
</script>

<style scoped>

 .admin-contract-delete-span{
     color: #bd2130;
 }
    .admin-contract-delete-span:hover{
        cursor:pointer;
    }

</style>