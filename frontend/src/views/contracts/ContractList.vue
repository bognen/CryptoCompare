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
        <div class="container" style="margin: 25px auto 0; width:55%; background-color: white">
            <div class="row">
                <div class="col-lg-2 col-md-12 image-column"><img class="image-icon" src="/img/companies/iqmining.png" /></div>
                <div class="col-lg-10 col-md-12 main-column">
                    <div class="on-top-column"><a href="/contract"><span class="contract-name">IMG-2910 Cloud Mining Contract</span></a>&nbsp;&nbsp;&nbsp;
                         <span class="contract-duration">60 Months</span></div>
                    <div class="row">
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                            <div class="column-header">Price:</div>
                            <div class="column-value">$ 210</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                            <div class="column-header">Hash Rate:</div>
                            <div class="column-value">1,000.0 GH/s</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block">
                            <div class="column-header">Mines:</div>
                            <div class="column-value">Bitcoin</div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6 column-block last-block">
                            <div class="column-header">Company:</div>
                            <div class="column-value">IQ Mining</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ContractList"
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
}

@media (max-width: 578px) {

    .column-block{
        text-align:center;
        width: 50%!important;
    }
}
</style>