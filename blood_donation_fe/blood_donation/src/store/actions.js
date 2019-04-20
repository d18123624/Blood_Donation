/* eslint-disable */
import Vue from 'vue'

export default () => ({
  async login({ state, commit }, payload) {
    var response = {
      message: "",
      error: true
    }
    await Vue.http.post(
      state.baseURL + '/person/login/',
      payload,
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true
      }
    ).then((result) => {
      response.message = result.body.message;
      response.error = false;
      commit("setIsLoggedIn", {
        loggedin: true,
        token: result.body.token
      })
    }).catch(function (error) {
      response.message = error.body.non_field_errors[0];
      response.error = true;
      commit("setIsLoggedIn", {
        loggedin: false,
        token: null
      })
    })
    return response
  },
  async signup({ state, commit }, payload) {
    var response = {
      message: "",
      error: true,
      error_fields: []
    }
    await Vue.http.post(
      state.baseURL + '/person/signup/',
      payload,
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true
      }
    ).then((result) => {
      response.message = result.body.message;
      response.error = false;
      response.error_fields = [];
      commit("setIsLoggedIn", {
        loggedin: true,
        token: result.body.token
      })
    }).catch(function (error) {
      response.message = "Error!";
      response.error = true;
      response.error_fields = error.body.error_fields;
      commit("setIsLoggedIn", {
        loggedin: false,
        token: null
      })
    })
    return response
  },
  async logout({ state, commit }) {
    var response = {
      message: "",
      error: true
    }
    await Vue.http.get(
      state.baseURL + '/person/logout/',
      {
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      response.error = false;
      response.message = result.body.message;
      commit("setIsLoggedIn", {
        loggedin: false,
        token: null
      })
    }).catch(function (error) {
      response.message = "Already logged out!";
      response.error = true;
      commit("setIsLoggedIn", {
        loggedin: false,
        token: null
      })
    })
    commit("setReset")
    commit("setSearchMarkers", { newPoints: [] });
    return response
  },
  async search({ state }, payload) {
    var response = {
      person_matches: [],
      no_of_matches: 0,
      error_message: "",
      error: false
    }
    var headers = {}
    if (localStorage.getItem('token')) {
      headers = {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    }
    await Vue.http.post(
      state.baseURL + '/donation_requests/search/',
      payload,
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers
      }
    ).then((result) => {
      response.person_matches = result.body.person_matches
      response.no_of_matches = result.body.no_of_matches
      response.error = false
      response.error_message = ""
    }).catch(function (error) {
      response.person_matches = []
      response.error = true
      response.no_of_matches = 0
      response.error_message = error.body.search_max_distance_metres[0];
    })
    return response
  },
  async getPreviousSearches({ state }) {
    var response = []
    await Vue.http.get(
      state.baseURL + '/donation_requests/get_own_searches/',
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      response = result.body
    }).catch(function (error) {
      response = []
    })
    return response
  },
  async requestForBloodDonation({ state }, payload) {
    var response = ""
    await Vue.http.post(
      state.baseURL + '/donation_requests/request_for_donation/',
      payload,
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      response = "Request registered successfully!"
    }).catch(function (error) {
      response = "Error!"
    })
    return response
  },
  async getReceivedRequests({ state }) {
    var response = []
    await Vue.http.get(
      state.baseURL + '/donation_requests/received_requests_own/',
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      result.body.forEach(function (item) {
        response.push(item.person_donation_request);
      });
    }).catch(function (error) {
      response = []
    })
    return response
  },
  async deleteAccount({ state }) {
    var response = {
      error: false,
      message: ""
    }
    await Vue.http.delete(
      state.baseURL + '/person/delete/',
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      response.error = result.body.error;
      response.message = result.body.message;
    }).catch(function (error) {
      response.error = true;
      response.message = error.body.detail;
    })
    return response
  },
  async updateDetails({ state }, payload) {
    var response = {
      message: "",
      error: true,
      error_fields: []
    }
    await Vue.http.post(
      state.baseURL + '/person/update/',
      payload,
      {
        'Content-Type': 'application/x-www-form-urlencoded',
        emulateJSON: true,
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      }
    ).then((result) => {
      response.message = result.body.message;
      response.error = false;
      response.error_fields = [];
    }).catch(function (error) {
      response.message = error.body.message;
      response.error = true;
      response.error_fields = error.body.error_fields;
    })
    return response
  }
})