import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CompanyList from '../views/companies/CompanyList.vue'
import Company from '../views/companies/Company.vue'
import CoinList from '../views/coins/CoinList.vue'
import ContractList from "../views/contracts/ContractList";
import Contract from "../views/contracts/Contract";
import addContractList from "../views/admin/addContractList";
import addContract from "../views/admin/addContract";

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/companies',
    name: 'CompanyList',
    component: CompanyList
  },
  {
    path: '/company/:id',
    name: 'Company',
    component: Company
  },
 {
    path: '/coins',
    name: 'CoinList',
    component: CoinList
  },
  {
    path: '/contracts',
    name: 'ContractList',
    component: ContractList
  },
 {
    path: '/contract/:id',
    name: 'Contract',
    component: Contract
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },

 {
    path: '/admin/contracts',
    name: 'addContractList',
    component: addContractList
  },

 {
    path: '/admin/contract/:id?',
    name: 'addContract',
    component: addContract
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
