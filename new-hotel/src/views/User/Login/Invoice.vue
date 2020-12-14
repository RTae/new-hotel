<template>
  <v-container fluid class="main" id="invoice">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center" align="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer" justify="center" align="center">
            <v-row style="width:1000px;"  justify="start" align="start">
              <p class="text">Invoice</p> 
            </v-row>
            <v-row style="width:950px;">
                <p class="textSub">Invoice ID : {{ invoiceID }}</p>
            </v-row>
            <v-row align="center" justify="center" style="margin-top:10px;" >
                <v-card  class="cardDetailContrin" style="border-radius: 20px;">
                    <v-row class="ml-12"  style="margin-top:40px;">
                        <div><label class="textPayment" >Payment Method : {{ this.user.paymentMethod  }}</label></div>
                    </v-row>
                    <v-row justify="center" style="margin-top:20px;">
                      <v-row justify="start" align="center">
                        <div style="width:400px; ">
                          <v-col style="width:400px;">
                            <v-row class="ml-10" justify="start" >
                              <label class="textDetail">Name on card :</label>
                            </v-row>
                            <v-row class="ml-10" justify="start">
                             <div class="inputFiled"  style="width: 200px;">
                              <v-text-field
                                  ref="nameOnCard"
                                  :rules="[v => !!v || 'Name on card is required']"
                                  v-model="nameOnCard"
                                  solo-inverted
                                  dense
                                  placeholder="S. THUNWARA"
                                  autocomplete="nameOnCard"
                              />   
                              </div>
                            </v-row>
                          </v-col>
                        </div>
                        <div style="width:300px;">
                          <v-col style="width:300px;" >
                            <v-row class="ml-6" justify="start">
                              <label class="textDetail" >Expire date :</label>
                            </v-row>
                            <v-row class="ml-6" justify="start">
                              <div class="inputFiled"  style="width: 200px;">
                              <v-text-field
                                ref="expireDate"
                                :rules="[v => !!v || 'Expire date is required']"
                                v-model="expireDate"
                                solo-inverted
                                dense
                                counter
                                maxlength="5"
                                placeholder="XX/XX"
                                autocomplete="expireDate"
                              />
                              </div>
                            </v-row>
                          </v-col>
                        </div>    
                      </v-row>
                      <v-row justify="start" align="center">
                        <div style="width:400px;">
                          <v-col style="width:400px;" >
                            <v-row class="ml-10" justify="start">
                              <label class="textDetail" >CreditCard Number :</label>
                            </v-row>
                            <v-row class="ml-10" justify="start">
                              <div class="inputFiled" style="width: 270px;">
                              <v-text-field
                                  ref="creaditNumber"
                                  :rules="[v => !!v || 'Credit card Number is required']"
                                  v-model="creaditNumber"
                                  solo-inverted
                                  dense
                                  counter
                                  maxlength="19"
                                  placeholder="XXXX-XXXX-XXXX-XXXX"
                                  autocomplete="creaditNumber"
                              />   
                              </div>
                            </v-row>
                          </v-col>
                        </div>
                        <div style="width:300px;">
                          <v-col style="width:300px;">
                            <v-row class="ml-6" justify="start">
                              <label class="textDetail">CVV :</label>
                            </v-row>
                            <v-row class="ml-6" justify="start">
                              <div class="inputFiled"  style="width: 140px;">
                              <v-text-field
                                ref="cvv"
                                :rules="[v => !!v || 'CVV is required']"
                                v-model="cvv"
                                dense
                                solo-inverted
                                counter
                                maxlength="3"
                                placeholder="XXX"
                                autocomplete="cvv"
                              />
                              </div>
                            </v-row>
                          </v-col>
                        </div>
                      </v-row>     
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Total : {{ this.total }} bath</label>
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Vat : {{ (parseInt(this.total) * 0.07) }} bath</label>
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Amount Due : {{ (parseInt(this.total) * 1.07) }} bath</label>
                    </v-row>
                </v-card>
            </v-row>

            <!--BUTTON&DIALOG-->
            <v-row justify="center" style="margin-top:220px;">
                <div class="cardTotal" >
                  <v-dialog
                      v-model="dialogCancel"
                      persistent
                      width="500px"
                      height="800px"
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
                            @click="dialogCancel = false"
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
                  <v-dialog v-model="dialogPayment" persistent width="800px" height="800px">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn 
                          color="#28BC49"
                          x-large
                          dark
                          rounded
                          v-bind="attrs"
                          v-on="on"
                          class="btnPayment"
                          width= "150px"
                      >
                      Payment
                      </v-btn>
                    </template>
                    <v-card style="border-radius: 20px;">
                      <v-card-title>
                        <span style="font-size:50px; margin-top:20px;">Receipt</span>
                      </v-card-title>
                      <v-card-title>
                        <span  style="font-size:25px;">Invoice ID : {{ invoiceID }}</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="6">
                              <label style="font-size:18px; color:black;">Customer ID : {{this.user.customerID}}</label>
                            </v-col>
                            <v-col cols="12" sm="6" md="6">
                              <label   style="font-size:18px; color:black;">Date :</label>
                            </v-col>
                            <v-col cols="12" sm="6" md="6">
                              <label style="font-size:18px; color:black;">Payment Method : Credit Card</label>
                            </v-col>
                            <v-col cols="12" sm="6" md="6">
                              <label style="font-size:18px; color:black;">Total : {{ total }} bath</label>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn 
                          rounded 
                          large 
                          dark
                          width="180px" 
                          color="#7FB2FF"
                          @click="onClickFinnish()"
                          style="margin-bottom:20px magin-right:20px;"
                          >Finish
                          </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </div>
            </v-row> 
        </v-card>
      </v-row>      
      </v-toolbar>
    </v-row>
  </v-container>
