import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { store } from './store/index.js'
import VueResource from 'vue-resource'

import './assets/css/utils.css'

Vue.config.productionTip = false

Vue.use(router)
Vue.use(VueResource);
//Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
//Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
//Vue.http.headers.common['Access-Control-Request-Method'] = '*'
new Vue({
  store: store,
  router: router,
  render: h => h(App)
}).$mount('#app')
