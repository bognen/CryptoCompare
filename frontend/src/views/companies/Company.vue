<template>
    <div class="main-div" style="background-color: #f5f5f5">
        <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">{{company.title}}</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
       <!----------------------------------------------------------------------------------->

        <div style="margin-top:0.75rem;">
              <tile :loading="isLoading" v-if="isLoading"></tile>
              <div class="card mb-3" style="margin: 0 auto;" v-if="!isLoading">
              <div class="row no-gutters">
                <div class="col-md-3">
                  <img v-bind:src="company.image" class="card-img" alt="...">
                  <h5 class="card-title">{{company.title}}</h5>
                </div>
                <div class="col-md-9 pl-3">
                  <div class="card-body">
                    <div class="row header-row">
                              <div class="col-sm-4 inside-card-block">
                                  <div class="card-text-header"><i class="fa fa-map-marker fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Location: </div>
                                  <div class="card-text">{{company.location}}</div>
                              </div>

                              <div class="col-sm-4 inside-card-block">
                                  <div class="card-text-header"><i class="fa fa-external-link fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Website </div>
                                  <div class="card-text"><a href="">{{company.title}}</a></div>
                              </div>
                              <div class="col-sm-4 inside-card-block last-in-small">
                                  <div class="card-text-header"><i class="fa fa-money fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Coins</div>
                                  <div class="card-text" style="font-size: 16px">{{company.coins}}</div>
                              </div>
                          </div>

                          <div class="row" style="margin-top: 1rem">
                              <div class="col-sm-4 inside-card-block">
                                <div class="card-text-header"><i class="fa fa-briefcase fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Contracts:</div>
                                <div class="card-text">{{company.num_of_contracts}}</div>
                              </div>
                              <div class="col-sm-4 inside-card-block">
                                <div class="card-text-header"><i class="fa fa-calendar fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Founded:</div>
                                <div class="card-text">{{company.founded}}</div>
                              </div>
                              <div class="col-sm-4 inside-card-block last-in-small" style="border-right:none;">
                                <div class="card-text-header">Reliability</div>
                                      <div class="card-text">
                                          <img v-if="company.legitimacy === 'Checked'" src="/img/trust.png" :title="`${company.legitimacy}`"/>
                                          <img v-else-if="company.legitimacy === 'Questionable'" src="/img/questionable.png" :title="`${company.legitimacy}`"/>
                                          <img v-else src="/img/avoid.png" :title="`${company.legitimacy}`"/>
                                      </div>
                              </div>
                          </div>
                  </div>
                </div>

                <div class="company-description">
                  {{company.description}}
                </div>
                   <h3 style="margin-left: 0.5rem">Offered Contracts:</h3>
                   <div class="row contract-row" style="margin-left: 0.5rem!important; ; margin-bottom: 0.5rem!important;">
                        <div v-for="(cc, index) in coinContract" :key="cc.CoinToken" class="col-md-2 coin-bookmark pt-2"
                             @click='show = cc.CoinName, activeDiv=index++'
                             v-bind:style="{'background-color':bkgColor[index],'border-bottom':brdBtm[index]}">
                            <div class="coin-bookmark-full-name">{{cc.CoinName}}</div>
                            <div class="coin-bookmark-token">{{cc.CoinToken}}</div>
                        </div>
                   </div>
                   <div  v-for="cc in coinContract" :key="cc.CoinName" v-show="show === cc.CoinName" class="contract-row">
                       <!---------------------------------------------------------------------------------->
                   <SingleContractComponent v-for="contract in cc.Contracts" :key="contract._id" v-show="show === cc.CoinName"  :contractInfo="contract" @cCheck="checkAction"></SingleContractComponent>
                   </div>

              </div>
            </div>
       </div>
        <!----------------------------------------------------------------------------------->
    </div>
</template>

<script>
    import Vue from 'vue'
    import axios from 'axios';
    import ContractComponent from "./../contracts/ContractComponent";
    import VueSpinners from 'vue-spinners'
    Vue.use(VueSpinners)

    let companyRequestUrl = process.env.VUE_APP_DATA_URL+"/api/company/";
    let coinContractRequestUrl = process.env.VUE_APP_DATA_URL+"/api/filtered-contract/";

    export default {
        name: "Company",
        data() {
            return {
                company: '',
                legPicture: '',
                coinContract: [],
                show: '',
                activeDiv: 0,
                errors: [],
                isLoading: true,
            }
        },

        // Fetches posts when the component is created.
        created() {
            axios.all([axios.get(companyRequestUrl+this.$route.params.id), axios.get(coinContractRequestUrl+this.$route.params.id)]).
            then(axios.spread((...responses) => {
                    this.company =  responses[0].data
                    this.coinContract = responses[1].data
                    this.show = this.coinContract[0].CoinName
                    this.isLoading = false

                }))
                .catch(e => {
                    this.errors.push(e)
                })
        },
        computed: {
            bkgColor: function(){
                let result = this.testFunc('#FFF', '#dedede');
                return result;
            },
            brdBtm: function(){
                let result = this.testFunc('none', '');
                return result;
            }
        },

        components:{
            SingleContractComponent: ContractComponent,
        },

        methods:{
            testFunc: function(active, nonActive){
                let len = this.coinContract.length;
                let result =[];
                for (let i = 0; i<len; i++){
                    if (this.activeDiv == i){
                      result.push(active);
                    } else {
                      result.push(nonActive);
                    }
                  }

                  return result;
            },
             checkAction(contract) {
                 //this.$emit('contractChecked', contract);
                 this.$root.$emit('toggle', contract);
             }
        }
    }
</script>

<style>
    .card{
        width:65%;
        height:auto;
        border: none!important;
    }

    .coin-bookmark-token{
        display: none;
    }

    .card-img{
       /* margin-left: 0.5rem;
        margin-top: 0.5rem; */
        max-width: 150px;
        display:block;
        margin:auto;
    }

    .card-title{
        color: #3c3ecf;
        font-size: 1.6em;
        font-family: "Arial Black", Gadget, sans-serif;
        text-align: center;
    }

    .card-text-header{
            font-size: 14px;
            text-align: center;
    }

    .card-text{
        font-weight: 700;
        font-size:20px;
        text-align: center;
    }

    .inside-card-block{
        border-right: 1px solid #dedede;
    }

    .header-row{
    line-height: 35px;
    }

    .marker-icons{
        color: #b0b0b0;
        top: 50%;
    }

    .company-description{
        margin: 0.5rem;
    }

    .last-in-small{
        border-right: none;
    }

    .contract-row{
        width: 100%;
        margin-left: 1.5rem!important;
        margin-right: 1.5rem!important;
    }

    .coin-bookmark{
        border: 1px solid #777777;
        cursor: pointer;
        font-size: 0.8rem;
        font-weight: bold;
    }

    @media (max-width: 992px) {
        .coin-bookmark-token{
            display: block;
        }

        .coin-bookmark-full-name{
            display: none;
        }
    }
</style>