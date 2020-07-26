<template>
    <div class="main-div"  style="background-color: #f5f5f5">
        <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">Mining Companies</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!----------------------------------------------------------------------------------->
      <bounce :loading="isLoading" v-if="isLoading"></bounce>
      <div v-for="comp in companies" :key="comp.id" style="margin-top:0.75rem;">
        <div class="card mb-3" style="margin:0 auto;">
          <div class="row no-gutters align-items-center">
            <div class="col-sm-12 col-md-12 col-lg-2">
              <img v-bind:src="comp.image" class="card-img img-responsive" alt="...">
            </div>
            <div class="col-sm-12 col-md-12 col-lg-10 pl-3">
              <div class="card-body">

                <div class="row header-row">
                  <div class="col-sm-12 col-md-12 col-lg-3 inside-card-block last-in-small">
                      <h5 class="card-title"><a :href="`company/${comp.id}`">{{comp.title}}</a></h5>
                  </div>

                  <div class="col-sm-6 col-md-6 col-lg-3 inside-card-block">
                      <div class="card-text-header">Location: </div>
                      <div class="card-text">{{comp.location}}</div>
                  </div>

                  <div class="col-sm-6 col-md-6 col-lg-3 inside-card-block last-in-small">
                    <div class="card-text-header">Contracts:</div>
                    <div class="card-text">{{comp.num_of_contracts}}</div>
                  </div>
                  <div id="founded-block" class="col-sm-6 col-md-6 col-lg-2 inside-card-block">
                    <div class="card-text-header">Founded:</div>
                    <div class="card-text">{{comp.founded}}</div>
                  </div>
                  <div class="col-sm-6 col-md-6 col-lg-3 inside-card-block last-in-small" style="border-right:none;">
                    <div class="card-text-header">Credibility</div>
                          <div class="card-text">
                              <img v-if="comp.legitimacy === 'Checked'" src="/img/trust.png" :title="`${comp.legitimacy}`"/>
                              <img v-else-if="comp.legitimacy === 'Questionable'" src="/img/questionable.png" :title="`${comp.legitimacy}`"/>
                              <img v-else src="/img/avoid.png" :title="`${comp.legitimacy}`"/>
                          </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
            <div class="company-description">
              {{comp.description.substring(0,350)+"..."}}
            </div>
        </div>
       </div>
        <!----------------------------------------------------------------------------------->
    </div>
</template>

<script>
    import Vue from 'vue'
    import axios from 'axios';
    import VueSpinners from 'vue-spinners'
    Vue.use(VueSpinners)

    export default {
        name: "CompanyList",
        data() {
            return {
                companies: [],
                errors: [],
                isLoading: true,
            }
        },

        // Fetches posts when the component is created.
        created() {
            axios.get(process.env.VUE_APP_DATA_URL+`/api/companies/`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.companies = response.data
                    this.isLoading=false
                })
                .catch(e => {
                    this.errors.push(e)
                })
        }
    }
</script>

<style scoped>
.card{
	width:60%;
	height:auto;
}

.card-img{
  /*margin-left: auto;
  margin-right: auto;*/
  display: block;
    max-width: 150px;
    text-align: center;
}

.card:hover{
	/*border-color: #f4fc03;*/
	border-width: 1.5px;
	box-shadow: 5px 5px #dedede;
}

.card-title{
	color: #3c3ecf;
	font-size: 1.5rem;
	font-family: "Arial Black", Gadget, sans-serif;
    text-align: center;
}

.card-text-header{
	font-size: 0.8rem;
    text-align: center;
}

.card-text{
	font-weight: 700;
	font-size:16px;
	text-align: center;
}

.inside-card-block{
	border-right: 1px solid #dedede;
}

.header-row{
	width:100%;
	position: absolute;
	top: 50%;
	-ms-transform: translateY(-50%);
	transform: translateY(-50%);
}

.company-description{
	margin: 0.5rem;
}

#founded-block{
    display: none;
}

@media (max-width: 992px) {
    .card-body {
        min-height: 200px;
    }

    .inside-card-block{
        margin-top: 0.75rem;
    }

    .last-in-small{
        border-right:none;
    }
    .card-img{
      margin-left: auto;
      margin-right: auto;
    }
    #founded-block{
        display: block;
    }
}

@media (max-width: 578px) {
    .card-body {
        min-height: 270px;
    }

    .inside-card-block{
        border-right:none;
    }
}
</style>