</template>

<script scoped>
export default {
  name: "Invoice",
  data () {
    return {
      expireDate:"",
      nameOnCard:"",
      creaditNumber:"",
      cvv:"",
      total:"",
      user: {
        firstName: "",
        familyName: "",
        paymentMethod: "Credit Card",
      },
      invoiceID: null,          
      totalPrice: null,
      dialogPayment: false,
      dialogCancel: false,
    }
  },
  methods: {
    onClickPayment () {
      this.$router.push({ name: "Receipt" 
      });
    },
    onClickFinnish () {
      this.$router.push({ name: "Home" 
      });
    },
    onClickYes () {
      this.$router.push({ name: "Home" 
      });
    }
  },
};
</script>

<style scoped>
.main {
  background-color: #C0D9FF;
  height: 1000px;
}

.bg {
  height: 1000px;
  width: 100vw;
}


.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 900px;
  height: 900px;

 }
 .cardDetailContrin {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 690px;
  height: 360px;
 }

.cardDetailContainer {
  border-radius: 20px;
  width: 800px;
  height: 180px;
  margin-top: 5vh;
 }

.cardInput{
  border-radius: 20px;
  width: 700px;
  height: 100px;
}
.inputFiled {
  width: 250px;
  height: 30px;
  margin-top: 10px;
  margin-left: 20px;
  margin-right: 20px;
  margin-bottom: 35px;
  
}
.text {
  font-size: 50px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 50px;
  margin-bottom: 20px;
  margin-left: 80px;
  font-weight: bold;
}
.textDetail {
  font-size: 19px;
  color: #5c5c5c;
  font-family: "Roboto";
  margin-left: 20px;
  
}

.cardTotal{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 1000px;
  height: 50px;
}
.textSub{
  font-size: 25px;
  color:  #5c5c5c;
  font-family: "Roboto";
  margin-left: 90px;

}

.textTotal{
  font-size: 20px;
  color:  #5c5c5c;
  font-family: "Roboto";
  margin-left: 90px;
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
.textPayment{
  font-size: 22px;
  color: #5c5c5c;
  font-family: "Roboto";
}
.label {
  font-size: 15px;
  color: #5c5c5c;
  font-family: "Roboto";
}
</style>