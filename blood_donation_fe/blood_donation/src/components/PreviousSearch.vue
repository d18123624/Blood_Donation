<template>
  <div class="col s12">
    <div class="card padding-16 margin-4">
      <div class="row zero-margin zero-padding valign-wrapper">
        <div class="col s2 m2 l1 valign-wrapper">
          <div class="circle teal valign-wrapper left-align">
            <span class="font-size-large white-text">{{ bloodgroup }}</span>
          </div>
        </div>
        <div class="col s10 m10 l11">
          <span class="font-size-small">{{ distance }}</span><br>
          <span class="font-size-small">{{ latitude }}</span><br>
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
      return this.result.blood_group_patient;
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

.circle {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  text-align: center;
}

span {
  width: 100%;
}
</style>
