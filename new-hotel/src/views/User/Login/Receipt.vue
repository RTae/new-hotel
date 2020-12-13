<template>
  <v-container fluid class="main" id="Receipt">
    <v-row class="bg">
    <v-toolbar
        src="../../../../dist/img/mainFirst.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center" align="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer" justify="center" align="center"> 
          <v-row style="width:840px;">
            <p class="textTitle">Receipt</p>
            </v-row>
            <v-row style="width:840px;">
                <p class="textTotal" >Invoice ID : {{ invoiceID }}</p>
            </v-row>
            <v-row align="center" justify="center">
                <v-card style= "border-radius: 20px;" class="cardDetailCotainer">
                    <v-row align="center" justify="center" style="margin-top: 18px;">
                        <v-col>
                            <v-row class="ml-8" justify="start">
                            <label>Customer ID : {{this.user.customerID}}</label>
                            </v-row>
                        </v-col>
                        <v-col>
                            <v-row class="ml-8" justify="start">
                            <label>Date :</label>
                            </v-row> 
                        </v-col>
                    </v-row>
                    <v-row align="center" justify="start">
                        <v-col>
                            <v-row class="ml-8" justify="start">
                                <label>Payment Method : Credit Card</label>
                            </v-row>
                        </v-col>
                        <v-col>
                            <v-row class="ml-8" justify="start">
                                <label>Total : {{ this.totalPrice }} bath</label>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card>
            </v-row>
            <!-- Button -->
            <v-row justify="center" style="margin-top:80px;">
                <div class="cardBTN" >
                    <v-btn class="btnCancel" type="submit" style="background-color:#ED3636;" dark x-large>Cancel</v-btn>
                    <v-btn class="btnFinish" type="submit" style="background-color:#28BC49;" dark x-large>Finish</v-btn>
                </div>
            </v-row> 
        </v-card>
      </v-row>
    </v-toolbar>  
    </v-row>
  </v-container>
</template>

<script>
export default {
name: "Receipt",
    data () {
        return {
            user: { 
                customerID: "1000",
            },
            totalPrice: "5000"
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
 }

.cardDetailCotainer{
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 850px;
  height: 150px;
}

.textTitle {
  font-size: 40px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 30px;
  margin-bottom: 40px;
}

label{
  font-size: 20px;
  color: #5c5c5c;
  font-family: "Roboto"; 
}
.textTotal{
  font-size: 25px;
  color: black;
  font-family: "Roboto";
}
.signUpBtn {
  background-color: #C4C4C4;
  background-position: center;
  font-family: "Roboto";
  border-radius: 100px;
  margin-right: 20px;
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

.signUpBtn:hover {
  background: #989191 radial-gradient(circle, transparent 1%, #47a7f5 1%)
    center/15000%;
}

.signUpBtn:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}

.cardBTN{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 850px;
  height: 50px;

}

.btnCancel{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;
}

.btnFinish{
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  width: 150px;
  height: 60px;
  font-size: 20px;

}
</style>
