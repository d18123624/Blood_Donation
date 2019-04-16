<template>
  <div class="container">
    <div class="row">
      <div class="rounded-corners-card-panel center padding-16 margin-16 relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Previous Searches ({{ previousSearchCount }} searches)</span>
      </div>
    </div>
    <div class="row previous-searches-height" v-if="previousSearches.length != 0">
      <PreviousSearch
        v-for="(result, index) in previousSearches"
        :key="result.id"
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
      searchCount: 0
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
      this.searchCount = this.previousSearches[
        index
      ].no_of_matches;
    }
  },
  mounted() {
    this.loading = true;
    this.$store.dispatch("getPreviousSearches").then(response => {
      this.previousSearches = response;
      this.previousSearchCount = response.length;
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

.previous-searches-height {
  max-height: 250px;
  overflow: auto;
}

.pointer {
  cursor: pointer;
}
</style>
