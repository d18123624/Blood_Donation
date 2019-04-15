<template>
  <div class="container">
    <div class="row margin-top-16">
      <div class="col s6 m4 margin-bottom-16">
        <router-link to="/search">
          <div class="rounded-corners-card-panel padding-32 red darken-3 center height-300px valign-wrapper">
            <span class="white-text font-size-large full-width">Search</span>
          </div>
        </router-link>
      </div>
      <div v-if="this.$store.state.isloggedIn" class="col s6 m4 margin-bottom-16">
        <router-link to="/previoussearches">
          <div class="rounded-corners-card-panel padding-32 blue darken-3 center height-300px valign-wrapper">
            <span class="white-text font-size-large full-width">Previous searches</span>
          </div>
        </router-link>
      </div>
      <div v-if="this.$store.state.isloggedIn" class="col s6 m4 margin-bottom-16">
        <router-link to="/incomingrequests">
          <div class="rounded-corners-card-panel padding-32 amber darken-3 center height-300px valign-wrapper">
            <span class="white-text font-size-large full-width">Incoming blood donation requests</span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Home",
  methods: {},
  created: function() {
    M.AutoInit();
  },
  data() {
    return {};
  },
  computed: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.rounded-corners-card-panel {
  border-width: 0;
}

.height-300px {
  height: 150px;
}

.full-width {
  width: 100%;
}
</style>
