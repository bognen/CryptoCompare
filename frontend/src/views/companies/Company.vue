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
              <div class="card mb-3" style="margin: 0 auto;">
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
                              <div class="col-sm-4 inside-card-block">
                                  <div class="card-text-header"><i class="fa fa-money fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Coins</div>
                                  <div class="card-text">Bitcoin</div>
                              </div>
                          </div>

                          <div class="row" style="margin-top: 1rem">
                              <div class="col-sm-4 inside-card-block">
                                <div class="card-text-header"><i class="fa fa-briefcase fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Contracts:</div>
                                <div class="card-text">17</div>
                              </div>
                              <div class="col-sm-4">
                                <div class="card-text-header"><i class="fa fa-calendar fa-lg marker-icons" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;Founded:</div>
                                <div class="card-text">{{company.founded}}</div>
                              </div>
                              <div class="col-sm-4 inside-card-block last-in-small" style="border-right:none;">
                                <div class="card-text-header">Reliability</div>
                                      <div class="card-text">
                                        <!--img :src="`${company.legPicture}`" :alt="`${company.legitimacy}`"/ -->
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
              </div>
            </div>
       </div>
        <!----------------------------------------------------------------------------------->
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Company",
        data() {
            return {
                company: '',
                legPicture: '',
                errors: []
            }
        },

        // Fetches posts when the component is created.
        created() {
            axios.get(`http://localhost:8000/api/company/`+this.$route.params.id)
                .then(response => {
                    this.company =  response.data
                    //legPicture = this.getLegitimacyPic(response.data.legitimacy)
                })
                .catch(e => {
                    this.errors.push(e)
                })
        }
    }
</script>

<style>
    .card{
	width:65%;
	height:auto;
	border: none!important;
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

    .card-body{

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
</style>