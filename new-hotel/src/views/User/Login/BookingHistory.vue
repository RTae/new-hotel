<template>
  <v-container fluid class="main" id="bookingHistory">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/bgPayment.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" justify="center" align="center">
          <v-row style="width:840px;">
              <p class="text">Booking History</p></v-row>
           <v-col>
            <div v-for="history in historys" :key="history.historyID">
              <v-card style= "border-radius: 40px;" class="cardDetailContainer" >
                <p class="textDetail">Room Type : {{ history.roomtype }}</p>
                <p class="textDetail">Number of room : {{ history.numberofroom  }}</p>
                <p class="textDetail">Total : {{ history.total  }}</p>
                <p class="textDetail">Status : {{ history.status  }}</p>
              </v-card>
            </div>
          </v-col>
                <v-row justify="center">
                  <button class="paymentBtn" type="submit">Payment</button>
                </v-row>
        </v-card>
      </v-row>
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "bookingHistory",
  id: "historyID",
  data () {
    return {
      historys: [
        {
        roomtype: "Deluxe",
        numberofroom:  "2",
        total: "5000",
        status: "ว่าง"
        },
        {
        roomtype: "Deluxe",
        numberofroom: "5",
        total: "6000",
        status: "ว่าง"
        }
      ]
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
  width: 1030px;
  height: 500px;
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 800px;
  height: 80px;
  margin-top: 2vh;
  display: grid;
  grid-template-columns: auto auto auto auto;
 }

.text {
  font-size: 40px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 50px;
  margin-bottom: 15px;

}

.textDetail {
  font-size: 18px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-left: 10px;
  margin-top: 30px;
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
