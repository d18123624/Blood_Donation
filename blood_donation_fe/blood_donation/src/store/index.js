import Vue from 'vue';
import Vuex from 'vuex';

import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        baseURL: 'http://blooddonorbackend.ddns.net:8000',
        isloggedIn: false
    },
    mutations,
    actions: actions()
})