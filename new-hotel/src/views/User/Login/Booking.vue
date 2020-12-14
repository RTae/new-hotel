<template>
  <v-container fluid class="main" id="booking">
    <v-row class="bg" >
    <v-toolbar
        src="../../../../dist/img/bgPayment.svg"
        height="1200px"
        width="100vw"   
      >
      <v-row justify="center" class="cardBigContainer">
        <v-card class="cardContainer" style="background-color:#A0C6FF; border-radius: 20px;" >
          <v-row>
            <v-col>
              <p class="text">Booking</p>
            </v-col>
            <v-col style="margin-top: 50px; margin-right:50px;" align="end" justify="center">
              <v-dialog
                v-model="dialog1"
                persistent
                max-width="600px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="white"
                    dark
                    fab
                    class="mx-2"
                    elevation="0"
                    v-bind="attrs"
                    v-on="on"
                    @click="dialog1 = !dialog1"
                  >
                    <span>
                      <v-icon style="color:#6eb9f7;">add</v-icon>
                    </span>
                  </v-btn>
                </template>
                          <v-card class="cardModalContainer">
                              <v-form
                                  ref="form"
                                  v-model="valid"
                                  @submit.prevent="submitAdd"
                                  lazy-validation
                                  style="width:100%; height:100%"
                              >
                                  <v-row>
                                      <v-col cols="4" offset="1">
                                          <label style="color:black; font-size:25px">Room Type:</label>
                                      </v-col>
                                      <v-col cols="6">
                                          <v-select
                                              :items="items"
                                              v-model="invoice.roomType"
                                              :rules="[v => !!v || 'Item is required']"
                                          ></v-select>
                                      </v-col>
                                  </v-row>
                                  <v-row>
                                      <v-col cols="4" offset="1">
                                          <label style="color:black; font-size:25px">Number of Room:</label>
                                      </v-col>
                                      <v-col cols="6">
                                          <v-text-field
                                              v-model="invoice.numberOfRoom"
                                          />
                                      </v-col>
                                  </v-row>
                                  <v-row>
                                      <v-col cols="4" offset="1">
                                          <label style="color:black; font-size:25px">Check In:</label>
                                      </v-col>
                                      <v-col cols="6">
                                          <v-menu
                                              v-model="menuCheckIn"
                                              :close-on-content-click="false"
                                              transition="scale-transition"
                                              offset-y
                                              max-width="290px"
                                              min-width="290px"
                                          >
                                          <template v-slot:activator="{ on, attrs }">
                                              <v-text-field
                                                  v-model="invoice.dateCheckIn"
                                                  persistent-hint
                                                  prepend-icon="mdi-calendar"
                                                  readonly
                                                  v-bind="attrs"
                                                  v-on="on"
                                              ></v-text-field>
                                          </template>
                                          <v-date-picker
                                              v-model="invoice.dateCheckIn"
                                              no-title
                                              @input="menuCheckIn = false"
                                          ></v-date-picker>
                                          </v-menu>
                                      </v-col>
                                  </v-row>
                                  <v-row>
                                      <v-col cols="4" offset="1">
                                          <label style="color:black; font-size:25px">Check out:</label>
                                      </v-col>
                                      <v-col cols="6">
                                          <v-menu
                                              v-model="menuCheckOut"
                                              :close-on-content-click="false"
                                              transition="scale-transition"
                                              offset-y
                                              max-width="290px"
                                              min-width="290px"
                                          >
                                          <template v-slot:activator="{ on, attrs }">
                                              <v-text-field
                                              v-model="invoice.dateCheckOut"
                                              persistent-hint
                                              prepend-icon="mdi-calendar"
                                              readonly
                                              v-bind="attrs"
                                              v-on="on"
                                              ></v-text-field>
                                          </template>
                                          <v-date-picker
                                              v-model="invoice.dateCheckOut"
                                              no-title
                                              @input="menuCheckOut = false"
                                          ></v-date-picker>
                                          </v-menu>
                                      </v-col>
                                  </v-row>
                                  <v-row>
                                      <v-col cols="3" offset="4">
                                          <v-btn @click="onClickCancel()" color="red" class="btnModal">
                                              <p style="margin-top:16px">Cancel</p>
                                          </v-btn>                        
                                      </v-col>
                                      <v-col cols="3" offset="1">
                                          <v-btn type="submit" color="#A0C6FF" class="btnModal">
                                              <p style="margin-top:16px">Add</p>
                                          </v-btn>
                                      </v-col>
                                  </v-row>
                              </v-form>
                          </v-card>
                      </v-dialog>
            </v-col>
          </v-row>
          <v-row justify="center">
            <div v-for="booking in books" :key="booking.bookingID">
              <v-card style= "border-radius: 40px;"  class="cardDetailContainer">
                <label class="textDetail">Room Type : {{ books.roomtype }}</label>
                <label class="textDetail">Arrival Date : {{ books.arrivaldate  }}</label>
                <label class="textDetail">Period of stay : {{ books.periodofstay  }}</label>
                <label class="textDetail">Number of room : {{ books.numberofroom  }}</label>
                <label class="textDetail">Departure Date : {{ books.departuredate  }}</label>
                <label class="textDetail">Total : {{ calculateTotal  }} bath</label>
              </v-card>
            </div>
          </v-row>
          <v-row justify="center" style="margin-top:80px;">
              <div class="cardTotal" >
                <v-dialog
                  v-model="dialog2"
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
                      @click="dialog2 = !dialog2"
                      class="btnCancel"
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
                        color="#ED3636"
                        large
                        dark
                        rounded
                        width="100px"
                        @click="dialog2 = false"
                      >
                        NO
                      </v-btn>
                      <v-btn
                        color="#70CCFF"
                        large
                        dark
                        rounded
                        width="100px"
                        @click="dialog2 = false"
                      >
                        YES
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-btn  
                  @click="onClickNext()" 
                  class="btnPayment" 
                  type="submit" 
                  style="background-color:#28BC49;" 
                  dark x-large>NEXT</v-btn>
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
  name: "login",
  data () {
    return {
        menuCheckIn: false,
        menuCheckOut: false,
        modalAdd: false,
        valid: true,
        counter: 1,
        invoice: {
            roomType: "",
            numberOfRoom: 1,
            dateCheckIn: new Date().toISOString().substr(0, 10),
            dateCheckOut: new Date().toISOString().substr(0, 10),
        },
        numberRule: v  => {
                if (!v.trim()) return true;
                if (!isNaN(parseFloat(v)) && v >= 0 && v <= 999) return true;
                return 'Number has to be between 0 and 999';
        },
        items: ["Single","Double","Suite","Delux","Premier"],
        };
    },
    methods: {
        onClickAdd() {
            this.modalAdd = true
        },
        onClickCancel() {
            this.modalAdd = false
        },
        submitAdd() {
            var state = this.$refs.form.validate();
            if (state) {
                var temp = {}
                const result = this.roomCat.find( ({ name }) => name === this.invoice.roomType );
                var dayIn = Date.parse(this.invoice.dateCheckIn)
                var dayOut = Date.parse(this.invoice.dateCheckOut)
                temp.id = this.counter
                temp.roomType = this.invoice.roomType
                temp.dateCheckIn = this.invoice.dateCheckIn
                temp.dateCheckOut = this.invoice.dateCheckOut
                temp.periodOfStay = ((dayOut-dayIn)/86400000)
                temp.typeID = result.id
                temp.total = temp.periodOfStay * parseInt(this.invoice.numberOfRoom) * result.price
                temp.numberOfRoom = this.invoice.numberOfRoom
                this.modalAdd = false
            }
        },
    },
    computed:{
        checkState(){
            console.log(this.invoices.length !== 0)
            if (this.invoices.length !== 0){
                return false
            } else {
                return true
            }
        }
    }
};
</script>

