<template>
  <div id="header">
    <v-app-bar app color="primary" dark height="80px">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40px"
        />
      </div>
      <v-spacer></v-spacer>
      <v-row align="center" justify="end">
        <v-toolbar-items >
          <v-btn class="btnHome" color="#A0C6FF"><router-link to="/"><v-img class="imgHome" src="../../../dist/img/home-black-18dp.svg"></v-img></router-link></v-btn>
          <router-link to="/signup"><button class="btnHeader">Sign Up</button></router-link>
          <router-link to="/login"><button class="btnHeader">LogIn</button></router-link>
        </v-toolbar-items>
      </v-row>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "Header",
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
  height: 50px;
  opacity: 1;
  transition: 0.3s;
  font-size: 20px;
  text-transform: uppercase;
  color: black;
  box-shadow: 0 0 4px #999;
  cursor: pointer;
  outline: none;
  margin-right: 10px;
  margin-top: 8px;
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
  margin-top: 8px;
}

.text {
  color: black;
  margin-top: 20px;
  font-family: "Average Sans", sans-serif;
  font-size: 30px;
}
.imgHome{
  width: 50px;
}
</style>
