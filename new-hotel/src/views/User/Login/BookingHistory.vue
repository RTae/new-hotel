<template>
  <v-container fluid class="main" id="bookingHistory">
    <v-row class="bg">
    <v-toolbar
        src="../../../assets/img/bgPayment.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" justify="center" align="center">
          <v-row style="width:840px;">
              <p class="text">Booking History</p></v-row>
           <v-col >
            <div v-for="history in historys" :key="history.receiptID">
              <v-card style= "border-radius: 40px;" class="cardDetailContainer" >
                <p class="textDetail">Receipt ID : {{ history.receiptID }}</p>
                <p class="textDetail">Amount Due : {{ history.totalReceived  }}</p>
                <p class="textDetail">Payment Method : {{ history.paymentMedId | ptoName }}</p>
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
import api from "../../../service/api"
import { server } from "../../../service/constants"
export default {
  name: "bookingHistory",
  async mounted() {
    var customerID = localStorage.getItem(server.USERNAME)
    const result = await api.getReceiptByCustomerID(customerID)
    this.historys = result.data.result
  },
  data () {
    return {
      historys: []
    }
  },
  filters: {
    ptoName (value) {
      if (value === "1     "){
        return "Cash"
      } else {
        return "Credit card"
      }
    }
  },
};
</script>

<style scoped>
.main {
  background-color: #C0D9FF;
}
.bg {
  display: flex;
  height: 988px;
  width: 100vw;
}

.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 1030px;
  min-height: 550px;
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 800px;
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
  font-weight: bold;

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
