<template>
    <div>
    <modal v-if="showModal" @close="showModal = false" :cForCompare1="modalContractId1" :cForCompare2="modalContractId2"></modal>
        <div class="fixed-bottom">
           <div class="content" v-bind:class="{ handleOpened: isOpen }" >
             <transition name="slide">
              <div class="container box" v-if="isOpen">
                  <div class="toggle-header">You have selected contracts for compare</div>
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
    import $ from 'jquery';

    export default {
        name: "CompareContractToggle",
        data(){
            return{
                isOpen: false,           // toggle
                selectedContracts: 0,    //

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
                                                  '<th scope="col">First Contract Very Very Long Name</th>' +
                                                  '<th scope="col">Second Contract Very Very Long Name</th>' +
                                                '</tr>' +
                                              '</thead>' +
                                              '<tbody>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Day</th>' +
                                                  '<td class="text-center">$ 5,00</td>' +
                                                  '<td class="text-center">$ 4,80</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Week</th>' +
                                                  '<td class="text-center">$ 34</td>' +
                                                  '<td class="text-center">$ 28</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profit Per Month</th>' +
                                                  '<td class="text-center">$ 125</td>' +
                                                  '<td class="text-center">$ 104</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Total Profit</th>' +
                                                  '<td class="text-center">$ 800</td>' +
                                                  '<td class="text-center">$ 752</td>' +
                                                '</tr>' +
                                                '<tr>' +
                                                  '<th scope="row">Profitablity</th>' +
                                                  '<td class="text-center">22,4 %</td>' +
                                                  '<td class="text-center">25,7 %</td>' +
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
                            test: null,
                        }
                    },
                    mounted: function () {
                        this.test = this.$props.cForCompare1.name;
                    }
                },
            },

            mounted(){
                this.$root.$on('toggle', contract => {
                    //console.log(contract);
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
                }

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