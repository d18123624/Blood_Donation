<template>
  <div class="container relative requests-component-wrapper">
    <div v-if="loading" class="progress preloader-wrapper">
      <div class="indeterminate"></div>
    </div>
    <div class="row center">
      <br>
      <span class="font-size-large">Incoming Requests</span>
    </div>
    <div class="row" v-if="searchResults.length != 0">
      <SearchResult v-for="result in searchResults" :key="result.id" :result="result" where="1"/>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import SearchResult from "./SearchResult.vue";

export default {
  name: "IncomingRequests",
  methods: {},
  created: function() {
    M.AutoInit();
  },
  data() {
    return {
      loading: false,
      searchResults: []
    };
  },
  components: {
    SearchResult
  },
  methods: {},
  mounted() {
    this.$store.commit("setSearchMarkers", { newPoints: [] });
    this.loading = true;
    this.$store.dispatch("getReceivedRequests").then(response => {
      this.searchResults = response;
      var newPoints = [];
      this.searchResults.forEach(function(obj) {
        newPoints.push({
          position: {
            lat: parseFloat(obj.address_lat),
            lng: parseFloat(obj.address_long)
          }
        });
      });
      this.loading = false;
      this.$store.commit("setSearchMarkers", { newPoints: newPoints });
      if (newPoints.length > 0) {
        this.$store.commit("setMapCenter", {
          mapCenter: {
            lat: newPoints[0].position.lat,
            lng: newPoints[0].position.lng
          }
        });
      }
    });
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.$store.commit("setIsIncomingRequestsOpen", true);
    });
  },
  beforeRouteLeave(to, from, next) {
    next();
    this.$store.commit("setIsIncomingRequestsOpen", false);
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

.requests-component-wrapper {
  width: 100%;
  height: calc(60vh - 32px);
}

@media only screen and (min-width: 601px) {
  /*tablet and laptop*/
  .requests-component-wrapper {
    height: calc(100vh - 64px);
  }
}
</style>
