<template>
  <v-container fluid class="main" id="profile">
    <v-row class="bg">
    <v-toolbar
        src="../../../assets/img/mainFirst.svg"
        height="815px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" >
          <v-row><p class="text">Profile</p></v-row>
            <div>
              <v-card style= "border-radius: 20px;" class="cardDetailContainer">
                <label class="textDetail" >First name : {{ user.firstName }}</label>
                <label class="textDetail">Family name : {{ user.familyName  }}</label>
                <label class="textDetail">Email : {{ user.email }}</label>
                <label class="textDetail">Phone Number : {{ user.phoneNumber }}</label>
                <label class="textDetail">Point : {{ user.point }}</label>
              </v-card>
            </div>
        </v-card>
      </v-row>
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script>
import api from "../../../service/api"
import { server } from "../../../service/constants"
export default {
  name: "Profile",
  async mounted () {
    const result = await api.getCustomer(localStorage.getItem(server.USERNAME))
    if (result.data.status === "1") {
      this.user.firstName = result.data.result.firstname
      this.user.familyName = result.data.result.familyname
      this.user.email = result.data.result.email
      this.user.phoneNumber = result.data.result.phoneNumber
      this.user.point = result.data.result.point
    }
    console.log(this.user)
  },
  data () {
    return {
      user: {
        firstName: "",
        familyName: "",
        email: "",
        phoneNumber: "",
        point: ""
      }
    }
  }
};
</script>

<style scoped>
.main {
  background-color: #C0D9FF;
  height: 815px;
}
.bg {
  display: flex;
  height: 815px;
  width: 100vw;
}
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 900px;
  height: 520px;
 }
.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 750px;
  height: 280px;
  margin-top: 5vh;
  margin-left: 75px;
  display: grid;
  grid-template-columns: auto auto;
 }
.text {
  font-size: 40px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 50px;
  margin-bottom: 20px;
  margin-left: 80px;
  font-weight:bold;
}
.textDetail {
  font-size: 18px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-top: 20px;
  margin-left: 40px;
}
</style>
