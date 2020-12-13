import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    coreHeader: true,
    logoHeader: false,
    loginHeaderUser: false,
    loginHeaderAdmin: false,
  },
  getters: {
    getCoreHeader (state) {
      return state.coreHeader
    },
    getLogoHeader (state) {
      return state.logoHeader
    },
    getLoginHeaderUser (state) {
      return state.loginHeaderUser
    },
    getLoginHeaderAdmin (state) {
      return state.loginHeaderAdmin
    }
  },
  mutations: {
    SET_CORE_HEADER (state, value) {
      state.coreHeader = value
    },
    SET_LOGO_HEADER (state, value) {
      state.logoHeader = value
    },
    SET_LOGIN_HEADER_USER (state, value) {
      state.loginHeaderUser = value
    },
    SET_LOGIN_HEADER_ADMIN (state, value) {
      state.loginHeaderAdmin = value
    },
    SET_USERNAME (state, value) {
      state.username = value
    },
    SET_USER_TYPE (state, value) {
      state.userType = value
    },
  },
  actions: {
    restoreLogin ({ commit, dispatch }) {
      if (api.isLoggedIn() === true) {
        const userType = localStorage.getItem(server.USER_TYPE);
        const username = localStorage.getItem(server.USERNAME);
        if (userType === "User") {
          commit("SET_USERNAME", username);
          commit("SET_USER_TYPE", userType);
          commit("SET_CORE_HEADER", false)
          commit("SET_LOGO_HEADER", false)
          commit("SET_LOGIN_HEADER_USER", true)
          commit("SET_LOGIN_HEADER_ADMIN", false)
          commit("SET_STATE_LOGIN_DIALOG", true)
        } else if (userType === "Admin") {
          commit("SET_USERNAME", username);
          commit("SET_USER_TYPE", userType);
          commit("SET_CORE_HEADER", false)
          commit("SET_LOGO_HEADER", false)
          commit("SET_LOGIN_HEADER_USER", false)
          commit("SET_LOGIN_HEADER_ADMIN", true)
        }
      }
    },  
    doLogout ({ commit }) {
      api.logoff()
      commit("SET_USERNAME", null);
      commit("SET_CORE_HEADER", true)
      commit("SET_LOGO_HEADER", false)
      commit("SET_LOGIN_HEADER_USER", false)
      commit("SET_LOGIN_HEADER_ADMIN", false)
      router.push({ name: "Home" })
    },
    async doLogin ({ commit, dispatch }, { email, password }) {
      const result = await api.login({ email, password });
      if (result.status === "1") {
        const userType = localStorage.getItem(server.USER_TYPE);
        const username = localStorage.getItem(server.USERNAME);
        if (userType === "User") {
          commit("SET_USERNAME", username);
          commit("SET_USER_TYPE", userType);
          commit("SET_CORE_HEADER", false)
          commit("SET_LOGO_HEADER", false)
          commit("SET_LOGIN_HEADER_USER", true)
          commit("SET_LOGIN_HEADER_ADMIN", false)
          router.push({ name: "Home" })
          commit("SET_STATE_LOGIN_DIALOG", true)
          setInterval(() => {
            commit("SET_STATE_LOGIN_DIALOG", false)
          }, 3000);
        } else if (userType === "Admin") {
          commit("SET_USERNAME", username);
          commit("SET_USER_TYPE", userType);
          commit("SET_CORE_HEADER", false)
          commit("SET_LOGO_HEADER", false)
          commit("SET_LOGIN_HEADER_USER", false)
          commit("SET_LOGIN_HEADER_ADMIN", true)
          commit("SET_DIALOG_LOADING", false)
          router.push({ name: "HomeAdmin" })
        }
      } else {
        commit("SET_DIALOG_LOADING", false)
        dispatch({ type: "dialogPopup", value: true, msg: result.msg })
        commit("SET_USERNAME", null);
        commit("SET_CORE_HEADER", true)
        commit("SET_LOGIN_HEADER_USER", false)
        commit("SET_LOGIN_HEADER_ADMIN", false)
      }
    },
  },
  modules: {
  }
})
