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
                <v-card>
                  <v-card-title>
                    <span class="headline">Book Room</span>
                  </v-card-title>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12">
                          <label>Room Type</label>
                          <v-select
                            label="Choose room type"
                            dense
                            solo
                            rounded
                            outlined
                            outline-color="#47a7f5"
                            item-color="blue accent-2"
                            :items="['Single', 'Double', 'Suite', 'Delux', 'Premier']"
                            :rules="[v => !!v || 'Plase choose is room type']"
                            autocomplete="roomType"
                          />
                        </v-col>
                        <v-col cols="12">
                          <label>Arrival Date</label>
                          <v-menu
                            ref="menu1"
                            v-model="menu1"
                            :close-on-content-click="false"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="290px"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                label="Choose Arrival Date"
                                v-model="dateFormatted"
                                persistent-hint
                                append-icon="mdi-calendar"
                                v-bind="attrs"
                                @blur="date = parseDate(dateFormatted)"
                                v-on="on"
                                dense
                                solo
                                rounded
                                outlined
                                outline-color="#47a7f5"
                              ></v-text-field>
                            </template>
                            <v-date-picker
                              v-model="date"
                              no-title
                              @input="menu1 = false"
                            ></v-date-picker>
                          </v-menu>
                        </v-col>
                        <v-col cols="12">
                          <label>Departure Date</label>
                          <v-menu
                              ref="menu2"
                              v-model="menu2"
                              :close-on-content-click="false"
                              transition="scale-transition"
                              offset-y
                              max-width="290px"
                              min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  label="Choose Departure Date"
                                  v-model="dateFormatted"
                                  persistent-hint
                                  append-icon="mdi-calendar"
                                  v-bind="attrs"
                                  @blur="date = parseDate(dateFormatted)"
                                  v-on="on"
                                  dense
                                  solo
                                  rounded
                                  outlined
                                  outline-color=  "#47a7f5"
                                ></v-text-field>
                              </template>
                              <v-date-picker
                                v-model="date"
                                no-title
                                @input="menu2 = false"
                              ></v-date-picker>
                            </v-menu>
                        </v-col>
                        <v-col cols="12">
                          <label>Number of room</label>
                          <v-select
                            label="Choose Number of room"
                            dense
                            solo
                            rounded
                            outlined
                            outline-color= "#47a7f5"
                            v-model="numValue"
                            :items="['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']"
                            :rules="[v => !!v || 'Plase choose is number of Room']"
                            autocomplete="numOfRoom"
                          />
                        </v-col>
                        <v-col cols="12">
                          <label>Guest</label>
                          <v-select
                            label="Choose Guest"
                            dense
                            solo
                            rounded
                            outlined
                            outline-color="#47a7f5"
                            :items="['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']"
                            :rules="[v => !!v || 'Plase choose is number of Guest']"
                            autocomplete="roomType"
                          />
                        </v-col>
                      </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="red darken-1"
                      text
                      @click="dialog1 = false"
                    >
                      Close
                    </v-btn>
                    <v-btn
                      color="blue darken-1"
                      text
                      @click="dialog1 = false"
                    >
                      Save
                    </v-btn>
                  </v-card-actions>
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
                        @click="onClickYes()"
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
  name: "Booking",
  data: vm => ({
    dialog1: false, 
    dialog2: false, 
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    menu2: false,
  }),
  watch: {
    date (val) {
      this.dateFormatted = this.formatDate(this.date)
    },
  },

  methods: {
    formatDate (date) {
      if (!date) return null

      const [year, month, day] = date.split('-')
      return `${month}/${day}/${year}`
    },
    parseDate (date) {
      if (!date) return null

      const [month, day, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    onClickNext () {
      this.$router.push({ name: "PaymentMethod" 
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
}

.bg {
  display: flex;
  max-height: 1500px;
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
  margin-top: 20px;
  
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
</style>
