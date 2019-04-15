<template>
  <div id="app">
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  name: "app",
  components: {
    Header
  },
  created: function() {
    if (localStorage.getItem("token")) {
      this.$store.commit('setIsLoggedIn', {
        loggedin: true,
        token: localStorage.getItem("token")
      })
    }
  }
};
</script>