import Vue from 'vue';
import Vuex from 'vuex';

import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        baseURL: 'http://blooddonorbackend.ddns.net:8000',
        isloggedIn: false,
        isIncomingRequestsOpen: false,
        searchMarkers: [
            {
                position: {
                    lat: 53.35014,
                    lng: -6.266155
                }
            }
        ],
        mapCenter: {
            lat: 53.35014,
            lng: -6.266155
        },
        resetSearch: false   
    },
    mutations,
    actions: actions()
})