<template>
    <div>
        <div class="row mb-2 pt-1" style="border-bottom: 2px solid #CCCCCC">
            <div class="col-lg-2 col-md-12 image-column"><img class="image-icon" v-bind:src="contract.company.image" /></div>
            <div class="col-lg-10 col-md-12 main-column">
                <div class="on-top-column">
                    <a :href="`/contract/${contract._id}`"><span class="contract-name">{{contract.name}}</span></a>&nbsp;&nbsp;&nbsp;
                    <span class="contract-duration">{{contract.duration==9999?"Lifetime":contract.duration+" Months"}}</span>
                    <div style="display: inline" class="float-right">
                        <input type="checkbox" v-model="contract.checked" :value="`contract-${contract._id}`" :id="`contract-${contract._id}`" v-on:click='checkedContract(contract)'/>
                        <label :for="`contract-${contract._id}`" type="text">Compare</label>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                        <div class="column-header">Price:</div>
                        <div class="column-value">$ {{contract.price}}</div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6 column-block last-when-small">
                        <div class="column-header">Hash Rate:</div>
                        <div class="column-value">{{contract.hashRate}} GH/s</div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                        <div class="column-header">Mines:</div>
                        <div class="column-value">{{contract.coin.name}}</div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6 column-block last-block">
                        <div class="column-header">Company:</div>
                        <div class="column-value">{{contract.company.title}}</div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    // import $ from 'jquery';

    export default {
        name: "ContractComponent",
        props:{
            contractInfo: {
                type: Object
            }
          },
        data(){
            return{
                contract: null,
            }
        },

        created(){
          this.contract = this.$props.contractInfo;
        },

        methods:{
            checkedContract(contract){
                this.$emit('cCheck', contract);
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
</style>