<template>
  <div class="full-height valign-wrapper">
    <div class="row">
      <div class="rounded-corners-card-panel center padding-huge relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Sign in</span>
        <br>
        <span class="font-size-medium">to continue to Blood Donation</span>
        <br>
        <br>
        <div class="row input-row">
          <div class="input-field col s12">
            <input id="username" type="text" v-model="username">
            <label for="username">Username</label>
            <span v-if="nameerror != ''" class="left left-align red-text font-size-little">{{ nameerror }}</span>
          </div>
          <div class="input-field col s12">
            <input id="password" type="password" v-model="password">
            <label for="password">Password</label>
            <span v-if="passworderror != ''" class="left left-align red-text font-size-little">{{ passworderror }}</span>
          </div>
        </div>
        <div class="row">
          <div class="col s12">
            <router-link to="/signup">
              <a
                class="left waves-effect btn-flat teal-text no-uppercase font-size-small zero-padding"
              >Create account</a>
            </router-link>
            <a
              class="right white-text waves-effect btn-flat teal no-uppercase font-size-small form-btn"
              v-on:click="login"
            >Next</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: "SignIn",
  methods: {
    login() {
      var error = false;
      if (this.username == "") {
        this.nameerror = "Username cannot be empty!"; 
        error = true;
      }
      if (this.password == "") {
        this.passworderror = "Password cannot be empty!";
        error = true;
      }
      if (error) {
        return;
      }
      this.nameerror = "";
      this.passworderror = "";
      this.loading = true;
      var payload = {
        username: String(this.username),
        password: String(this.password)
      };
      this.$store.dispatch("login", payload).then(response => {
        try {
          M.toast({ html: response.message });
        } catch {}
        this.loading = false;
        if (!response.error) {
          this.$router.push("/");
        }
      });
    }
  },
  created: function() {
    M.AutoInit();

    if (this.$store.state.isloggedIn) {
      this.$router.push("/");
      M.toast({ html: "You're already logged in" });
    }
  },
  data() {
    return {
      username: "",
      password: "",
      loading: false,
      nameerror: "",
      passworderror: ""
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.full-height {
  min-height: 100vh;
}

.input-row {
  width: 80vw;
}

@media only screen and (min-width: 601px) {
  /*tablet*/
  .input-row {
    width: 50vw;
  }
}

@media only screen and (min-width: 993px) {
  /*tablet*/
  .input-row {
    width: 40vw;
  }
}

.form-btn {
  border-radius: 4px;
}

.zero-padding {
  padding: 0 !important;
}

.zero-margin {
  margin: 0 !important;
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
