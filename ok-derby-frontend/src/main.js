/*!

=========================================================
* Vue Argon Dashboard - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import "@/assets/scss/index.scss";

import Vue from 'vue'
import VTooltip from 'v-tooltip'
import App from './App.vue'
import store from './store'
import router from './router'
import './registerServiceWorker'
import ArgonDashboard from './plugins/argon-dashboard'


Vue.config.productionTip = false
Vue.use(VTooltip)
Vue.use(ArgonDashboard)
router.beforeEach((to, from, next) => {
  document.title = to.meta.title ? to.meta.title + ' - 轻松养马' : '轻松养马'
  next()
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
