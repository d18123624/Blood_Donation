<template>
  <div class="container relative search-component-wrapper">
    <div v-if="loading" class="progress preloader-wrapper">
      <div class="indeterminate"></div>
    </div>
    <div class="row zero-margin zero-padding">
      <div class="input-field col s5">
        <input
          id="searchmaxdistancemetres"
          type="number"
          v-model="searchmaxdistancemetres"
          class="active"
        >
        <label for="searchmaxdistancemetres">Search radius (m)</label>
        <span
          v-if="distanceerror != ''"
          class="left left-align red-text font-size-little"
        >{{ distanceerror }}</span>
      </div>
      <div class="input-field col s5">
        <select v-model="patientbloodgroup">
          <option value disabled selected>Choose</option>
          <option value="A+" selected>A+</option>
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
      <div class="col s2 center">
        <a v-on:click="search" class="btn-floating btn-large waves-effect waves-light">
          <i class="material-icons">search</i>
        </a>
      </div>
    </div>
    <div v-if="isLoadedOneTime" class="row center">
      <span
        v-if="searchCount != '0'"
        class="font-size-large"
      >Search Results ({{ searchCount }} results)</span>
      <span v-else class="font-size-large">No results</span>
    </div>
    <div class="row" v-if="searchResults.length != 0">
      <SearchResult v-for="result in searchResults" :key="result.id" :result="result" where="0"/>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import SearchResult from "./SearchResult.vue";
import { setTimeout } from "timers";

export default {
  name: "Search",
  data() {
    return {
      searchmaxdistancemetres: 6000,
      patientbloodgroup: "",
      loading: false,
      searchResults: [],
      distanceerror: "",
      bloodgrouperror: "",
      searchCount: 0,
      isLoadedOneTime: false
    };
  },
  components: {
    SearchResult
  },
  computed: {
    location() {
      return this.$store.state.searchMarkers[0].position;
    }
  },
  methods: {
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
      this.distanceerror = "";
      this.bloodgrouperror = "";
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

          var newPoints = [];
          newPoints.push({
            position: {
              lat: this.location.lat,
              lng: this.location.lng
            }
          });
          this.searchResults.forEach(function(obj) {
            var latitude;
            var longitude;
            try {
              longitude = parseFloat(obj.match_person.address_long);
            } catch {
              if (obj.longitude) {
                longitude = parseFloat(obj.longitude);
              } else {
                longitude = parseFloat(obj.address_long);
              }
            }
            try {
              latitude = parseFloat(obj.match_person.address_lat);
            } catch {
              if (obj.latitude) {
                latitude = parseFloat(obj.latitude);
              } else {
                latitude = parseFloat(obj.address_lat);
              }
            }
            newPoints.push({
              position: {
                lat: latitude,
                lng: longitude
              }
            });
          });
          this.$store.commit("setSearchMarkers", { newPoints: newPoints });
        }
        this.loading = false;
        this.isLoadedOneTime = true;
        setTimeout(() => {
          M.AutoInit();
          M.updateTextFields();
        }, 100);
      });
    }
  },
  mounted() {
    M.AutoInit();
    M.updateTextFields();
    var newPoints = [];
    newPoints.push({
      position: {
        lat: 53.35014,
        lng: -6.266155
      }
    });
    this.$store.commit("setSearchMarkers", { newPoints: newPoints });
    this.$store.commit("setMapCenter", { mapCenter: {
      lat: 53.35014,
        lng: -6.266155
    }});
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
  width: 100%;
  margin: 0 !important;
  padding: 0 !important;
  height: 4px;
}

.container {
  width: 100%;
  max-height: 100%;
  padding-left: 3.5%;
  padding-right: 3.5%;
  padding-top: 8px;
  padding-bottom: 8px;
  overflow-x: hidden;
  overflow-y: auto;
}

@media only screen and (min-width: 601px) {
  /*tablet*/
  .container {
    width: 100%;
    max-height: 100%;
    padding-left: 3.5%;
    padding-right: 3.5%;
    overflow-x: hidden;
    overflow-y: auto;
  }
}

@media only screen and (min-width: 993px) {
  /*laptop*/
  .container {
    width: 100%;
    max-height: 100%;
    padding-left: 3.5%;
    padding-right: 3.5%;
    overflow-x: hidden;
    overflow-y: auto;
  }
}

.full-height {
  height: 100%;
}

.search-component-wrapper {
  width: 100%;
  height: calc(60vh - 32px);
}

@media only screen and (min-width: 601px) {
  /*tablet and laptop*/
  .search-component-wrapper {
    height: calc(100vh - 64px);
  }
}
</style>
