<template>
  <v-container fluid class="main" id="aboutus">
    <div class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center" align="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer" justify="center" align="center">
            <v-row style="width:840px;" >
              <p class="text">Invoice</p>
            </v-row>
            <v-row style="width:840px;">
                <p class="textTotal">Invoice ID : {{ invoiceID }}</p>
            </v-row>
            <v-row align="center" justify="center" style="margin-top:10px;" >
                <v-card style= "border-radius: 20px;">
                    <v-row justify="center">
                      <v-card class="cardInput" elevation="0">
                        <v-row style="margin-top:50px;">
                          <div><label class="textDetail">Customer name : {{ this.user.firstName }} {{ this.user.familyName  }}</label></div>
                          <v-spacer></v-spacer>
                          <v-spacer></v-spacer>
                          <v-spacer></v-spacer>
                          <div><label class="textDetail">Payment Method: {{ this.user.paymentMethod  }}</label></div>
                        </v-row>
                      </v-card>
                    </v-row>
                    <v-row justify="center">
                      <v-card class="cardInput" elevation="0">
                        <v-row  style="margin-top:50px;">
                          <div style="margin-top: 15px;">
                              <label class="textDetail2">CreditCard Number </label>
                          </div>
                          <v-spacer></v-spacer>
                          <div>
                              <v-text-field
                                  ref="creaditNumber"
                                  :rules="[v => !!v || 'Credit card Number is required']"
                                  v-model="creaditNumber"
                                  solo
                                  rounded
                                  outlined
                                  autocomplete="creaditNumber"
                              />
                          </div>
                          <v-spacer></v-spacer>
                          <v-spacer></v-spacer>
                          <v-spacer></v-spacer>
                          <div style="margin-top: 15px;">
                              <label class="textDetail2">CVV</label>
                          </div>
                          <v-spacer></v-spacer>
                          <div>
                              <v-text-field
                                  ref="cvv"
                                  :rules="[v => !!v || 'CVV is required']"
                                  v-model="cvv"
                                  solo
                                  rounded
                                  outlined
                                  autocomplete="cvv"
                              />    
                          </div> 
                        </v-row>
                      </v-card>       
                    </v-row>
                    <v-row align="center" justify="end" class="cardTotal" >
                      <label class="textTotal" style="margin-top:100px;">Total : {{ this.totalPrice }} bath</label>
                    </v-row>
                </v-card>
            </v-row>
            <v-row justify="center" style="margin-top:150px;">
                <div class="cardTotal" >
                   <v-dialog
                      v-model="dialog"
                      persistent
                      max-width="500px"
                      max-height="800px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
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
                            @click="dialog = false"
                          >
                            YES
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-btn class="btnPayment" type="submit" style="background-color:#28BC49;" dark x-large>Payment</v-btn>
                </div>
            </v-row> 
        </v-card>
      </v-row>      
      </v-toolbar>
    </div>
  </v-container>
</template>

<script scoped>
export default {
  name: "Invoice",
  data () {
    return {
      user: {
        firstName: "",
        familyName: "",
        paymentMethod: "Credit Card",

      },
      invoiceID: null,          
      totalPrice: null,
      dialog: false,
    }
  },
  async mounted () {
    this.$store.commit("SET_DIALOG_LOADING", true)
    const id = localStorage.getItem(server.USERNAME)
    const result = await api.getUser(id)
    if (result.data.status === "1") {
      this.user.firstName = result.data.result[0].Firstname
      this.user.familyName = result.data.result[0].Familyname
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
  justify-content: space-around;
  align-items: center;
  justify-content: center;
  height: 465px;
  width: 100vw;
  background-color: black;
  margin-top: 20vh;
}


.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 1000px;
  height: 720px;
 }

.cardDetailContainer {
  border-radius: 20px;
  width: 850px;
  height: 180px;
  margin-top: 5vh;
 }

.cardInput{
  border-radius: 20px;
  width: 700px;
  height: 100px;
}

.text {
  font-size: 40px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 50px;
  margin-bottom: 40px;
}
.textDetail {
  font-size: 19px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-top: 50px;
}
.textDetail2 {
  font-size: 19px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-top: 40px;
}
.cardTotal{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 850px;
  height: 50px;
}
.textTotal{
  font-size: 25px;
  color: black;
  font-family: "Roboto";
}
.btnCancel{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;
}
.btnDialog{
  display: flex;
  justify-content:space-around; 
  height: 100px;
  background-color:white;
  border-radius: 100px;
}

.cardTitle{
  background-color:white;
  width:500px;
  height:100px;
  size:40px;
  display: flex;
  justify-content: center;
}

.btnPayment{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;
  border-color:white;
}
</style>