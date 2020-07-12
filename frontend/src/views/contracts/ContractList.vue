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

        <modal v-if="showModal" @close="showModal = false" :cForCompare1="modalContractId1" :cForCompare2="modalContractId2"><p></p></modal>

        <div class="container" style="margin: 25px auto 0; width:55%; background-color: white">
            <div class="row mb-2 pt-1" v-for="c in contracts" :key="c._id" style="border-bottom: 2px solid #CCCCCC">
                <div class="col-lg-2 col-md-12 image-column"><img class="image-icon" v-bind:src="c.company.image" /></div>
                <div class="col-lg-10 col-md-12 main-column">
                    <div class="on-top-column">
                        <a href="/contract"><span class="contract-name">{{c.name}}</span></a>&nbsp;&nbsp;&nbsp;
                        <span class="contract-duration">{{c.duration==9999?"Lifetime":c.duration+" Months"}}</span>
                        <div style="display: inline" class="float-right">
                            <input type="checkbox" v-model="c.checked" :value="`contract-${c._id}`" :id="`contract-${c._id}`" v-on:click='toggle(c)'/>
                            <label :for="`contract-${c._id}`" type="text">Compare</label>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                            <div class="column-header">Price:</div>
                            <div class="column-value">$ {{c.price}}</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block last-when-small">
                            <div class="column-header">Hash Rate:</div>
                            <div class="column-value">{{c.hashRate}} GH/s</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                            <div class="column-header">Mines:</div>
                            <div class="column-value">{{c.coin.name}}</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block last-block">
                            <div class="column-header">Company:</div>
                            <div class="column-value">{{c.company.title}}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

       <div>
        <div class="fixed-bottom">
           <div class="content" v-bind:class="{ handleOpened: isOpen }" >
             <transition name="slide">
              <div class="container box" v-if="isOpen">
                  <div class="toggle-header">You have selected contracts for compare</div>
                  <div class="row toggle-row justify-content-center align-items-center">
                      <div class="col-lg-4 col-md-5 toggle-cube">
                          <!--span v-html="sContract1"></span-->
                          <component :is="currentFirstComponent" :contractDetail="firstContractDetails" :isFilled="isFirstFilled" @change="changeLayout"/>
                      </div>
                      <div class="col-lg-4 col-md-5 toggle-cube">
                          <!--span v-html="sContract2"></span-->
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
    </div>
</template>

<script>
    import axios from 'axios';
    import $ from 'jquery';

    export default {
        name: "ContractList",
        data() {
            return {
                contracts: [],
                isOpen: false,
                selectedContracts: 0,

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
                         '<div class="modal-dialog">' +
                             '<div class="modal-content" style="top:150px!important; opacity: 1!important;">' +
                                 '<div class="modal-header">' +
                                     '<h4 class="modal-title">Contracts Comparison</h4>' +
                                     '<button type="button" @click="$emit(\'close\')" class="close"><span >&times;</span></button>' +
                                 '</div>' +
                                 '<div class="modal-body">{{test}}' +
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
            }
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
                  }
              }
            }
        },


        created() {
            axios.get(`http://localhost:8000/api/contracts`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.contracts = JSON.parse(response.data)
                })
                .catch(e => {
                    this.errors.push(e)
                })
        },
        methods: {
            open() {
                this.isOpen = true;
            },
            close() {
                this.isOpen = false;
            },
            toggle(contract) {
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

                console.log(this.firstContractDetails._id)

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
                this.contracts.forEach((contract) => {
                    if(contract.checked) contract.checked=false;
                });
            }

        }
    }
</script>

<style scoped>
.image-column{
    padding-left: 0!important;
    padding-right: 0!important;
}
.main-column{
    padding-left: 0!important;
}
.on-top-column{
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}
.column-block{
    text-align: right;
    border-right: 1px solid #b0b0b0;
}

.last-block{
    border-right: none;
}

.contract-name{
    color: #337ab7;
    font-size: 20px;
    font-weight: bold;
}
.contract-duration{
    color: #82ae52;
    font-size: 18px;
    font-family: open sans condensed,sans-serif;
}
.column-value{
    color: #000;
    font-size: 16px;
    font-weight: bold;
}
@media (max-width: 992px) {
    .image-icon {
        display: block;
        margin: 0 auto;
    }
    .on-top-column{
        text-align: center;
    }

    .last-when-small{
        border: none;
    }

    .compare-button{
        margin-top: 8px;
    }

    .box {
      height: 260px!important;
    }
}

@media (max-width: 578px) {
    .column-block{
        text-align:center;
        width: 50%!important;
    }
}

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

/********  TOGGLE   ********/
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
     /* background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    opacity:1!important;

}
/*
.modal-content{
    top:150px!important;
    opacity: 1!important;
}

/***************************/
</style>