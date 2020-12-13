<template>
  <v-container fluid class="main" id="invoice">
    <div class="bg">
    <v-toolbar
        src="../../../../dist/img/bgPayment.svg"
        height="1200px"
        width="100vw"   
        flat
      >
      <v-row justify="center" align="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer" justify="center" align="center">
            <v-row style="width:1000px;"  justify="start" align="start">
              <p class="text">Invoice</p> 
            </v-row>
            <v-row style="width:950px;">
                <p class="textTotal">Invoice ID : {{ invoiceID }}</p>
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
                                  ref="creaditNumber"
                                  :rules="[v => !!v || 'Name on card is required']"
                                  v-model="creaditNumber"
                                  solo
                                  rounded
                                  outlined
                                  autocomplete="creaditNumber"
                              />   
                              </div>
                            </v-row>
                          </v-col>
                        </div>
                        <div style="width:300px;">
                          <v-col style="width:300px;" >
                            <v-row class="ml-8" justify="start">
                              <label class="textDetail" >Expire date :</label>
                            </v-row>
                            <v-row class="ml-8" justify="start">
                              <div class="inputFiled"  style="width: 200px;">
                              <v-text-field
                                ref="expireDate"
                                :rules="[v => !!v || 'Expire date is required']"
                                v-model="expireDate"
                                solo
                                rounded
                                outlined
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
                              <div class="inputFiled" style="width: 400px;">
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
                            </v-row>
                          </v-col>
                        </div>
                        <div style="width:200px;">
                          <v-col style="width:200px;">
                            <v-row class="ml-8" justify="start">
                              <label class="textDetail">CVV :</label>
                            </v-row>
                            <v-row class="ml-8" justify="start">
                              <div class="inputFiled"  style="width: 100px;">
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
                          </v-col>
                        </div>
                      </v-row>     
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Total : {{ this.total }} bath</label>
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Vat : {{ (parseInt(this.total) * 70)/100 }} bath</label>
                    </v-row>
                    <v-row align="center" justify="start" class="cardTotal" >
                      <label class="textTotal" style="margin-top:50px;">Amount Due : {{ (parseInt(this.total) * 170)/100 }} bath</label>
                    </v-row>
                </v-card>
            </v-row>
            <v-row justify="center" style="margin-top:220px;">
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
                            @click="onClickYes()"
                          >
                            YES
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-btn 
                    @click="onClickPayment()"
                    class="btnPayment" 
                    type="submit" 
                    style="background-color:#28BC49;" 
                    dark 
                    x-large
                    >
                    Payment
                  </v-btn>
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
  methods: {
    onClickPayment () {
      this.$router.push({ name: "Receipt" 
      });
    },
    onClickYes () {
      this.$router.push({ name: "Home" 
      });
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
  height: 1100px;
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
  height: 32px;
  margin-top: 10px;
  margin-left: 20px;
  margin-right: 20px;
  margin-bottom: 35px;
  
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
  margin-left: 20px;
  
}

.cardTotal{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 1000px;
  height: 50px;
}
.textTotal{
  font-size: 22px;
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
  font-size: 24px;
  color: #5c5c5c;
  font-family: "Roboto";
}
label {
  font-size: 15px;
  color: #5c5c5c;
  font-family: "Roboto";
}
</style>