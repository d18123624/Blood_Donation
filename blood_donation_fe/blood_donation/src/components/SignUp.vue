<template>
  <div class="full-height valign-wrapper">
    <div class="row margin-vertical-32">
      <div class="rounded-corners-card-panel center padding-huge relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Sign Up</span>
        <br>
        <br>
        <div class="row input-row">
          <div class="input-field col s12">
            <input id="name" type="text" v-model="name">
            <label for="name">Name</label>
            <span
              v-if="nameerror != ''"
              class="left left-align red-text font-size-little"
            >{{ nameerror }}</span>
          </div>
          <div class="col s12 valign-wrapper zero-padding">
            <div class="input-field col s4">
              <input id="age" type="number" v-model="age">
              <label for="age">Age</label>
              <span
                v-if="ageerror != ''"
                class="left left-align red-text font-size-little"
              >{{ ageerror }}</span>
            </div>
            <div class="col s4">
              <label>
                <input
                  class="with-gap"
                  name="gender"
                  value="M"
                  type="radio"
                  v-model="gender"
                  checked
                >
                <span>Male</span>
              </label>
            </div>
            <div class="col s4">
              <label>
                <input class="with-gap" name="gender" value="F" type="radio" v-model="gender">
                <span>Female</span>
              </label>
            </div>
          </div>
          <div class="input-field col s12">
            <input id="username" type="text" v-model="username">
            <label for="username">Username</label>
            <span
              v-if="usernameerror != ''"
              class="left left-align red-text font-size-little"
            >{{ usernameerror }}</span>
          </div>
          <div class="input-field col s12">
            <input id="email" type="email" v-model="email">
            <label for="email">Email</label>
            <span
              v-if="emailerror != ''"
              class="left left-align red-text font-size-little"
            >{{ emailerror }}</span>
          </div>
          <div class="input-field col s12">
            <input id="password" type="password" v-model="password">
            <label for="password">Password</label>
            <span
              v-if="passworderror != ''"
              class="left left-align red-text font-size-little"
            >{{ passworderror }}</span>
          </div>
          <div class="input-field col s12">
            <input id="phone" type="tel" maxlength="10" v-model="phone">
            <label for="phone">Phone</label>
            <span
              v-if="phoneerror != ''"
              class="left left-align red-text font-size-little"
            >{{ phoneerror }}</span>
          </div>
          <div class="input-field col s6">
            <select v-model="bloodgroup">
              <option value="A+">A+</option>
              <option value="A-">A-</option>
              <option value="B+">B+</option>
              <option value="B-">B-</option>
              <option value="AB+">AB+</option>
              <option value="AB-">AB-</option>
              <option value="O+">O+</option>
              <option value="O-">O-</option>
            </select>
            <label>Blood group</label>
            <span
              v-if="bloodgrouperror != ''"
              class="left left-align red-text font-size-little"
            >{{ bloodgrouperror }}</span>
          </div>
          <div class="input-field col s6">
            <input id="date" class="datepicker" type="text">
            <label for="date">Last blood donation</label>
            <span
              v-if="dateerror != ''"
              class="left left-align red-text font-size-little"
            >{{ dateerror }}</span>
          </div>
          <div class="col s12">
            <label class="left checkbox-input">
              <input
                type="checkbox"
                class="filled-in"
                checked="checked"
                v-model="availableforblooddonation"
              >
              <span class="black-text">Currently eligible for blood donation</span>
            </label>
            <span
              v-if="eligiblefordonationerror != ''"
              class="left left-align red-text font-size-little"
            >{{ eligiblefordonationerror }}</span>
          </div>
          <div class="col s12 valign-wrapper zero-padding">
            <div class="input-field col s4 m4 l5">
              <input id="latitude" type="number" step="any" v-model="location.lat" class="active">
              <label for="latitude">Latitude</label>
              <span
                v-if="laterror != ''"
                class="left left-align red-text font-size-little"
              >{{ laterror }}</span>
            </div>
            <div class="input-field col s4 m4 l5">
              <input id="longitude" type="number" step="any" v-model="location.lng" class="active">
              <label for="longitude">Longitude</label>
              <span
                v-if="lngerror != ''"
                class="left left-align red-text font-size-little"
              >{{ lngerror }}</span>
            </div>
            <div class="col s4 m4 l2">
              <a
                class="right white-text waves-effect btn-flat teal no-uppercase font-size-small form-btn"
                v-on:click="toggleLocationPickerVisibility"
              >{{ locationPickerButtonText }}</a>
            </div>
          </div>
          <div v-if="isPickLocationVisible" class="col s12">
            <location-picker v-model="location"/>
          </div>
        </div>
        <div class="row">
          <div class="col s12">
            <router-link to="/signin" class="left">
              <a
                class="left waves-effect btn-flat teal-text no-uppercase font-size-small zero-padding"
              >Sign in</a>
            </router-link>
            <a
              v-on:click="signup"
              class="right white-text waves-effect btn-flat teal no-uppercase font-size-small form-btn"
            >Signup</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { LocationPicker } from "vue2-location-picker";

