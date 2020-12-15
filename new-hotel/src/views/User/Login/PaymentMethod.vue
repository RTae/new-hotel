<template>
  <v-container fluid class="main" id="order">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/bgPayment.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" >
          <v-row><p class="text">Order</p></v-row>
              <v-card style= "border-radius: 20px;" class="cardDetailContainer">
                <v-col >
                <v-row  v-for="order in $store.getters.getInvices" :key="order.id" align="center" justify="center">
                <p class="textDetail">Room Type : {{ order.roomType }}</p>
                <v-spacer></v-spacer>
                <p class="textDetail">{{ order.periodOfStay }} day</p>
                <p class="textDetail">{{ order.numberOfRoom }} room</p>
                <p class="textDetail">Total {{ order.total }} bath</p>
                </v-row>
                </v-col>
              </v-card>
            <v-row><p class="text">Payment Method</p></v-row>
            <v-card style= "border-radius: 20px;" class="cardDetailContainer2">
          <div class="radioContainer">
            <div class="radioLineContainer" style= "margin-top:32px;">
              <v-radio-group
                :rules="[v => !!v || 'You must select payment method']"
                v-model="paymentmethod.name"
                column
                required
              >
                <v-radio class="textradio" label="Credit Card" color="info" value="2" />
                <v-radio class="textradio" label="Cash" color="info" value="1" />
              </v-radio-group>
            </div>
          </div>
          </v-card>
             <v-row justify="center" style="margin-top:40px;" >
                <div class="cardTotal" >
                   <v-dialog
                      v-model="dialog"
                      persistent
                      max-width="500px"
                      max-height="800px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn @click="onClickCancel()"
                          color="#ED3636"
                          x-large
                          dark
                          rounded
                          v-bind="attrs"
                          v-on="on"
                          class="btnCancel"
                          width= "150px"
                        >
                          Cancel
                        </v-btn>
                      </template>
                      <v-card>
                        <v-card-title class="cardTitle">
                          Are you sure to cancel this booking?
                        </v-card-title>
                        <v-card-actions class="btnDialog">
                          <v-btn
                            color="#EB5757"
                            width="100px"
                            @click="dialog = false"
                            large
                            dark
                            rounded
                          >
                            NO
                          </v-btn>
                          <v-btn
                            color="#70CCFF"
                            large
                            dark
                            rounded
                            width="100px"
                            @click="onClickYes()"
                          >
                            YES
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-btn @click="onClickPayment()"
                    class="btnPayment" 
                    type="submit" 
                    style="background-color:#28BC49;" 
                    dark 
                    x-large
                    >
                    Payment</v-btn>
                </div>
            </v-row> 
        </v-card>
      </v-row>
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script>
import api from "../../../service/api"
export default {
  name: "Profile",
  id: "id",
  data () {
    return {
      total:0,
      paymentmethod: {
        name: "1"
      },
      dialog: false,
      invoicesID: []
      }
  },
  mounted() {
    this.total = this.$route.params.total
    this.invoicesID = this.$route.params.invoicesID
  },
  methods: {
    async onClickPayment () {
      if (this.paymentmethod.name === "1"){
        const resultReceipt = await api.createReceipt({
          customerID: this.$store.getters.getUserID,
          paymentMedId: this.paymentmethod.name,
          cuponID: "co0001",
          dateCreate: new Date().toISOString().substr(0, 10),
          paymentRef: "Cash",
          totalReceived: this.total,
          remark: "Test"
        })
        var receiptID = resultReceipt.result
        this.receiptID = receiptID
        for(var i = 0; i < this.invoicesID.length; i++){
          var invoiceID = this.invoicesID[i]
          const result = await api.createReceiptLine({
            receiptID: receiptID,
            invoiceID: invoiceID,
            remark: "Test"
          })
        }
        this.$router.push({ name: "Home" });
      } else {
        this.$router.push({ name: "Invoice", params: {total: this.total, invoicesID: this.invoicesID } });
      }
    },
    onClickYes () {
      this.$router.push({ name: "Home" });
    },
  },
  computed: {
  }
};
</script>

<style scoped>
.main {
  background-color: #C0D9FF;
  height: 1010px;
}

.bg {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  justify-content: center;
  height: 980px;
  width: 100vw;
}
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 950px;
  height: 820px;
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 750px;
  height: 270px;
  margin-top: 3vh;
  margin-left: 75px;
  display: grid;
  grid-template-columns: auto auto auto auto;
 }

 .cardDetailContainer2 {
  color: #A0C6FF;
  border-radius: 20px;
  width: 750px;
  height: 120px;
  margin-top: 3vh;
  margin-left: 75px;
 }

.text {
  font-size: 40px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 50px;
  margin-bottom: 20px;
  margin-left: 80px;
  font-weight: bold;

}

.textDetail {
  font-size: 18px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-top: 20px;
  margin-left: 50px;
}


.radioContainer {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  margin-left: 35px;
}

.radioLineContainer {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  flex-direction: row;
}

.cardTotal{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 1000px;
  height: 50px;
}

.btnCancel{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;
}
.btnPayment{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;
  border-color:white;
}

.btnDialog{
  display: flex;
  justify-content:space-around; 
  height: 100px;
  background-color:white;
  border-radius: 100px;
}

label {
  font-weight: bold;
  font-size: 25px;
  color: #ffffff;
  font-family: "Roboto";
}

.textradio {
  font-weight: bold;
  font-size: 25px;
  color: #ffffff;
  font-family: "Roboto";
}
.large label {
  padding-left: 24px;
  font-size: 48px;
}

</style>
