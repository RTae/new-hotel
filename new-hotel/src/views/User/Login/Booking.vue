<template>
  <v-container fluid class="main" id="booking">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.png"
        height="800px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" >
          <v-row><p class="text">Booking</p></v-row>
           <v-col>
            <div>
            <v-row justify="center">
              <v-card style= "border-radius: 40px;"  class="cardDetailContainer">
                <p class="textDetail">Room Type : {{ this.booking.roomtype }}</p>
                <p class="textDetail">Arrival Date : {{ this.booking.arrivaldate  }}</p>
                <p class="textDetail">Period of stay : {{ this.booking.periodofstay  }}</p>
                <p class="textDetail">Number of room : {{ this.booking.numberofroom  }}</p>
                <p class="textDetail">Departure Date : {{ this.booking.departuredate  }}</p>
                <p class="textDetail">Total : {{ this.booking.total  }}</p>
              </v-card>
              </v-row>
            </div>
          </v-col>
        </v-card>
      </v-row>
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "booking",
  data () {
    return {
      booking: {
        roomtype: "Deluxe",
        arrivaldate: "10/11/2020",
        periodofstay: "5",
        numberofroom: "2",
        departuredate: "15/11/2020",
        total: "5000"
      }
    }
  },
};
</script>

<style scoped>
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 1030px;
  height: 500px;
  margin-top: 15vh;
  margin-left: 20px;
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 750px;
  height: 100px;
  margin-top: 5vh;
  margin-left: 50px;
  display: grid;
  grid-template-columns: auto auto auto;
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

.paymentBtn {
  background-color: #C4C4C4;
  background-position: center;
  font-family: "Roboto";
  border-radius: 100px;
  margin-left: 760px;
  width: 130px;
  height: 45px;
  opacity: 1;
  transition: 0.3s;
  font-size: 13px;
  text-transform: uppercase;
  color: black;
  box-shadow: 0 0 4px #999;
  cursor: pointer;
  outline: none;
  margin-top: 50px;
}

.paymentBtn:hover {
  background: #989191
    radial-gradient(circle, transparent 1%, #989191 1%) center/15000%;
}
.paymentBtn:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}
</style>
