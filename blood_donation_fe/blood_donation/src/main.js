import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { store } from './store/index.js'
import VueResource from 'vue-resource'
import * as VueGoogleMaps from 'vue2-google-maps'

import './assets/css/utils.css'

Vue.config.productionTip = false

Vue.use(router)
Vue.use(VueResource)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyB2s22dOCpytjh2IT9Y7uCJOFw9NlXLIxM',
    libraries: 'places'
  },
  installComponents: true
})

new Vue({
  store: store,
  router: router,
  render: h => h(App)
}).$mount('#app')
