import Vue from 'vue'
import Router from 'vue-router'
import DashboardLayout from '@/layout/DashboardLayout'
Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: 'main',
      component: DashboardLayout,
      children: [
        {
          path: '/main',
          name: '主页',
          meta: {
            title: '主页'
          },
          component: () => import(/* webpackChunkName: "demo" */ './views/MainPage.vue')
        },
        {
          path: '/settings',
          name: '设置',
          meta: {
            title: '设置'
          },
          component: () => import(/* webpackChunkName: "demo" */ './views/Settings.vue')
        },
      ]
    }
  ]
})
