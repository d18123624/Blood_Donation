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
      response.message = "Error!";
      response.error = true;
    })
    return response
  },
  async search({ state }, payload) {
    var response = []
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
      response = result.body.person_matches
    }).catch(function (error) {
      response = []
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
          Authorization: 'Token ' + '64466136b534cc310dc7598ed8855dc189638329' //localStorage.getItem('token')
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
  }
})