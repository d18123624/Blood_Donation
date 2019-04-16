<template>
  <div class="container">
    <div class="row">
      <div class="rounded-corners-card-panel center padding-16 margin-16 relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Search</span>
        <div class="row valign-wrapper zero-padding zero-margin-bottom margin-top-16">
          <div class="input-field col s4 m4 l5">
            <input id="latitude" type="number" step="any" v-model="location.lat" class="active">
            <label for="latitude">Latitude</label>
            <span
              v-if="laterror != ''"
              class="left left-align red-text font-size-little"
            >{{ laterror }}</span>
          </div>
          <div class="input-field col s4 m4 l5">
            <input id="longitude" type="number" step="any" v-model="location.lng" class="active">
            <label for="longitude">Longitude</label>
            <span
              v-if="lngerror != ''"
              class="left left-align red-text font-size-little"
            >{{ lngerror }}</span>
          </div>
          <div class="col s4 m4 l2">
            <a
              class="right white-text waves-effect btn-flat teal no-uppercase font-size-small form-btn"
              v-on:click="toggleLocationPickerVisibility"
            >{{ locationPickerButtonText }}</a>
          </div>
        </div>
        <div class="row zero-padding zero-margin">
          <div v-if="isPickLocationVisible" class="col s12">
            <location-picker v-model="location"/>
          </div>
        </div>
        <div class="row zero-padding zero-margin">
          <div class="input-field col s6">
            <input
              id="searchmaxdistancemetres"
              type="number"
              v-model="searchmaxdistancemetres"
              class="active"
            >
            <label for="searchmaxdistancemetres">Search distance (in m)</label>
            <span
              v-if="distanceerror != ''"
              class="left left-align red-text font-size-little"
            >{{ distanceerror }}</span>
          </div>
          <div class="input-field col s6">
            <select v-model="patientbloodgroup">
              <option value disabled selected>Choose your blood group</option>
              <option value="A+">A+</option>
              <option value="A-">A-</option>
              <option value="B+">B+</option>
              <option value="B-">B-</option>
              <option value="AB+">AB+</option>
              <option value="AB-">AB-</option>
              <option value="O+">O+</option>
              <option value="O-">O-</option>
            </select>
            <label>Patient blood group</label>
            <span
              v-if="bloodgrouperror != ''"
              class="left left-align red-text font-size-little"
            >{{ bloodgrouperror }}</span>
          </div>
        </div>
        <div class="row zero-padding zero-margin">
          <a v-on:click="search" class="btn-floating btn-large waves-effect waves-light">
            <i class="material-icons">search</i>
          </a>
        </div>
      </div>
    </div>
    <div class="row" v-if="searchResults.length != 0">
      <div class="row center">
        <span class="font-size-large">Search Results ({{ searchCount }} results)</span>
      </div>
      <SearchResult v-for="result in searchResults" :key="result.id" :result="result" where="0"/>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { LocationPicker } from "vue2-location-picker";
import SearchResult from "./SearchResult.vue";

export default {
  name: "Search",
  methods: {},
  created: function() {
    M.AutoInit();
  },
  data() {
    return {
      location: {
        lat: 53.35014,
        lng: -6.266155
      },
      searchmaxdistancemetres: 6000,
      patientbloodgroup: "",
      isPickLocationVisible: false,
      locationPickerButtonText: "Pick",
      loading: false,
      searchResults: [],
      laterror: "",
      lngerror: "",
      distanceerror: "",
      bloodgrouperror: "",
      searchCount: 0
    };
  },
  components: {
    LocationPicker,
    SearchResult
  },
  computed: {
    loginLogoutText() {
      if (localStorage.getItem("token")) {
        return "Logout";
      } else {
        return "Login";
      }
    }
  },
  methods: {
    toggleLocationPickerVisibility() {
      this.isPickLocationVisible = !this.isPickLocationVisible;
      if (this.isPickLocationVisible) {
        this.locationPickerButtonText = "Hide";
      } else {
        this.locationPickerButtonText = "Pick";
      }
    },
    search() {
      var error = false;
      if (this.location.lat == "") {
        this.laterror = "Latitude cannot be empty!";
        error = true;
      }
      if (this.location.lng == "") {
        this.lngerror = "Longitude cannot be empty!";
        error = true;
      }
      if (this.searchmaxdistancemetres == "") {
        this.distanceerror = "Distance cannot be empty!";
        error = true;
      }
      if (this.patientbloodgroup == "") {
        this.bloodgrouperror = "Select blood group!";
        error = true;
      }
      if (error) {
        return;
      }
      this.loading = true;
      var payload = {
        search_lat: this.location.lat,
        search_long: this.location.lng,
        search_max_distance_metres: this.searchmaxdistancemetres,
        blood_group_patient: this.patientbloodgroup
      };
      this.$store.dispatch("search", payload).then(response => {
        if (response.error) {
          this.distanceerror = response.error_message;
        } else {
          this.searchResults = response.person_matches;
          this.searchResults.sort(function(a, b) {
            return (
              parseFloat(a.distance_in_metres) -
              parseFloat(b.distance_in_metres)
            );
          });
          this.searchResults = this.searchResults.slice(0, 10);
          this.searchCount = response.no_of_matches;
        }
        this.loading = false;
      });
    }
  },
  mounted() {
    M.AutoInit();
    M.updateTextFields();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.zero-padding {
  padding: 0 !important;
}

.zero-margin {
  margin: 0 !important;
}

.zero-margin-bottom {
  margin-bottom: 0 !important;
}

.relative {
  position: relative;
}

.preloader-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  width: 100%;
  height: 4px;
}
</style>
