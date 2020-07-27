<template>
    <div class="main-div" v-if="contract">
        <section class="banner-area relative">
        <div class="overlay overlay-bg"></div>
        <div class="container">
            <div class="row d-flex align-items-center justify-content-start" style="padding-top: 100px; padding-bottom: 70px">
                <div class="banner-content col-lg-12 col-md-12">
                    <h5 class="text-white text-uppercase">The Deal of The Day</h5>
                    <h1 class="text-uppercase">
                    {{contract.name}}
                    </h1>
                    <h4  class="text-white text-uppercase">by {{contract.company.title}}</h4>
                    <p class="text-white pt-20 pb-20">
                        {{contract.description}}
                    </p>
                    <router-link :to="`contract/${contract._id}`" class="primary-btn header-btn text-uppercase mb-20">Find Out More</router-link>
                </div>
            </div>
        </div>
        </section>

        <div class="hello">
            <section class="convert-area" id="convert">
                <div class="container">
                    <div class="convert-wrap">
                        <div class="row justify-content-center align-items-center flex-column pb-30">
                            <h2 class="text-white" style="width:70%; margin: 0 auto;">
                                So, how exactly Cloud Mining Works...
                            </h2>
                        </div>
                    <div class="row justify-content-center align-items-start">
                        <p class="text-white-front">
                            Cloud mining is the way to mine a cryptocurrency  without having to install all the hardware and related paraphernalia. There are companies that allow people to open an account with them and participate in the process of cloud mining for a basic cost.
                            The mining rigs are housed and maintained in a facility owned by mining company and the customer simply needs to register and purchase mining contracts or shares. Since Cloud Mining is provided as a service there is generally some cost and this can result in lower returns for the miner
                        </p>
                    </div>
                        <div class="text-center" style="width:70%; margin: 0 auto;">
                            <router-link to="/contracts" class="primary-btn header-btn text-uppercase mb-20">Explore Mining Contracts</router-link>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
      name: 'Home',
      data(){
          return{
              contract: null,
              errors:[]
        }
      },

       created() {
           axios.get(process.env.VUE_APP_DATA_URL+`/api/most-profitable/`)
            .then(response => {
                this.contract = JSON.parse(response.data)
            })
            .catch(e => {
                this.errors.push(e)
            })
        }
    }
</script>

