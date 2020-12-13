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
           <v-col >
            <div v-for="history in historys" :key="history.historyID">
              <v-card style= "border-radius: 40px;" class="cardDetailContainer" >
                <p class="textDetail">Receipt ID : {{ history.receiptid }}</p>
                <p class="textDetail">Amount Due : {{ history.amountdue  }}</p>
                <p class="textDetail">Payment Method : {{ history.paymentmethod  }}</p>
                <v-spacer></v-spacer>
              </v-card>
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
  name: "bookingHistory",
  id: "historyID",
  data () {
    return {
      historys: [
        {
        receiptid: "i00001",
        amountdue: "5000",
        paymentmethod: "Credit card"
        },
        {
        receiptid: "i00002",
        amountdue: "6000",
        paymentmethod: "Credit card"
        },
        {
        receiptid: "i00003",
        amountdue: "7000",
        paymentmethod: "Cash"
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
  grid-template-columns: auto auto auto ;
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
  background-color: #28BC49;
  background-position: center;
  font-family: "Roboto";
  border-radius: 100px;
  margin-left: 660px;
  width: 130px;
  height: 45px;
  opacity: 1;
  transition: 0.3s;
  font-size: 13px;
  text-transform: uppercase;
  color: white;
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
