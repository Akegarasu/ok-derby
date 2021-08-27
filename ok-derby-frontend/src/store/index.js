import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    log: ""
  },
  mutations: {
    addLog(state, logStr) {
      state.log += logStr
    },
    clearLog(state) {
      state.log = ""
    }
  }
})

export default store