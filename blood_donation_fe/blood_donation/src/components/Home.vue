<template>
  <div class="row">
    <div class="col s12 m6 relative">
      <div class="search-location-wrapper">
        <div class="search-location z-depth-1">
          <GmapAutocomplete @place_changed="setPlace"></GmapAutocomplete>
        </div>
      </div>
      <GmapMap :center="center" :zoom="10" :options="options" class="gmap-wrapper">
        <GmapMarker
          :key="index"
          v-for="(m, index) in markers"
          :position="m.position"
          :draggable="false"
          :icon="getMarkerIcon(index)"
        />
      </GmapMap>
    </div>
    <div class="col s12 m6">
      <router-view/>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
const pinMarker = require("../assets/pin.svg");
const bloodMarker = require("../assets/blood-drop.svg");

export default {
  name: "Home",
  computed: {
    markers() {
      return this.$store.state.searchMarkers;
    },
    center() {
      return this.$store.state.mapCenter;
    }
  },
  methods: {
    getMarkerIcon(index) {
      if (this.$store.state.isIncomingRequestsOpen) {
        return {
          url: bloodMarker,
          size: { width: 45, height: 45, f: "px", b: "px" },
          scaledSize: { width: 45, height: 45, f: "px", b: "px" }
        };
      }
      if (index == 0) {
        return {
          url: pinMarker,
          size: { width: 45, height: 45, f: "px", b: "px" },
          scaledSize: { width: 45, height: 45, f: "px", b: "px" }
        };
      } else {
        return {
          url: bloodMarker,
          size: { width: 45, height: 45, f: "px", b: "px" },
          scaledSize: { width: 45, height: 45, f: "px", b: "px" }
        };
      }
    },
    setPlace(place) {
      if (place) {
        this.$store.commit("setSearchMarkers", {
          newPoints: [
            {
              position: {
                lat: place.geometry.location.lat(),
                lng: place.geometry.location.lng()
              }
            }
          ]
        });
        this.$store.commit("setMapCenter", {
          mapCenter: {
            lat: place.geometry.location.lat(),
            lng: place.geometry.location.lng()
          }
        });
      }
    }
  },
  created: function() {
    try {
      M.AutoInit();
    } catch {}
  },
  data() {
    return {
      options: {
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
        disableDefaultUi: false
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.row,
.col {
  padding: 0 !important;
  margin: 0 !important;
}

.relative {
  position: relative;
}

.search-location-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 200;
  padding: 16px;
}

.search-location {
  border-radius: 24px;
  background-color: white;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 16px;
  padding-right: 16px;
  max-height: 45px;
  min-height: 45px;
  height: 45px;
  overflow: hidden;
}

@media only screen and (min-width: 601px) {
  /*tablet*/
  .search-location {
    max-height: 45px;
    min-height: 45px;
    height: 45px;
  }
}

@media only screen and (min-width: 993px) {
  /*laptop*/
  .search-location {
    max-height: 49px;
    min-height: 49px;
    height: 49px;
  }
}

.gmap-wrapper {
  width: 100%;
  height: calc(40vh - 32px);
}

@media only screen and (min-width: 601px) {
  /*tablet and laptop*/
  .gmap-wrapper {
    height: calc(100vh - 64px);
  }
}
</style>
