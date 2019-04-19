<template>
  <div class="navbar-fixed">
    <nav class="white">
      <div class="nav-wrapper white">
        <router-link to="/">
          <a class="black-text font-size-huge">Blood donation</a>
        </router-link>
        <ul class="left">
          <a href="#" data-target="slide-out" class="sidenav-trigger show-on-large">
            <i class="material-icons black-text">menu</i>
          </a>
        </ul>

        <ul class="right">
          <li>
            <a v-on:click="loginOrLogout" class="black-text font-size-medium">{{ loginLogoutText }}</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: "Header",
  methods: {},
  created: function() {
    M.AutoInit();
  },
  data() {
    return {};
  },
  computed: {
    loginLogoutText() {
      if (this.$store.state.isloggedIn) {
        return "Logout";
      } else {
        return "Login";
      }
    }
  },
  methods: {
    loginOrLogout() {
      if (this.$store.state.isloggedIn) {
        this.$store.dispatch("logout").then(response => {
          try {
            M.toast({ html: response.message });
            this.$router.push("/");
          } catch {}
        });
      } else {
        this.$router.push("/signin");
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-fixed {
  z-index: 500;
}
</style>
