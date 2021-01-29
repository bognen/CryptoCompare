<template>
    <div class="main-div"  style="background-color: #f5f5f5">
         <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">Contract Name</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
         <!----------------------------------------------------------------------------------->
        <div class="container" style="margin: 25px auto 0; width:65%; background-color: white; padding-top: 1rem; padding-bottom: 1rem" v-if="contract&&coinParams">
            <div class="row">
                <img class="col-lg-2 single-contract-image" v-bind:src="contract.company.image" style="max-width: 135px;"/>
                <div class="col-lg-10 single-contract-name-duration">
                    <span class="single-contract-name">{{contract.name}} &nbsp;&nbsp;&nbsp;</span>
                    <span class="single-contract-duration">{{contract.duration==9999?"Lifetime":contract.duration+" Months"}}</span>

            <div class="row single-contract-top-row">
                <div class="col-lg-2 offset-lg-2 col-md-6 col-sm-6 single-contract-main-col">
                    <div class="single-contract-column-header">Price:</div>
                    <div class="single-contract-column-value">$ {{contract.price}}</div>
                </div>
                <div class="col-lg-2 col-md-6 col-sm-6 single-contract-main-col single-contract-sm-last">
                    <div class="single-contract-column-header">Hash Rate:</div>
                    <div class="single-contract-column-value">{{contract.hashRate}} GH/s</div>
                </div>
                <div class="col-lg-2 col-md-6 col-sm-6 single-contract-main-col">
                    <div class="single-contract-column-header">Mines:</div>
                    <div class="single-contract-column-value">{{contract.coin.name}}</div>
                </div>
                <div class="col-lg-2 col-md-6 col-sm-6 single-contract-main-col single-contract-sm-last">
                    <div class="single-contract-column-header">Company:</div>
                    <div class="single-contract-column-value">{{contract.company.title}}</div>
                </div>
                <div class="col-lg-2 col-md-12 col-sm-12 single-contract-main-col single-contract-last-col">
                    <div class="single-contract-column-header">Website:</div>
                    <div class="single-contract-column-value"><a :href="`${contract.company.website}`" target="_blank">Visit Website</a></div>
                </div>
            </div>
                </div>
            </div>

            <div class="row" style="margin-top: 0.75rem; margin-bottom: 0.75rem; padding-left: 15px; padding-right: 15px">
                <div class="col-lg-3 col-md-6 col-sm-6 single-contract-label-column">
                    <div class="label-info">Cost Per Day</div>
                    <div class="label-text">$ {{monthlyCost/30 | formatCurrency}}</div>
                    <div class="label-info">Return Per Day</div>
                    <div class="label-text">$ {{returnPerDay | formatCrypto}}</div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 single-contract-label-column">
                    <div class="label-info">Cost Per Week</div>
                    <div class="label-text">$ {{monthlyCost/30*7 | formatCurrency}}</div>
                    <div class="label-info">Return Per Week</div>
                    <div class="label-text">$ {{returnPerDay*7 | formatCurrency}}</div>
                </div>

                 <div class="col-lg-3 col-md-6 col-sm-6 single-contract-label-column">
                    <div class="label-info">Cost Per Month</div>
                    <div class="label-text">$ {{monthlyCost | formatCurrency}}</div>
                    <div class="label-info">Return Per Month</div>
                    <div class="label-text">$ {{returnPerDay*30 | formatCurrency}}</div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 single-contract-label-column">
                    <div class="label-info">Payback Period</div>
                    <div class="label-text"><span v-bind:style="profitable ? 'color: #82ae52; font-weight:600;' : 'color: #fa3c3c;font-weight:600;'">{{paybackPeriod}}</span></div>
                    <div class="label-info">Profit *</div>
                    <div class="label-text"><span v-bind:style="profitable ? 'color: #82ae52; font-weight:600;' : 'color: #fa3c3c;font-weight:600;'">{{ totalReturn }}</span></div>
                </div>
            </div>
            <!------------------------------------------------------------------------->
            <div>
                {{contract.description}}
            </div>
            <!------------------------------------------------------------------------->
            <div style="margin: 1rem 1rem 1rem 1rem; background-color:#f5f5f5">
                Disclosure: Mining contract metrics are calculated based on a network hash rate of <span class="disclosure-span">{{coinParams[0].network_hashrate/1000000000 | formatCurrency}} GH/s</span> and using exchange rate of <span class="disclosure-span">1 {{coinParams[0].coin}} = $ {{coinParams[0].price | formatCurrency}}</span>. These figures vary based on the total network hash rate and on the conversion rate. Block reward is fixed at <span class="disclosure-span">{{contract.coin.blockReward}} {{coinParams[0].coin}}</span>. Future block reward and hash rate changes are not taken into account. Network hash rate varies over time, this is just an estimation based on current values. The average block time used in the calculation is 600 seconds.
            </div>
            <div>
                * Profit is calculated as accumulated returns for the whole duration of a contract minus price of price contract
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue';
    import axios from 'axios';
    let numeral = require("numeral");

    Vue.filter("formatCurrency", function (value) {
        return numeral(value).format("0.00");
    });

    Vue.filter("formatCrypto", function (value) {
        return numeral(value).format("0.00000");
    });

    export default {
        name: "Contract",
        data(){
            return{
                contract: null,
                profitable: true,
                coinParams: null,
                monthlyCost: 0,
                returnPerDay: 0,
                totalReturn: 0,
                paybackPeriod:0,
            }
        },
       created() {
            axios.get(process.env.VUE_APP_DATA_URL+'/api/contract/'+this.$route.params.id)
            .then( contractResponse =>{
                this.contract = JSON.parse(contractResponse.data);
                console.log(this.contract)
                // Get Coin Technical Details
                axios.get('https://mineable-coins.p.rapidapi.com/coins?list='+this.contract.coin.token, {
                    "method": "GET",
                    "headers": {
                        "x-rapidapi-host": "mineable-coins.p.rapidapi.com",
                        "x-rapidapi-key": process.env.VUE_APP_RAPID_KEY
                    }
                })
                    .then(
                        coinDetailResponse =>{
                            this.coinParams= coinDetailResponse.data

                            let minedPerDay = parseFloat(this.contract.coin.blockReward) * (1440 / parseFloat(this.contract.coin.blockTime)) * (parseFloat(this.contract.hashRate) / (parseFloat(this.coinParams[0].network_hashrate) / 1000000000))
                            this.returnPerDay = minedPerDay * (parseFloat(this.coinParams[0].price))

                            this.totalReturn = this.calculateTotalProfit(this.returnPerDay*30)
                            this.paybackPeriod = this.calculatePayback(this.returnPerDay*30)
                        }
                )


                // Calculate contract monthly cost
                if(this.contract.duration>60){
                    this.monthlyCost = this.contract.price/this.contract.duration
                }else{
                    this.monthlyCost = this.contract.price/60
                }
                //***** AI add return prediction calculations here
            })
            .catch(e => {
                console.log(e)
            })
        },

        methods:{
            calculatePayback(monthlyReturn){
                let payBackPeriod = this.contract.price / monthlyReturn
                if (this.contract.duration < payBackPeriod){
                    this.profitable = false
                    return "Never"
                }else{
                    this.profitable = true
                    return Math.ceil(payBackPeriod)+" Months"
                }
            },

            // AI method needs to be refactored when AI part is fully implemented
            calculateTotalProfit(monthlyReturn){
                if(this.contract.duration==9999){
                    return "Not Applicable"
                }else {
                    let totalProfit = monthlyReturn*this.contract.duration - this.contract.price
                    let response = "$ "+totalProfit.toFixed(2)
                    return response
                }
            }
        }

    }
