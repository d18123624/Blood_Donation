<template>
  <div class="col s12">
    <div class="rounded-corners-card-panel padding-16 margin-4">
      <div v-if="name != ''" class="row zero-margin zero-padding">
        <span class="font-size-large teal-text">{{ name }}</span>
      </div>
      <div class="row zero-margin zero-padding">
        <div v-if="age != ''" class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ age }}</span>
        </div>
        <div v-if="gender != ''" class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ gender }}</span>
        </div>
      </div>
      <div class="row zero-margin zero-padding">
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ bloodgroup }}</span>
        </div>
        <div v-if="phonenumber != ''" class="col s6 zero-margin zero-padding">
          <a :href="phonehref">
            <span class="font-size-small teal-text">{{ phonenumber }}</span>
          </a>
        </div>
      </div>
      <div class="row zero-margin zero-padding">
        <div v-if="where == '0'" class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ distance }}</span>
        </div>
        <div v-if="email != ''" class="col s6 zero-margin zero-padding">
          <span class="font-size-small">{{ email }}</span>
        </div>
      </div>
      <div class="row zero-margin zero-padding">
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small truncate">{{ longitude }}</span>
        </div>
        <div class="col s6 zero-margin zero-padding">
          <span class="font-size-small truncate">{{ latitude }}</span>
        </div>
      </div>
      <div class="row zero-margin zero-padding center">
        <a
          v-if="isAuthorizedUserSearching && where == '0'"
          v-on:click="requestForBloodDonation"
          class="waves-effect waves-light btn margin-top-16"
        >Request Blood Donation</a>
        &nbsp;
        <a :href="'/location/' + latitudeVal + '/' + longitudeVal" target="_blank" class="waves-effect waves-light btn margin-top-16">See location on map</a>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "SearchResult",
  created: function() {
    M.AutoInit();
  },
  props: ["result", "where"],
  computed: {
    isAuthorizedUserSearching() {
      try {
        return this.result.match_person ? true : false;
      } catch {
        return false;
      }
    },
    latitude() {
      try {
        return "Latitude: " + this.result.match_person.address_lat;
      } catch {
        if (this.result.latitude) {
          return "Latitude: " + this.result.latitude;
        } else {
          return "Latitude: " + this.result.address_lat;
        }
      }
    },
    latitudeVal() {
      try {
        return this.result.match_person.address_lat;
      } catch {
        if (this.result.latitude) {
          return this.result.latitude;
        } else {
          return this.result.address_lat;
        }
      }
    },
    longitude() {
      try {
        return "Longitude: " + this.result.match_person.address_long;
      } catch {
        if (this.result.longitude) {
          return "Longitude: " + this.result.longitude;
        } else {
          return "Longitude: " + this.result.address_long;
        }
      }
    },
    longitudeVal() {
      try {
        return this.result.match_person.address_long;
      } catch {
        if (this.result.longitude) {
          return this.result.longitude;
        } else {
          return this.result.address_long;
        }
      }
    },
    distance() {
      return "Distance (metres): " + this.result.distance_in_metres;
    },
    name() {
      try {
        return this.result.match_person.name;
      } catch {
        if (this.result.name) {
          return this.result.name;
        } else {
          return "";
        }
      }
    },
    email() {
      try {
        return this.result.match_person.email;
      } catch {
        if (this.result.email) {
          return this.result.email;
        } else {
          return "";
        }
      }
    },
    age() {
      try {
        return "Age: " + this.result.match_person.age;
      } catch {
        return "";
      }
    },
    gender() {
      try {
        return (
          "Gender: " +
          (this.result.match_person.gender === "M" ? "Male" : "Female")
        );
      } catch {
        return "";
      }
    },
    bloodgroup() {
      try {
        return "Bloodgroup: " + this.result.match_person.blood_group;
      } catch {
        return "Bloodgroup: " + this.result.blood_group;
      }
    },
    phonenumber() {
      try {
        return "Phone: " + this.result.match_person.mobile_number;
      } catch {
        if (this.result.mobile_number) {
          return "Phone: " + this.result.mobile_number;
        } else {
          return "";
        }
      }
    },
    phonehref() {
      try {
        return "tel:" + this.result.match_person.mobile_number;
      } catch {
        return "";
      }
    }
  },
  methods: {
    requestForBloodDonation() {
      var payload = {
        search_match_donation_id: this.result.id
      };
      this.$store
        .dispatch("requestForBloodDonation", payload)
        .then(response => {
          M.toast({ html: response });
        });
    }
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
