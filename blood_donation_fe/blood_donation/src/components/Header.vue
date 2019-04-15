<template>
  <div class="navbar-fixed">
    <nav class="white">
      <div class="nav-wrapper white margin-horizontal-16">
        <router-link to="/">
          <a class="black-text font-size-huge">Blood donation</a>
        </router-link>
        <ul class="right">
          <li>
            <a v-on:click="loginOrLogout" class="black-text">
              {{ loginLogoutText }}
            </a>
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
</style>
