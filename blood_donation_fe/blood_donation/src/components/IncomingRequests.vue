<template>
  <div class="container">
    <div class="row">
      <div class="rounded-corners-card-panel center padding-16 margin-16 relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Incoming Requests</span>
      </div>
    </div>
    <div class="row" v-if="searchResults.length != 0">
      <div class="row center">
        <span class="font-size-large">Search Results</span>
      </div>
      <SearchResult v-for="result in searchResults" :key="result.id" :result="result" where="1" />
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
    this.loading = true;
    this.$store.dispatch("getReceivedRequests").then(response => {
      this.searchResults = response;
      this.loading = false;
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
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  width: 100%;
  height: 4px;
}
</style>
