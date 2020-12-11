<template>
  <v-container fluid class="main" id="aboutus">
      <div align="center" justify="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer">
            <v-row >
                <p class="text">Payment</p>
            </v-row>
            <v-row align="center" justify="center" >
                <v-card style= "border-radius: 20px;" class="cardDetailContainer" >
                    <v-row>
                        <v-col cols="6"><label class="textDetail">Customer name : {{ this.user.firstName }} {{ this.user.familyName  }}</label></v-col>
                        <v-col cols="6"><label class="textDetail">Payment Method: {{ this.user.paymentMethod  }}</label></v-col>
                    </v-row>
                    <v-row justify="center">
                      <v-card class="cardInput" elevation="0">
                        <v-row>
                          <div style="margin-top: 15px;">
                              <label class="textDetail2">CreditCard Number </label>
                          </div>
                          <div></div>
                          <div>
                              <v-text-field
                                  ref="creaditNumber"
                                  :rules="[v => !!v || 'Credit card Number is required']"
                                  v-model="user.creaditNumber"
                                  solo
                                  rounded
                                  outlined
                                  autocomplete="creaditNumber"
                              />
                          </div>
                          <div style="margin-top: 15px;">
                              <label class="textDetail2">CVV</label>
                          </div>
                          <div>
                              <v-text-field
                                  ref="cvv"
                                  :rules="[v => !!v || 'CVV is required']"
                                  v-model="user.cvv"
                                  solo
                                  rounded
                                  outlined
                                  autocomplete="cvv"
                              />    
                          </div> 
                        </v-row>
                      </v-card>       
                    </v-row>
                    <v-row>
                    </v-row>
                </v-card>
            </v-row>
        </v-card>
    </div>
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
        paymentMethod: "Credit Card",
        creaditNumber: "4859-4785-5899-696",
        cvv: "896",
      }
    }
  }
};
</script>

<style scoped>
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 1000px;
  height: 500px;
  margin-top: 15vh;
  margin-left: 20px;
 }

.cardDetailContainer {
  border-radius: 20px;
  width: 850px;
  height: 180px;
  margin-top: 5vh;
 }

.cardInput{
  border-radius: 20px;
  width: 720px;
  height: 80px;
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
  font-size: 19px;
  color: black;
  font-family: "Roboto";
  margin-top: 30px;
}
.textDetail2 {
  font-size: 19px;
  color: black;
  font-family: "Roboto";
  margin-top: 40px;
}
.inputFiled{
  width: 200px;
  height: 25px;
  margin-top: 20px;
  margin-left: 20px;
  margin-right: 20px;
  margin-bottom: 35px;
}
</style>
