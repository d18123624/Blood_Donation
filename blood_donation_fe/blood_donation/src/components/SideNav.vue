<template>
  <ul id="slide-out" class="sidenav">
    <li>
      <router-link to="/">
        <a class="black-text valign-wrapper">
          <i class="material-icons">search</i>&emsp;Search
        </a>
      </router-link>
    </li>
    <li v-if="this.$store.state.isloggedIn">
      <router-link to="/previoussearches">
        <a class="black-text valign-wrapper">
          <i class="material-icons">history</i>&emsp;Previous Searches
        </a>
      </router-link>
    </li>
    <li v-if="this.$store.state.isloggedIn">
      <router-link to="/incomingrequests">
        <a class="black-text valign-wrapper">
          <i class="material-icons">priority_high</i>&emsp;Incoming Requests
        </a>
      </router-link>
    </li>
    <li v-if="this.$store.state.isloggedIn">
      <router-link @click.native="deleteUser" to="/">
        <a class="black-text valign-wrapper">
          <i class="material-icons">delete</i>&emsp;Delete account
        </a>
      </router-link>
    </li>
    <li v-if="this.$store.state.isloggedIn">
      <router-link to="/updatedetails">
        <a class="black-text valign-wrapper">
          <i class="material-icons">update</i>&emsp;Update details
        </a>
      </router-link>
    </li>
  </ul>
</template>

<script>
/* eslint-disable */

export default {
  name: "SideNav",
  mounted() {
    M.AutoInit();
  },
  methods: {
    deleteUser() {
      if (
        confirm("Are you sure you want to delete this account?")
      ) {
        this.$store.dispatch("deleteAccount").then(response => {
          M.toast({ html: response.message });
          if (!response.error) {
            this.$store.commit("setIsLoggedIn", {
              loggedin: false,
              token: null
            });
          }
        });
      }
    }
  }
};
</script>

<style scoped>
.sidenav {
  z-index: 2000;
}
</style>
