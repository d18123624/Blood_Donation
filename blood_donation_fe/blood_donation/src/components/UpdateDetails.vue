<template>
  <div class="full-height valign-wrapper">
    <div class="row">
      <div class="rounded-corners-card-panel center padding-huge relative">
        <div v-if="loading" class="progress zero-margin zero-padding preloader-wrapper">
          <div class="indeterminate"></div>
        </div>
        <span class="font-size-large">Update details</span>
        <br>
        <br>
        <div class="row input-row">
          <div class="input-field col s12">
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
        </div>
        <div class="row">
          <div class="col s12">
            <a
              class="center white-text waves-effect btn-flat teal no-uppercase font-size-small form-btn"
              v-on:click="update"
            >Update</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: "UpdateDetails",
  methods: {
    update() {
      var error = false;
      if (document.getElementById("date").value == "") {
        this.dateerror = "Select last blood donation date!";
        error = true;
      }
      if (error) {
        return;
      }
      this.dateerror = "";
      this.eligiblefordonationerror = "";
      this.loading = true;
      var payload = {
        last_blood_donation: String(document.getElementById("date").value),
        currently_eligible_for_donation: String(this.availableforblooddonation)
      };
      this.$store.dispatch("updateDetails", payload).then(response => {
        console.log(response);
        this.loading = false;
        M.toast({ html: response.message });
        if (!response.error) {
          this.$router.push("/");
        } else {
          if (response.error_fields.last_blood_donation) {
            this.dateerror = response.error_fields.last_blood_donation[0];
          }
          if (response.error_fields.currently_eligible_for_donation) {
            this.eligiblefordonationerror =
              response.error_fields.currently_eligible_for_donation[0];
          }
        }
      });
    }
  },
  mounted() {
    M.AutoInit();
    var elems = document.querySelectorAll(".datepicker");
    var instances = M.Datepicker.init(elems, {
      format: "yyyy-mm-dd"
    });
  },
  data() {
    return {
      eligiblefordonationerror: "",
      dateerror: "",
      availableforblooddonation: true,
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
