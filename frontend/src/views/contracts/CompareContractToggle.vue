<template>
    <div>
    <modal v-if="showModal" @close="showModal = false" :cForCompare1="modalContractId1" :cForCompare2="modalContractId2"></modal>
        <div class="fixed-bottom">
           <div class="content" v-bind:class="{ handleOpened: isOpen }" >
             <transition name="slide">
              <div class="container box" v-if="isOpen">
                  <div class="toggle-header">You have selected {{selectedContracts}} of 2 contracts</div>
                  <div class="row toggle-row justify-content-center align-items-center">
                      <div class="col-lg-4 col-md-5 toggle-cube">
                          <component :is="currentFirstComponent" :contractDetail="firstContractDetails" :isFilled="isFirstFilled" @change="changeLayout"/>
                      </div>
                      <div class="col-lg-4 col-md-5 toggle-cube">
                           <component :is="currentSecondComponent" :contractDetail="secondContractDetails" :isFilled="isSecondFilled" @change="changeLayout"/>
                      </div>
                      <div class="col-lg-2 col-md-12 text-center">
                          <button class="btn btn-warning compare-button" :disabled="selectedContracts < 2" @click="compareContracts">
                              Compare
                          </button>
                      </div>
                  </div>
              </div>
          </transition>
          </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue';
    import VueCookies from 'vue-cookies'
    Vue.use(VueCookies)
    import $ from 'jquery';
    import axios from 'axios';
    let numeral = require("numeral");

    export default {
        name: "CompareContractToggle",
        data(){
            return{
                isOpen: false,
                selectedContracts: 0,
                cookiesArray: [],

                currentFirstComponent: null,
                currentSecondComponent: null,

                firstContractDetails: "First",
                secondContractDetails: "Second",

                isFirstFilled: false,
                isSecondFilled: false,

                showModal:false,
                modalContractId1: null,
                modalContractId2: null,
            }
        },
        components:{
                "modal":{
                     props:['cForCompare1','cForCompare2'],
                     template:
                         '<div class="modal fade in modal-active">' +
                             '<div class="modal-dialog modal-lg">' +
                                 '<div class="modal-content" style="top:150px!important; opacity: 1!important;">' +
                                     '<div class="modal-header">' +
                                         '<h4 class="modal-title" style="border-bottom: none;">Contracts Comparison</h4>' +
                                         '<button type="button" @click="$emit(\'close\')" class="close"><span >&times;</span></button>' +
                                     '</div>' +
                                     '<div class="modal-body">' +
                                         '<table class="table table-striped">' +
                                              '<thead>' +
                                                '<tr>' +
                                                  '<th scope="col"></th>' +
                                                  '<th scope="col text-center">{{firstContract.name}}</th>' +
                                                  '<th scope="col text-center">{{secondContract.name}}</th>' +
                                                '</tr>' +
                                              '</thead>' +
                                              '<tbody>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Day</th>' +
                                                  '<td class="text-center">$ {{firstContractDetails.dailyProfit | formatNumber}}</td>' +
                                                  '<td class="text-center">$ {{secondContractDetails.dailyProfit | formatNumber}}</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Week</th>' +
                                                  '<td class="text-center">$ {{firstContractDetails.weeklyProfit | formatNumber}}</td>' +
                                                  '<td class="text-center">$ {{secondContractDetails.weeklyProfit | formatNumber}}</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Month</th>' +
                                                  '<td class="text-center">$ {{firstContractDetails.monthlyProfit | formatNumber}}</td>' +
                                                  '<td class="text-center">$ {{secondContractDetails.monthlyProfit | formatNumber}}</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Total Profit</th>' +
                                                  '<td class="text-center">{{firstContractDetails.totalProfit}}</td>' +
                                                  '<td class="text-center">{{secondContractDetails.totalProfit}}</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profitablity</th>' +
                                                  '<td class="text-center">{{firstContractDetails.profitability}}</td>' +
                                                  '<td class="text-center">{{secondContractDetails.profitability}}</td>' +
                                                '</tr>' +
                                              '</tbody>' +
                                            '</table>'+
                                            '<slot></slot>' +
                                     '</div>' +
                                     '<div class="modal-footer">' +
                                        '<button type="button" class="btn btn-default" @click="$emit(\'close\')">Close</button>' +
                                     '</div>' +
                                 '</div>' +
                             '</div>' +
                         '</div>',
                    data(){
                        return{
                            firstContract: "",
                            secondContract: "",
                            firstContractDetails: "",
                            secondContractDetails: "",
                        }
                    },
                    mounted: function () {
                        this.firstContract = this.$props.cForCompare1;
                        this.secondContract = this.$props.cForCompare2;
                        this.firstContractDetails = this.calcContractParams(this.firstContract)
                        this.secondContractDetails = this.calcContractParams(this.secondContract)
                    },
                    methods:{
                         calcContractParams(contract){
                            let contractParams = {
                                "dailyProfit": 0,
                                "weeklyProfit": 0,
                                "monthlyProfit": 0,
                                "totalProfit": "Not Applicable",
                                "profitability": "Not Applicable"

                            }
                            axios.get('https://mineable-coins.p.rapidapi.com/coins?list='+contract.coin.token, {
                                "method": "GET",
                                "headers": {
                                    "x-rapidapi-host": "mineable-coins.p.rapidapi.com",
                                    "x-rapidapi-key": process.env.VUE_APP_RAPID_KEY
                                }
                            })
                                .then(
                                    coinDetailResponse =>{
                                        this.coinParams= coinDetailResponse.data

                                        let costPerDay = (contract.duration < 60) ? contract.price/contract.duration/30 : contract.price/60/30
                                        let minedPerDay = parseFloat(contract.coin.blockReward) * (1440 / parseFloat(contract.coin.blockTime)) * (parseFloat(contract.hashRate) / (parseFloat(this.coinParams[0].network_hashrate) / 1000000000))
                                        let revenuePerDay = minedPerDay * (parseFloat(this.coinParams[0].price))

                                        contractParams.dailyProfit = revenuePerDay - costPerDay
                                        contractParams.weeklyProfit = (revenuePerDay - costPerDay)*7
                                        contractParams.monthlyProfit = (revenuePerDay - costPerDay)*30
                                        if(contract.duration!=9999) {
                                            let profit = revenuePerDay * 30 * parseFloat(contract.duration) - contract.price
                                            contractParams.totalProfit = "$ "+profit.toFixed(2)
                                            let profitability = (revenuePerDay * 30 * parseFloat(contract.duration) - contract.price) / contract.price * 100
                                            contractParams.profitability = profitability.toFixed(2)+" %"
                                        }

                                    }
                            )
                            return contractParams
                         }
                    },
                    filters:{
                        "formatNumber": function (value) {
                                return numeral(value).format("0.00");
                        }
                    }
                },
            },
        created(){
           let cookContract = Vue.$cookies.get('Compare_Contract');
           let tContracts = JSON.parse(cookContract)
           if(tContracts && tContracts.length>0){
               tContracts.forEach((c) => {
                   this.selectedContracts += 1
                   this.addContractDetails(c);
               })

               this.open()
           }
        },

            mounted(){
                this.$root.$on('toggle', contract => {
                    // Handles check/uncheck box
                    if (contract.checked) {
                        contract.checked = false
                        this.selectedContracts -= 1
                        // Here add logic to REMOVE from selected ARRAY
                        this.removeContractDetails(contract)
                    // Do not allow to check more than two items to be selected
                    } else if (!contract.checked && this.selectedContracts == 2) {
                        let cbxId = "#contract-" + contract._id
                        $(cbxId).prop('checked', false);
                        contract.checked = false;
                    } else {
                        contract.checked = true
                        this.selectedContracts += 1
                        this.addContractDetails(contract);
                    }

                    // Handles open/close modal
                    if (this.isOpen && this.selectedContracts == 0) {
                        this.close();
                    } else if (!this.isOpen && this.selectedContracts == 1) {
                        this.open(contract);
                    }
                })
            },

            computed:{
               emptySlot: function(){
                   return{
                      props: ['contractDetail'],
                      template: `<p style="padding-top: 15px">Select {{contractDetail}} Contract</p>`,
                    }
                  },

               sContract: function() {
                  return {
                    props: [`contractDetail`],
                    template:
                       '<div>' +
                           '<div style="height: 8px"><span class="toggle-close" v-on:click="clearContract(contractDetail)">&times;</span></div>'+
                           '<div style="text-align: center; margin-top: 5px">'+
                              '<div style="display: inline">{{contractDetail.company.title}}</div>' +
                              '<span>&nbsp;</span><span>&#47;</span><span>&nbsp;</span>'+
                              '<div style="display: inline">{{contractDetail.coin.name}}</div>' +
                           '</div>'+
                           '<img style="width:75px; display:block; margin:0 auto" v-bind:src="contractDetail.company.image"/>' +
                                  '<div style="text-align: center">{{contractDetail.name}}</div>' +
                                  '<div style="display: none">{{contractDetail._id}}</div>' +
                       '</div>',
                      methods:{
                        clearContract(contract){
                            this.$emit('change', contract);
                        }
                      },
                  }
                }
            },

            methods: {
                open() {
                    this.isOpen = true;
                },
                close() {
                    this.isOpen = false;
                },

                // Method adds a contracts to the toggle
                addContractDetails(contract){
                    // Add contract to Cookies Array
                    this.addToCookiesArray(contract)
                    // If both slots are empty
                    if(!this.isFirstFilled && !this.isSecondFilled){
                        this.currentFirstComponent = this.sContract;
                        this.currentSecondComponent = this.emptySlot;
                        this.firstContractDetails = contract;
                        this.secondContractDetails = "Second"
                        this.isFirstFilled = true;
                        this.isSecondFilled = false;
                    // If the first slot is empty and second is filled
                    }else if(!this.isFirstFilled && this.isSecondFilled){
                        this.currentFirstComponent = this.sContract;
                        this.firstContractDetails = contract;
                        this.isFirstFilled = true;
                    // If the first slot is filled and the second is empty
                    }else if(this.isFirstFilled && !this.isSecondFilled){
                        this.currentSecondComponent = this.sContract;
                        this.secondContractDetails = contract;
                        this.isSecondFilled = true;
                    }else{
                        console.log("An error has occurred!");
                    }
                },

                // ***********************************************************************
                // Method removes a contract from a toggle
                // Compares contract that user wants to remove, if it is not the first one
                // than delete the second one
                removeContractDetails(contract){
                   // Remove from Cookies Array
                   this.removeFromCookiesArray(contract)

                   if(this.firstContractDetails._id == contract._id){
                        this.currentFirstComponent = this.emptySlot;
                        this.firstContractDetails = "First";
                        this.isFirstFilled = false;
                   }else{
                        this.currentSecondComponent = this.emptySlot;
                        this.secondContractDetails = "Second";
                        this.isSecondFilled = false;
                   }
                },

                // ***********************************************************************
                // The method handles click on (x) span on the toggle
                changeLayout(contract){
                    this.removeContractDetails(contract);
                    let cbxId = "#contract-" + contract._id
                    $(cbxId).prop('checked', false);
                    contract.checked = false;
                    this.selectedContracts -= 1;
                    if(this.selectedContracts == 0) this.close();
                },

                // ***********************************************************************
                // The method handles click on "Compare" button and sets all varialbles to
                // default state
                compareContracts(){
                    this.showModal=true;

                    this.selectedContracts=0;
                    this.currentFirstComponent=null;
                    this.currentSecondComponent=null;

                    this.modalContractId1 = this.firstContractDetails;
                    this.modalContractId2 = this.secondContractDetails;

                    // Remove checkmarks
                    this.removeCheckMark(this.firstContractDetails._id);
                    this.removeCheckMark(this.secondContractDetails._id);

                    this.firstContractDetails="First";
                    this.secondContractDetails="Second";

                    this.isFirstFilled=false;
                    this.isSecondFilled=false;

                    // Set Contract Selected property back to false
                    this.revertContractSelection();

                    // Clean out cookies
                    //console.log("PRESENT!")
                    Vue.$cookies.set('Compare_Contract', null);

                    // Close modal
                    this.close();
                },

                // ***********************************************************************
                // The method handles removing checkmarks from a given DOM object
                removeCheckMark(id){
                    let cbxId = "#contract-"+id;
                    $(cbxId).prop('checked', false);
                },

                // ***********************************************************************
                // The method sets checked property of a contract back to FALSE
                revertContractSelection(){
                     this.$emit('deselectContracts');
                },

                // ***********************************************************************
                // The method sets checked property of a contract back to FALSE
                addToCookiesArray(contract){
                    // Remove Description Parts in order to meet cookie max size criteria
                    contract.description = ""
                    contract.coin.description = ""
                    contract.company.description = ""
                    this.cookiesArray.push(contract)
                    let stringifiedCookie =  JSON.stringify(this.cookiesArray);
                    Vue.$cookies.set('Compare_Contract',stringifiedCookie);
                },

                // ***********************************************************************
                // The method sets checked property of a contract back to FALSE
                removeFromCookiesArray(contract){
                    this.cookiesArray.splice( this.cookiesArray.indexOf(contract), 1 );
                    let stringifiedCookie = JSON.stringify(this.cookiesArray);
                    Vue.$cookies.set('Compare_Contract', stringifiedCookie);
                },
            }
    }
</script>

<style scoped>
/********  ANIMATION *******/
.slide-enter-active, .slide-leave-active {
  transition: margin-bottom 1.0s ease-out;
}

.slide-enter, .slide-leave-to {
  margin-bottom: -200px;
}

.slide-enter-to, .slide-leave {
  margin-bottom: 0px;
}

/********** TOOGLE ****************/
  .content{
   background-color: #0d0d0d;
   color: white;
   opacity: 0.9;
   width: 60%;
    margin: 0 auto;
}
.box {
  height: 200px;
}

.toggle-header{
    text-align: center;
    font-size: 18px;
    padding-top: 2px;
    margin-bottom: 5px;
}
.toggle-row{
    height: 70%;
    width: 98%;
    margin: auto;
}

.toggle-cube{
    border: 1px dashed white;
    height: 100%;
    margin-left: 2px;
    margin-right: 2px;
}

.compare-button:disabled,
.compare-button[disabled]{
    border: 1px solid #999999;
    background-color: #cccccc;
    color: #666666;
    cursor: not-allowed
}

/********  MODAL   ********/
.modal-active{
	display:block;
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    opacity:1!important;

}
/***************************/
</style>