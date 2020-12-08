<template>
  <v-container fluid class="main" id="aboutus">
    <v-row justify="center">
      <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer">
        <v-row><p class="text">Profile</p></v-row>
          <div>
            <v-card style= "border-radius: 20px;" class="cardDetailContainer">
              <p class="textDetail">First name : {{ this.user.firstName }}</p>
              <p class="textDetail">Family name : {{ this.user.familyName  }}</p>
              <p class="textDetail">Email : {{ this.user.email }}</p>
              <p class="textDetail">Phone Number : {{ this.user.phoneNumber }}</p>
              <p class="textDetail">Credit Card Number : {{ this.user.creditCardNumber }}</p>
              <p class="textDetail">Point : {{ this.user.point }}</p>
            </v-card>
          </div>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Profile",
  data () {
    return {
      user: {
        firstName: "Thunwara",
        familyName: "Sunthon",
        email: "Thunwara@gmail.com",
        phoneNumber: "098-639-5858",
        creditCardNumber: "4859-4785-5899-696",
        point: "3489"
      }
    }
  }
};
</script>

<style scoped>
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 900px;
  height: 500px;
  margin-top: 15vh;
  margin-left: 20px;
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 750px;
  height: 250px;
  margin-top: 5vh;
  margin-left: 75px;
  display: grid;
  grid-template-columns: auto auto;
 }

.text {
  font-size: 30px;
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
