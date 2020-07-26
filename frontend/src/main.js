import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
Vue.prototype.$apiURI = "http://18.191.43.124:8000"
Vue.prototype.$rapidKey = "57c7a0bfecmsh6bd72873440fb7ep1be0bfjsned54b9a32281"

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
