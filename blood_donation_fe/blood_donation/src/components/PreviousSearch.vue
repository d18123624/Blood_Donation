<template>
  <div class="col s12">
    <div class="card padding-16 margin-4">
      <div class="row zero-margin zero-padding">
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ bloodgroup }}</span>
        </div>
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ distance }}</span>
        </div>
      </div>
      <div class="row zero-margin zero-padding">
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ latitude }}</span>
        </div>
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ longitude }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "PreviousSearch",
  created: function() {
    M.AutoInit();
  },
  props: ["result"],
  computed: {
    bloodgroup() {
      return "Patient blood group: " + this.result.blood_group_patient;
    },
    distance() {
      return "Distance (metres): " + this.result.search_max_distance_metres;
    },
    latitude() {
      return "Latitude: " + this.result.search_lat;
    },
    longitude() {
      return "Longitude: " + this.result.search_long;
    }
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

.col {
  margin: 0 !important;
  padding: 0 !important;
}
</style>
