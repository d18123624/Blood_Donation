<template>
  <div id="app">
    <Header/>
    <SideNav />
    <router-view/>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import SideNav from "./components/SideNav.vue";

export default {
  name: "app",
  components: {
    Header,
    SideNav
  },
  created: function() {
    if (localStorage.getItem("token")) {
      this.$store.commit('setIsLoggedIn', {
        loggedin: true,
        token: localStorage.getItem("token")
      });
    }
  }
};
</script>