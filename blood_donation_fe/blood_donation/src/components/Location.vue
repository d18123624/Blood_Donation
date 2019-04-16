<template>
  <location-picker v-model="location"/>
</template>

<script>
/* eslint-disable */
import { LocationPicker } from "vue2-location-picker";

export default {
  name: "Location",
  created() {
    var url = window.location;
    var splittedUrl = url.toString().split("/");
    this.location.lat = parseFloat(splittedUrl[splittedUrl.length - 2]);
    this.location.lng = parseFloat(splittedUrl[splittedUrl.length - 1]);
  },
  components: {
    LocationPicker
  },
  data() {
    return {
      location: {
        lat: 0,
        lng: 0
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
