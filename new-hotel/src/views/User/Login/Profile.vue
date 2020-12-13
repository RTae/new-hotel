<template>
  <v-container fluid class="main" id="profile">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.svg"
        height="800px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" >
          <v-row><p class="text">Profile</p></v-row>
            <div>
              <v-card style= "border-radius: 20px;" class="cardDetailContainer">
                <p class="textDetail">First name : {{ this.user.firstName }}</p>
                <p class="textDetail">Family name : {{ this.user.familyName  }}</p>
                <p class="textDetail">Email : {{ this.user.email }}</p>
                <p class="textDetail">Phone Number : {{ this.user.phoneNumber }}</p>
                <p class="textDetail">Point : {{ this.user.point }}</p>
              </v-card>
            </div>
        </v-card>
      </v-row>
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Profile",
  async mounted () {
    const result = await api.getUser(localStorage.getItem(server.USERNAME))
    if (result.data.status === "1") {
      this.user.firstName = result.data.result[0].Firstname
      this.user.familyName = result.data.result[0].Familyname
      this.user.email = result.data.result[0].Email
      this.user.phoneNumber = result.data.result[0].PhoneNumber
      this.user.point = result.data.result[0].Point
    }
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
}
.bg {
  display: flex;
  height: 800px;
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
}
.textDetail {
  font-size: 18px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-top: 40px;
  margin-left: 40px;
}
</style>