<style scoped>
.main {
    background-color: #FFFFFF;
    min-height: 100vh;
}

.textContainer{
    display: flex;
    justify-content: center;
    align-content: center;
}

.textShow{
    font-size: 25px;
}

.cardModalContainer{
    min-width: 10vw;
    min-height: 60vh;
    border: 2px solid black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.btnModal {
    width: 100%;
    border-radius: 20px;
    display: flex;
    justify-content: center;
}

.btnContainer{
    margin-top: 20px;
    margin-bottom: 100px;
    width: 70vw;
    display: flex;
    justify-content: flex-end;
}

.main {
  background-color: #C0D9FF;
}

.bg {
  display: flex;
  max-height: 1200px;
  width: 100vw;
}

.cardBigContainer{
  display: flex;
  flex-wrap: wrap;
  align-content:flex-start;
}

.cardContainer {
  background-color: #A0C6FF;
  border-radius: 200px;
  width: 1030px;
  max-height: 200vh;
  
 }

.cardDetailContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 850px;
  height: 100px;
  margin-top: 2vh;
  display: grid;
  grid-template-columns: auto auto auto;
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
  margin-left: 40px;
  margin-top: 12px;
}


.cardTotal{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 850px;
  height: 50px;
  margin-bottom:50px;
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

.cardContainer{
    margin-top: 100px;
    min-height: 70vh;
    min-width: 70vw;
}

.cardOrder{
    min-width: 60vw;
    min-height: 10vh;
    margin-top: 30px;
    margin-bottom: 30px;
}

</style>
