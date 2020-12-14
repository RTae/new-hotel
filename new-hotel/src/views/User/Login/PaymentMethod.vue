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
                <v-row  v-for="order in orders" :key="order.id" align="center" justify="center">
                <p class="textDetail">Room Type : {{ order.roomtype }}</p>
                <v-spacer></v-spacer>
                <p class="textDetail">x   {{ order.periodofstay }} day</p>
                <p class="textDetail">x {{ order.numberofroom }} room</p>
                <p class="textDetail">Total {{ order.total }} bath</p>
                </v-row>
                <v-row>
                  <v-spacer></v-spacer>
                  <p class="textDetail">Sum Total {{(parseInt(this.total))}} bath</p>
                </v-row>
                </v-col>
              </v-card>
            <v-row><p class="text">Payment Method</p></v-row>
          <div class="radioContainer">
            <div class="radioLineContainer">
              <v-radio-group
                :rules="[v => !!v || 'You must select payment method']"
                v-model="paymentmethod.name"
                column
                required
              >
                <v-radio class="textradio" label="Credit Card" color="info" value="a" />
                <v-radio class="textradio" label="Cash" color="info" value="b" />
              </v-radio-group>
            </div>
          </div>
             <v-row justify="center" style="margin-top:10px;" >
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
export default {
  name: "Profile",
  id: "id",
  data () {
    return {
      total:"",
      orders: [{
        roomtype: "Deluxe",
        periodofstay: "5",
        numberofroom: "1",
        total: "5000"
      },
      {
        roomtype: "Suite",
        periodofstay: "5",
        numberofroom: "1",
        total: "6000"
      },
      {
        roomtype: "Premier",
        periodofstay: "5",
        numberofroom: "1",
        total: "7000"
      }
      ],
       paymentmethod: {
        name: ""
       },
       dialog: false,
    }
    },
      methods: {
      onClickPayment () {
      this.$router.push({ name: "Invoice" 
      });
    },
      onClickYes () {
      this.$router.push({ name: "Home" 
      });
    }
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
  height: 1000px;
  width: 100vw;
}
.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 950px;
  height: 800px;
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
  margin-top: 20px;
  margin-left: 50px;
}


.radioContainer {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  margin-left: 75px;
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
