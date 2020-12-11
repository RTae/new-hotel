<template>
  <v-container fluid class="main" id="Home">
    <v-row class="bg">
      <v-toolbar
        src="../../../dist/img/mainFirst.png"
        height="800px"
        width="100vw"   
        flat
      >
        <div class="cardContain" align="center"> 
            <v-row justify="center" class="cardChoose">
              <v-col cols="1"></v-col>          
              <v-col class="ChooseContain">
                <v-row justify="start">
                  <label>Room Type</label>
                </v-row>
                <v-row>
                  <div class="inputFiled">
                    <v-select
                      v-model="roomValue"
                      :items="roomType"
                      :rules="[v => !!v || 'Item is required']"
                      autocomplete="roomType"
                    />
                  </div>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                  <label>Arrival Date</label>
                </v-row>
                <v-row justify="start">
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
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Departure Date</label>
                </v-row>
                <v-row justify="start" >
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
                        v-model="dateFormatted"
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
                      @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Number of room</label>
                </v-row>
                <v-row>
                  <div class="inputFiled">
                    <v-select
                      v-model="numValue"
                      :items="numOfRoom"
                      :rules="[v => !!v || 'Item is required']"
                      autocomplete="numOfRoom"
                    />
                  </div>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Guest</label>
                </v-row>
                <v-row>
                  <div class="inputFiled">
                    <v-select
                      v-model="peopelValue"
                      :items="peopel"
                      :rules="[v => !!v || 'Item is required']"
                      autocomplete="roomType"
                    />
                  </div>
                </v-row>
              </v-col>
              <v-col  cols="1">
                <v-btn
                    class="ma-2"
                    text
                    icon
                    color="black"
                    x-large
                  ><span class="material-icons">
                    search
                </span></v-btn>
              </v-col>
               <v-col cols="1"></v-col> 
            </v-row>
            <v-row justify="center" align="center">
              <v-card class="cardAbout" style="border-radius: 30px;">
                <v-row justify="center"><p class="textAbout">ABOUT US</p></v-row>
                <v-row justify="center" class="textDetailAboutUs">
                  <p>ในปี พ. ศ. 2563 บริษัท กลุ่ม Newway จำกัด ซึ่งเป็นกลุ่มค้าปลีกชั้นนำของประเทศไทยได้ก่อตั้ง</p>
                  <p>บริษัท นิวโฮเทลส์แอนด์รีสอร์ท และได้เปิดตัวโรงแรมแห่งแรก ซึ่งเป็นโรงแรมระดับ 5 ดาวสุดหรู</p>
                  <p>ที่ชื่อ New Hotel ตั้งอยู่ใจกลางเมืองกรุงเทพ โดยวิสัยทัศน์ของบริษัทคือการทุ่มเทให้กับการบริการที่ดีเลิศ</p>
                  <p>ในฐานะที่เป็นบริษัทบริหารและการจัดการโรงแรมสัญชาติไทย จึงให้ความสำคัญกับการต้อนรับแบบไทยที่อบอุ่น</p>
                </v-row>
              </v-card>
            </v-row>
        </div>
      </v-toolbar>
    </v-row>
    <v-row class="numRoom"> 
      <v-col cols="2">
        <v-row justify="center">
          <label class="textType">Single</label>
        </v-row>
        <v-row justify="center">
          <label class="textType">{{ this.numRoomSingle }}</label>
        </v-row>
      </v-col>
      <v-col cols="2">
        <v-row justify="center">
          <label class="textType">Double</label>
        </v-row>
        <v-row justify="center">
          <label class="textType">{{ this.numRoomDouble }}</label>
        </v-row>
      </v-col>
      <v-col cols="2">
        <v-row justify="center">
          <label class="textType">Suite</label>
        </v-row>
        <v-row justify="center">
          <label class="textType">{{ this.numRoomSuite }}</label>
        </v-row>        
      </v-col>
      <v-col cols="2">
        <v-row justify="center">
          <label class="textType">Deluxe</label>
        </v-row>
        <v-row justify="center">
          <label class="textType">{{ this.numRoomDeluxe }}</label>
        </v-row>
      </v-col>
      <v-col cols="2">
        <v-row justify="center">
          <label class="textType">Premier</label>
        </v-row>
        <v-row justify="center">
          <label class="textType">{{ this.numRoomPremier }}</label>
        </v-row>
      </v-col>
    </v-row>
    <!--Detail-->
    <v-card class="room"> 
      <v-row class="containRoom">
        <v-col cols="6">
          <v-img class="imgRoom" src="../../../dist/img/single.png"></v-img>
        </v-col>
        <v-col cols="6">
            <v-row justify="center" style="margin-top:80px">
              <label class="textHead">Single Room</label>
            </v-row>
            <v-row justify="center" style="margin-top:20px">
              <label>This 22 sqm Single Room has single bed positioned near a window offering natural light and pleasant views of the city.  Guests can help themselves to complimentary hot drinks and drinking water</label>
            </v-row>
        </v-col>  
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px"> 
            <label class="textHead">Double Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <label>This 26 sqm Superior Room has twin single beds positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-img class="imgRoom" src="../../../dist/img/double.png"></v-img>
        </v-col>
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-img class="imgRoom" src="../../../dist/img/suite.png"></v-img>
        </v-col>
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Suite Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <label>This 50 sqm Superior Room has 2 room that it has a guest room and  a queen bed positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Deluxe Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <label justify="center" style="margin-top:20px">This 60 sqm deluxe Room has 2 room that it has a guest room and  a king bed positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-img class="imgRoom" src="../../../dist/img/deluxe.png"></v-img>
        </v-col>
      </v-row>
       <v-row class="containRoom">
        <v-col cols="6">
          <v-img class="imgRoom" src="../../../dist/img/premier.png"></v-img>
        </v-col>
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Premier</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <label>This 60 sqm deluxe Room has 2 room that it has a guest room and  2 king beds positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
          </v-row>
        </v-col>
        
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data: vm => ({
    roomType: ["Single", "Double", "Suite", "Delux", "Premier"],
    numOfRoom: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    peopel: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    menu2: false,
    numRoomSingle: "12",
    numRoomDouble: "12",
    numRoomSuite: "3",
    numRoomDeluxe: "4",
    numRoomPremier: "2",
    roomValue:"",
    numValue:"",
    peopelValue:"",
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
      return `${day}/${month}/${year}`
    },
    parseDate (date) {
      if (!date) return null
      const [month, day, year] = date.split('/')
      return `${year}-${day.padStart(2, '0')}-${month.padStart(2, '0')}`
    },
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
.cardContain{
  justify-content: center;
  align-items: center;
  height: 650px;
  width: 100vw;
  border-radius: 50px;
}
.cardChoose {
  background-color: #CADFFF;
  height: 150px;
  width: 1400px;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
}
.ChooseContain{
  height: 100px;
  width: 80px;
  justify-content: center;
  align-items: center;
  margin-left:10px;
  margin-right:10px;
}
.SubChooseContain{
  height: 100px;
  width: 10px; 
}
.cardAbout{
  background-color: white;
  opacity:  80%;
  width: 1400px;
  height: 450px;
  margin-top: 50px;
}
.numRoom{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  justify-content: center;
  align-items: center;
  background-color: #CADFFF;
  height: 120px;
  width: 100vw;
  margin-top: 335px;
}
.textType{
  font-size: 25px;
  font-family: roboto ;
}
.textAbout{
  font-size: 45px;
  font-weight: bolder;
  font-family: roboto ;
  margin-top: 60px;
}
.textDetailAboutUs{
  font-size: 25px;
  font-family: roboto ; 
  color: black; 
} 
.textHead{
  font-size: 45px;
  font-weight: bolder;
  font-family: roboto ;
}
.room{
  background-color: red;
  height: 2050px;
}
.containRoom{
  background-color:white;
  height:510px;
  width: 100vw;
}
.imgRoom{
  height:490px;  
}
</style>
