import Vue from 'vue'
import Vuex from 'vuex'
import api from "../service/api"
import { server } from "../service/constants"
import router from "../router"
 
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    headerCoreState: true,
    headerLoginState: false,
    headerInvoiceState: false,
    headerAdminState: false,
    loadingState: false,
    userid: "",
    customer: {},
    dialogState: false,
    dialogMessage: "",
    invoices: [],
    customerID: "",
  },
  getters: {
    getHeaderCoreState( state ){
      return state.headerCoreState
    },
    getHeaderLoginState( state ){
      return state.headerLoginState
    },
    getHeaderInvoiceState( state ){
      return state.headerInvoiceState
    },
    getHeaderAdminState( state ){
      return state.headerAdminState
    },
    getLoadingState( state ){
      return state.loadingState
    },
    getUserID( state ){
      return state.userid
    },
    getCustomer ( state ){
      return state.customer
    },
    getDialogState( state ){
      return state.dialogState
    },
    getDialogMessage( state ){
      return state.dialogMessage
    },
    getInvices( state ) {
      return state.invoices
    },
    getCustomerID( state ){
      return state.customerID
    }
  },
  mutations: {
    SET_HEADER_CORE_STATE( state, value ){
      state.headerCoreState = value
    },
    SET_HEADER_LOGIN_STATE( state, value ){
      state.headerLoginState = value
    },
    SET_HEADER_INVOICE_STATE( state, value ){
      state.headerInvoiceState = value
    },
    SET_HEADER_ADMIN_STATE( state, value ){
      state.headerAdminState = value
    },
    SET_LOADING_STATE( state, value ){
      state.loadingState = value
    },
    SET_USER_ID( state, value ){
      state.userid = value
    },
    SET_CUSTOMER( state, value ){
      state.customer = value
    },
    SET_DIALOG_STATE( state, value){
      state.dialogState = value
    },
    SET_DIALOG_MSG( state, value ){
      state.getDialogMessage = value
    },
    SET_INVOICES( state, value ){
      state.invoices = value
    },
    SET_CUSTOMER_ID( state, value ){
      state.customerID = value
    }
  },
  actions: {
    async doRegister ({ commit }, { firstname, familyname, email, phoneNumber, creditCardNumber, point, password }) {
      var result = await api.register({ firstname, familyname, email, phoneNumber, creditCardNumber, point, password })
      if  (result.status === "1") {
        commit("SET_CUSTOMER_ID", result.result)
      } else {
        commit("SET_DIALOG_STATE", true)
        commit("SET_DIALOG_MSG", result.msg)
      } 
    },
    async doLogin ({ commit }, { email, password }){
      if (email == "admin@new-hotel.com") {
        var result = await api.login({ email, password })
        if (result.status === "1") {
          localStorage.setItem(server.USERNAME, result.result)
          localStorage.setItem(server.USER_TYPE, "admin")
          commit("SET_USER_ID", result.result)
          commit("SET_HEADER_CORE_STATE", false)
          commit("SET_HEADER_LOGIN_STATE", false)
          commit("SET_HEADER_ADMIN_STATE", true)
          router.push({name: "HomeAdmin"})
        } else {
          commit("SET_HEADER_CORE_STATE", true)
          commit("SET_HEADER_LOGIN_STATE", false)
          commit("SET_HEADER_ADMIN_STATE", false)
          router.push({name: "Home"})
        }
      } else {
        var result = await api.login({ email, password })
        if (result.status === "1") {
          localStorage.setItem(server.USERNAME, result.result)
          localStorage.setItem(server.USER_TYPE, "customer")
          commit("SET_USER_ID", result.result)
          commit("SET_HEADER_CORE_STATE", false)
          commit("SET_HEADER_LOGIN_STATE", true)
          commit("SET_HEADER_ADMIN_STATE", false)
          router.push({name: "Home"})
        } else {
          commit("SET_HEADER_CORE_STATE", true)
          commit("SET_HEADER_LOGIN_STATE", false)
          commit("SET_HEADER_ADMIN_STATE", false)
          router.push({name: "Home"})
        }
      }
    },
    async restoreLogin ({ commit }){
      var userid = localStorage.getItem(server.USERNAME)
      if (userid !== null) {
        var result = localStorage.getItem(server.USER_TYPE)
        if (result === "admin") {
          commit("SET_USER_ID", userid)
          commit("SET_HEADER_CORE_STATE", false)
          commit("SET_HEADER_LOGIN_STATE", false)
          commit("SET_HEADER_ADMIN_STATE", true)
          router.push({name: "HomeAdmin"})
        } else {
          commit("SET_USER_ID", userid)
          commit("SET_HEADER_CORE_STATE", false)
          commit("SET_HEADER_LOGIN_STATE", true)
          commit("SET_HEADER_ADMIN_STATE", false)
        }
      } else {
        commit("SET_HEADER_CORE_STATE", true)
        commit("SET_HEADER_LOGIN_STATE", false)
        commit("SET_HEADER_ADMIN_STATE", false)
        router.push({name: "Home"})
      }
    },
    async doLogout ({ commit }){
      localStorage.removeItem(server.USERNAME)
      commit("SET_USER_ID", "")
      commit("SET_HEADER_CORE_STATE", true)
      commit("SET_HEADER_LOGIN_STATE", false)
      commit("SET_HEADER_ADMIN_STATE", false)
    }
  }
})
