<template>
  <div id="header">
    <v-app-bar app color="primary" dark height="70px">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="../../assets/logoHotel.png"
          transition="scale-transition"
          width="200"
        />
      </div>
      <v-spacer></v-spacer>
      <v-row align="center" justify="end">
        <v-toolbar-items >
          <router-link to="/">
            <span>
              <v-icon x-large class="btnHome">home</v-icon>
            </span>
          </router-link>
          <span>
            <v-icon x-large class="btnHome">
              more_vert
            </v-icon>
          </span>
          <v-menu
          botton
          transition="slide-y-transition"
          right
          >
            <template v-slot:activator="{ on, attrs }">
              <button style="outline:none" icon v-bind="attrs" v-on="on">
                <v-icon x-large class="btnHome">
                  account_circle
                </v-icon>
              </button>
            </template>

            <v-list>
              <v-list-item v-for="(item, i) in items" :key="i">
                <v-list-item-title>
                  <v-hover v-slot="{ hover }">
                    <button
                      :elevation="hover ? 8 : 0"
                      class="btnPro"
                      @click="onClickHover(item.title)"
                    >
                      {{ item.title }}
                    </button>
                  </v-hover>
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar-items>
      </v-row>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "Header",
  data: () => ({
    items: [
      { title: "My Profile" },
      { title: "My Booking" },
      { title: "Logout" }
    ]
  }),
  methods: {
    onClickHover (functionName) {
      if (functionName === "My Profile") {
        this.$router.push({ name: "Profile" })
      }else if (functionName === "My Booking") {
        this.$router.push({ name: "BookingHistory" })
      } else if (functionName === "Logout") {
        this.$store.dispatch({
          type: "doLogout"
        });
        this.$router.push({name:"Home"})
      }
    }
  }
};
</script>

<style>
.input_serach {
  width: 600px;
  height: 10px;
  margin-top: 10px;
  margin-right: 20px;
}
.btnHeader {
  background-color: white;
  font-family: Roboto;
  border-radius: 100px;
  width: 140px;
  height: 45px;
  opacity: 1;
  transition: 0.3s;
  font-size: 15px;
  text-transform: uppercase;
  color: black;
  box-shadow: 0 0 4px #999;
  cursor: pointer;
  outline: none;
  margin-right: 10px;
  margin-top: 4px;
}

.btnHeader:hover {
  background: #47a7f5
    radial-gradient(circle, transparent 1%, #47a7f5 1%) center/15000%;
}

.btnHeader:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}
.btnHome {
  width: 50px;
  height: 45px;
  margin-right: 20px;
  margin-top: 5px;
}

.text {
  color: black;
  margin-top: 18px;
  font-family: "Average Sans", sans-serif;
  font-size: 30px;
}
.imgHome{
  width: 50px;
}
.btnHome {
  margin-left: 20px;
  margin-top: 8px;
}
</style>