export default {
  name: "SignUp",
  mounted() {
    M.AutoInit();
    M.updateTextFields();

    var elems = document.querySelectorAll(".datepicker");
    var instances = M.Datepicker.init(elems, {
      format: "yyyy-mm-dd"
    });
  },
  methods: {
    toggleLocationPickerVisibility() {
      this.isPickLocationVisible = !this.isPickLocationVisible;
      if (this.isPickLocationVisible) {
        this.locationPickerButtonText = "Hide";
      } else {
        this.locationPickerButtonText = "Pick";
      }
    },
    signup() {
      var error = false;
      if (this.name == "") {
        this.nameerror = "Name cannot be empty!";
        error = true;
      }
      if (this.age == "") {
        this.ageerror = "Age cannot be empty!";
        error = true;
      }
      if (this.username == "") {
        this.usernameerror = "Username cannot be empty!";
        error = true;
      }
      if (this.password == "") {
        this.passworderror = "Password cannot be empty!";
        error = true;
      }
      if (this.phone == "") {
        this.phoneerror = "Phone cannot be empty!";
        error = true;
      }
      if (this.bloodgroup == "") {
        this.bloodgrouperror = "Select blood group!";
        error = true;
      }
      if (this.location.lat == "") {
        this.laterror = "Latitude cannot be empty!";
        error = true;
      }
      if (this.location.lng == "") {
        this.lngerror = "Longitude cannot be empty!";
        error = true;
      }
      if (document.getElementById("date").value == "") {
        this.dateerror = "Select last blood donation date!";
        error = true;
      }
      if (error) {
        return;
      }
      this.nameerror = "";
      this.ageerror = "";
      this.usernameerror = "";
      this.passworderror = "";
      this.phoneerror = "";
      this.bloodgrouperror = "";
      this.laterror = "";
      this.lngerror = "";
      this.dateerror = "";
      this.emailerror = "";
      this.eligiblefordonationerror = "";
      this.loading = true;
      var payload = {
        username: String(this.username),
        password: String(this.password),
        email: String(this.email),
        name: String(this.name),
        age: String(this.age),
        gender: String(this.gender),
        blood_group: this.bloodgroup,
        address_lat: String(this.location.lat),
        address_long: String(this.location.lng),
        mobile_number: String(this.phone),
        last_blood_donation: String(document.getElementById("date").value),
        currently_eligible_for_donation: String(this.availableforblooddonation)
      };
      this.$store.dispatch("signup", payload).then(response => {
        console.log(response);
        this.loading = false;
        if (!response.error) {
          M.toast({ html: response.message });
          this.$router.push("/");
        } else {
          if (response.error_fields.name) {
            this.nameerror = response.error_fields.name[0];
          }
          if (response.error_fields.age) {
            this.ageerror = response.error_fields.age[0];
          }
          if (response.error_fields.username) {
            this.usernameerror = response.error_fields.username[0];
          }
          if (response.error_fields.password) {
            this.passworderror = response.error_fields.password[0];
          }
          if (response.error_fields.mobile_number) {
            this.phoneerror = response.error_fields.mobile_number[0];
          }
          if (response.error_fields.blood_group) {
            this.bloodgrouperror = response.error_fields.blood_group[0];
          }
          if (response.error_fields.address_lat) {
            this.laterror = response.error_fields.address_lat[0];
          }
          if (response.error_fields.address_long) {
            this.lngerror = response.error_fields.address_long[0];
          }
          if (response.error_fields.last_blood_donation) {
            this.dateerror = response.error_fields.last_blood_donation[0];
          }
          if (response.error_fields.email) {
            this.emailerror = response.error_fields.email[0];
          }
          if (response.error_fields.currently_eligible_for_donation) {
            this.eligiblefordonationerror = response.error_fields.currently_eligible_for_donation[0];
          }
        }
      });
    }
  },
  components: {
    LocationPicker
  },
  data: function() {
    return {
      location: {
        lat: 53.35014,
        lng: -6.266155
      },
      loading: false,
      isPickLocationVisible: false,
      locationPickerButtonText: "Pick",
      name: "",
      age: "",
      gender: "M",
      username: "",
      email: "",
      password: "",
      phone: "",
      bloodgroup: "",
      availableforblooddonation: true,
      nameerror: "",
      ageerror: "",
      usernameerror: "",
      passworderror: "",
      phoneerror: "",
      bloodgrouperror: "",
      laterror: "",
      lngerror: "",
      dateerror: "",
      emailerror: "",
      eligiblefordonationerror: ""
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
