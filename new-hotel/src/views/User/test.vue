<template>
  <v-container fluid class="main" id="Home">
    <v-row class="bg">
      <v-toolbar
        src="../../../dist/img/mainFirst.png"
        height="1000px"
        width="100vw"   
        flat
      >
        <v-card class="cardChoose"> 
          <v-col >
            <v-row justify="center">             
              <v-col cols="3" >
                <v-row class="ml-8" justify="start">
                <label>Room Type</label>
                </v-row>
                <div class="inputFiled">
                  <v-select
                    v-model="roomValue"
                    :items="roomType"
                    :rules="[v => !!v || 'Item is required']"
                    autocomplete="roomType"
                  />
                </div>
              </v-col>
              <v-col cols="2">
                <v-row class="ml-8" justify="start">
                <label>Arrival Date</label>
                </v-row>
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
                      v-model="dateFormatted"
                      label="Date"
                      hint="MM/DD/YYYY format"
                      persistent-hint
                      append-icon="mdi-calendar"
                      v-bind="attrs"
                      @blur="date = parseDate(dateFormatted)"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="date"
                    no-title
                    @input="menu1 = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="2">
                <v-row class="ml-8" justify="start">
                <label>Departure Date</label>
                </v-row>
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
                      v-model="dateFormatted"
                      label="Date"
                      hint="MM/DD/YYYY format"
                      persistent-hint
                      append-icon="mdi-calendar"
                      v-bind="attrs"
                      @blur="date = parseDate(dateFormatted)"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="date"
                    no-title
                    @input="menu1 = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="2">
                <v-row class="ml-8" justify="start">
                <label>Number of room</label>
                </v-row>
                <div class="inputFiled">
                  <v-select
                    v-model="numValue"
                    :items="numOfRoom"
                    :rules="[v => !!v || 'Item is required']"
                    autocomplete="numOfRoom"
                  />
                </div>
              </v-col>
              <v-col cols="2">
                <v-row class="ml-8" justify="start">
                <label>Guest</label>
                </v-row>
                <div class="inputFiled">
                  <v-select
                    v-model="roomValue"
                    :items="roomType"
                    :rules="[v => !!v || 'Item is required']"
                    autocomplete="roomType"
                  />
                </div>
              </v-col>
            </v-row>
          </v-col> 
        </v-card>
      </v-toolbar>
    </v-row>
    <v-row class="numRoom"> 
      <v-col>
        <text>
          Single
        </text>
        <text>
          12
        </text>
      </v-col>
      <v-col>
      </v-col>
      <v-col>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data: () => ({
    roomType: ["Single", "Double", "Suite", "Delux", "Premier"],
    numOfRoom: ["1", "2", "3", "4", "5"],
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    menu2: false,
  }),
  computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
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
    }
  }
};
</script>

<style scoped>
.main {
  background: rgb(239, 239, 239);
  min-height: 100vh;
}
.a{
  background-color: blue;
}
.bg {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  justify-content: center;
  height: 465px;
  width: 100vw;
  background-color: black;

}
.cardChoose {
  display: flex;
  background-color: #CADFFF;
  height: 150px;
  width: 1400px;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
}
.numRoom{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  justify-content: center;
  align-items: center;
  background-color: #CADFFF;
  height: 156px;
  width: 100vw;
  margin-top: 550px;
}
</style>