</script>

<style scoped>
.disclosure-span{
   /* color: #000000;*/
    font-weight: bold;
}
.single-contract-image{
    margin-bottom: 0.5rem;
}
.single-contract-name{
    font-size: 32px;
    font-weight: 700;
    color: #000;
}
.single-contract-duration{
    color: #82ae52;
    font-weight: 700;
    font-size: 18px;
}
.single-contract-top-row{
    margin-top: 0.5rem;
    text-align: right;
}
.single-contract-main-col{
    border-right: 1px solid #dedede;
}
.single-contract-last-col{
    border-right: none;
}
.single-contract-column-header{
    font-size: 12px;
}
.single-contract-column-value{
    font-size: 15px;
    font-weight: bold;
}
.single-contract-label-column{
    padding-right: 0!important;
    padding-left: 0!important;
}
.label-info{
    border: 1px solid #eee;
    text-align: center;
    background: #f4f9ff;
}
.label-text{
    border: 1px solid #eee;
    text-align: center;
}
@media (max-width: 1200px) {
.single-contract-image{
    margin-left: auto;
    margin-right: auto;
    display: block;
}
.single-contract-name-duration{
    text-align: center;
}
}
@media (max-width: 992px) {
.single-contract-column-header, .single-contract-column-value{
    text-align: center;
}
.single-contract-sm-last{
    border-right: none;
}
}
@media (max-width: 575px) {
    .single-contract-label-column{
        width: 50%!important;
    }
}
</style>