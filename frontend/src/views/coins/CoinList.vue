<template>
    <div class="main-div"  style="background-color: #f5f5f5">
        <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">Coins</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!----------------------------------------------------------------------------------->
        <div class="container" style="margin: 25px auto 0; width:75%; background-color: white">
            <div class="row">
                <div class="col-sm-1 col-lg-2 coins-board">
                    <tr v-for="(c, index) in coins" :key="c.id"  @click='show = c.id, activeDiv=index++' class="btn coin"
                         v-bind:style="{'background-color':backgroudColor[index]}">
                        <td><img v-bind:src="c.image" style="max-width: 25px"/></td>
                        <td class="pl-2">
                            <div class="coin-name"><span >{{c.name}}</span></div>
                            <div class="coin-token"><span>{{c.token}}</span></div>
                        </td>
                    </tr>
                </div>
                <div class="col-sm-11 col-lg-10">
                    <div  v-show="show === c.id" v-for="c in coins" :key="c.id" class="row coin-row">
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Start Day</div>
                            <div class="coin-table-cell">{{c.start_date}}</div>
                        </div>
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Algorithm</div>
                            <div class="coin-table-cell">{{c.algorithm}}</div>
                        </div>
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Max Supply</div>
                            <div class="coin-table-cell">{{c.max_supply}}</div>
                        </div>
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Current Supply</div>
                            <div class="coin-table-cell">{{c.currentSupply | formatNumber}}</div>
                        </div>
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Website</div>
                            <div class="coin-table-cell"><a v-bind:href="`${c.website}`">{{c.name}}</a></div>
                        </div>
                        <div class="col-sm-4 col-md-2 col-lg-2 coin-table">
                            <div class="coin-table-cell-head">Current Price</div>
                            <div class="coin-table-cell" style="color:#1c7430; font-weight:bold">${{c.currentPrice}}</div>
                        </div>
                        <!--------------------------------------------------------------------------------------------->
                        <div class="coin-description mt-3">{{c.description}}</div>
                        <!--------------------------------------------------------------------------------------------->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue'
    import axios from 'axios';
    let numeral = require("numeral");

    let coinInfo = process.env.VUE_APP_DATA_URL+'/api/coins/';
    let coinPrice = 'https://api.coingecko.com/api/v3/simple/price';
    let coinSupply = 'https://api.coingecko.com/api/v3/coins/markets';
    let coinParams = 'https://mineable-coins.p.rapidapi.com/coins?list=BTC,BCH,LTC,ETH,DASH,ZEC,XMR,BSV,XRP';

    const coinInfoRequest = axios.get(coinInfo);
    const coinPriceRequest = axios.get(coinPrice, {
        params: {
            ids: 'bitcoin,bitcoin-cash,litecoin,ethereum,dash,zcash,monero,bitcoin-cash-sv,ripple',
            vs_currencies: 'usd'
        }
    });
    const coinSupplyRequest = axios.get(coinSupply, {
        params: {
            vs_currency: 'usd',
            ids: 'bitcoin,bitcoin-cash,litecoin,ethereum,dash,zcash,monero,bitcoin-cash-sv,ripple'
        }
    });
    const coinParamsRequest = axios.get(coinParams, {
        "method": "GET",
        "headers": {
            "x-rapidapi-host": "mineable-coins.p.rapidapi.com",
            "x-rapidapi-key": process.env.VUE_APP_RAPID_KEY
        }
    });

    // Number formatter
    Vue.filter("formatNumber", function (value) {
        return numeral(value).format("0,0");
      });

    export default {
        name: "CoinList",
        data() {
            return {
                coins: [],
                errors: [],
                show: null,
                activeDiv: 0
            }
        },

        // Fetches posts when the component is created.
        created() {
            axios.all([coinInfoRequest, coinPriceRequest,coinSupplyRequest, coinParamsRequest]).then(axios.spread((...responses) => {
                this.coins = this.processResponse(responses[0].data, responses[1].data, responses[2].data);
                //console.log(this.coins[0].id)
                this.show = this.coins[0].id;
                console.log(responses[3].data)
            })).catch(errors => {
                console.log(errors);
            })
        },
        computed: {
            backgroudColor: function(){
                let len = this.coins.length;
                let result =[];
                for (let i = 0; i<len; i++){
                    if (this.activeDiv == i){
                      result.push('#FFF');
                    } else {
                      result.push('#dedede');
                    }
                  }

                  return result;
            }
        },
        methods:{
            // Method ads current price and current supply
            processResponse(general, prices, supply){
                //let response = []
                for(let i=0; i< general.length; i++){
                    // Add Current Price
                    general[i].currentPrice = prices[general[i].coinGecko].usd;

                    // Filter the whole supply array to get correct element
                    let marketObj = supply.filter(obj => {
                          return obj.id === general[i].coinGecko;
                        });
                    // add circulating supply to the response as Current Supply
                    general[i].currentSupply = marketObj[0].circulating_supply;
                }
                return general;
            }
        }
    }
</script>

<style scoped>
.coin{
    text-align: left;
    margin: 0 auto;
    width: 100%;
    border-radius: 0!important;
    color: #000;
}
.coin-name{
    font-weight: bold;
    font-size: 15px;
    margin-bottom: -3px;
}
.coin-token{
    color: #7a7a7a;
    font-size: 13px;
}
.coins-board{
    padding-left: 0!important;
    padding-right: 0!important;
}
.coin-row{
    margin: 0.5rem;
}

.coin-table{
    border: 1px solid #EEE;
    font-size: 12px;
    text-align: center;
    padding-left: 0!important;
    padding-right: 0!important;
}
.coin-table-cell-head{
    font-weight: bold;
    font-size: 14px;
    border-bottom: 1px solid #EEE;
    min-height: 46px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.coin-table-cell{
    font-size: 14px;
}

.coin-description{
    color: #000;
    text-align: justify;
    font-family: "Gill Sans", sans-serif;
}
@media (max-width: 1150px) and (min-width: 580px) {
    .coin-name {
        display: none;
    }
}

@media (max-width: 990px) and (min-width: 580px) {
    .coin-token {
        display: none;
    }
}


</style>