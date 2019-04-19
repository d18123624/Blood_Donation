<template>
  <div class="container relative search-component-wrapper">
    <div v-if="loading" class="progress preloader-wrapper">
      <div class="indeterminate"></div>
    </div>
    <div v-if="isLoadedOneTime" class="row center">
      <span
        v-if="previousSearchCount != 0"
        class="font-size-large"
      >Previous Searches ({{ previousSearchCount }} searches)</span>
      <span v-else class="font-size-large">No previous searches</span>
    </div>
    <div class="row zero-margin zero-padding previous-searches" v-if="previousSearches.length != 0">
      <PreviousSearch
        v-for="(result, index) in previousSearches"
        :key="index"
        :result="result"
        class="pointer"
        v-on:click.native="showSearchResults(index)"
      />
    </div>
    <div class="row" v-if="searchResults.length != 0">
      <div class="row center">
        <span class="font-size-large">Search Results ({{ searchCount }} results)</span>
      </div>
      <SearchResult v-for="result in searchResults" :key="result.id" :result="result"/>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { LocationPicker } from "vue2-location-picker";
import SearchResult from "./SearchResult.vue";
import PreviousSearch from "./PreviousSearch.vue";

export default {
  name: "PreviousSearches",
  methods: {},
  created: function() {
    M.AutoInit();
  },
  data() {
    return {
      loading: false,
      previousSearches: [],
      previousSearchCount: 0,
      searchResults: [],
      searchCount: 0,
      isLoadedOneTime: false
    };
  },
  components: {
    SearchResult,
    PreviousSearch
  },
  methods: {
    showSearchResults: function(index) {
      this.searchResults = this.previousSearches[index].person_matches;
      this.searchResults.sort(function(a, b) {
        return (
          parseFloat(a.distance_in_metres) - parseFloat(b.distance_in_metres)
        );
      });
      this.searchResults = this.searchResults.slice(0, 10);
      this.searchCount = this.previousSearches[index].no_of_matches;

      var newPoints = [];
      newPoints.push({
        position: {
          lat: parseFloat(this.previousSearches[index].search_lat),
          lng: parseFloat(this.previousSearches[index].search_long)
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
      if (newPoints.length > 0) {
        this.$store.commit("setMapCenter", {
          mapCenter: {
            lat: newPoints[0].position.lat,
            lng: newPoints[0].position.lng
          }
        });
      }
    }
  },
  mounted() {
    this.$store.commit("setSearchMarkers", {
      newPoints: []
    });
    this.loading = true;
    this.$store.dispatch("getPreviousSearches").then(response => {
      this.previousSearches = response;
      this.previousSearchCount = response.length;
      this.loading = false;
      this.isLoadedOneTime = true;
    });
    M.AutoInit();
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

.previous-searches {
  max-height: 250px;
  overflow: auto;
  border-width: 1px;
  border-color: #00000040;
  border-style: solid;
}

.pointer {
  cursor: pointer;
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
</style>
