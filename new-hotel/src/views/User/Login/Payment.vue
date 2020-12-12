<template>
  <v-container fluid class="main" id="aboutus">
    <div class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer">
            <v-row >
                <p class="text">Payment</p>
            </v-row>
            <v-row align="center" justify="center" style="margin-top:30px;" >
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
                      <label class="textTotal">Total : {{ this.totalPrice }} bath</label>
                    </v-row>
                </v-card>
            </v-row>
            <v-row justify="center" style="margin-top:150px;">
                <div class="cardTotal" >
                  <v-btn class="btnCancel" type="submit" style="background-color:#ED3636;" dark x-large>Cancel</v-btn>
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
  name: "Profile",
  data () {
    return {
      user: {
        firstName: "Thunwara",
        familyName: "Sunthon",
        paymentMethod: "Credit Card",

      },        
      creaditNumber: "4859-4785-5899-696",
      cvv: "896",  
      totalPrice: "5000"
    }
  }
};
</script>

<style scoped>
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
  height: 650px;
  margin-top: 100px;
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
  height: 80px;
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
  margin-top: 100px;
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
</style>