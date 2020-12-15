<template>
  <v-container fluid class="main" id="Home">
    <v-row class="bg">
      <v-toolbar
        src="../../assets/img/hotel.svg"
        height="800px"
        width="800px"   
        flat
      >
        <div class="cardContain" align="center"> 
            <v-row justify="center" class="cardChoose">
              <v-col cols="1"></v-col>          
              <v-col class="ChooseContain">
                <v-row justify="start">
                  <label>Room Type</label>
                </v-row>
                <v-row style="margin-top:20px;">
                    <v-select
                      append-outer-icon="night_shelter"
                      v-model="roomValue"
                      :items= "['Single', 'Double', 'Suite', 'Delux', 'Premier']"
                      :rules="[v => !!v || 'Plase choose is room type']"
                      autocomplete="roomType"
                    />
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                  <label>Arrival Date</label>
                </v-row>
                <v-row justify="start" style="margin-top:20px;">
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
                        v-model="dateCheckIn"
                        persistent-hint
                        readonly
                        append-icon="date_range"
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="dateCheckIn"
                      :min="this.today"
                      no-title
                      @input="menuCheckIn = false"
                    ></v-date-picker>
                  </v-menu>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Departure Date</label>
                </v-row>
                <v-row justify="start" style="margin-top:20px;" >
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
                        v-model="dateCheckOut"
                        persistent-hint
                        append-icon="date_range"
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      :min="this.dateCheckIn"
                      v-model="dateCheckOut"
                      no-title
                      @input="menuCheckOut = false"
                    ></v-date-picker>
                  </v-menu>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Number of room</label>
                </v-row>
                <v-row style="margin-top:20px;">
                  <v-text-field 
                    v-model="numRoom" 
                    type="number"
                    :min="0" 
                    :max="10"
                    append-icon="local_hotel">
                  </v-text-field>
                </v-row>
              </v-col>
              <v-col class="ChooseContain">
                <v-row justify="start">
                <label>Guest</label>
                </v-row>
                <v-row style="margin-top:20px;">
                  <v-text-field 
                    v-model="numGuest" 
                    type="number"
                    :min="0" 
                    :max="50"
                    append-icon="family_restroom"
                    >
                  </v-text-field >
                </v-row>
              </v-col>
              <v-col  cols="2">
                <v-btn
                    width="150px"
                    depressed
                    color="#A0C6FF"
                    elevation="2"
                    x-large
                    rounded
                    @click="onClickBooking()"
                  > 
                  BOOK
                  <v-icon right>book_online</v-icon>
                </v-btn>
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
          <v-hover v-slot:default="{ hover }">
            <v-img class="imgRoom" src="../../assets/img/single.svg">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out  grey darken-3 v-card--reveal display-3 white--text"
                  style="height: 100%;"
                >
                  ฿ 1,500 / per night
                </div>
              </v-expand-transition>
            </v-img>
          </v-hover>
        </v-col>
        <v-col cols="6" justify="center"> 
            <v-row justify="center" style="margin-top:80px">
              <label class="textHead">Single Room</label>
            </v-row>
            <v-row justify="center" class="textDetailAboutUs">
              <div class="textDetaiRoomContain">
                <label class="textDetaiRoom">This 22 sqm Single Room has single bed positioned near a window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
              </div>
            </v-row>
        </v-col>  
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px"> 
            <label class="textHead">Double Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <div class="textDetaiRoomContain">
                <label class="textDetaiRoom">This 26 sqm Superior Room has twin single beds positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
            </div>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-hover v-slot:default="{ hover }">
            <v-img class="imgRoom" src="../../assets/img/double.svg">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out grey darken-3 v-card--reveal display-3 white--text"
                  style="height: 100%;"
                >
                  ฿ 2,500 / per night
                </div>
              </v-expand-transition>
            </v-img>
          </v-hover>       
        </v-col>
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-hover v-slot:default="{ hover }">
            <v-img class="imgRoom" src="../../assets/img/suite.svg">
              <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out grey darken-3 v-card--reveal display-3 white--text"
                    style="height: 100%;"
                  >
                    ฿ 3,000 / per night
                  </div>
                </v-expand-transition>
            </v-img>
          </v-hover>
        </v-col>
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Suite Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <div class="textDetaiRoomContain">
              <label class="textDetaiRoom">This 50 sqm Superior Room has 2 room that it has a guest room and  a queen bed positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
            </div>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="containRoom">
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Deluxe Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <div class="textDetaiRoomContain">
              <label class="textDetaiRoom">This 60 sqm deluxe Room has 2 room that it has a guest room and a king bed positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
            </div>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-hover v-slot:default="{ hover }">
            <v-img class="imgRoom" src="../../assets/img/deluxe.svg">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out grey darken-3 v-card--reveal display-3 white--text"
                  style="height: 100%;"
                >
                  ฿ 4,000 / per night
                </div>
              </v-expand-transition>
            </v-img>
          </v-hover>
        </v-col>
      </v-row>
       <v-row class="containRoom">
        <v-col cols="6">
          <v-hover v-slot:default="{ hover }">
            <v-img class="imgRoom" src="../../assets/img/premier.svg">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out grey darken-3 v-card--reveal display-3 white--text"
                  style="height: 100%;"
                >
                  ฿ 5,000 / per night
                </div>
              </v-expand-transition>
            </v-img>
          </v-hover>
        </v-col>
        <v-col cols="6">
          <v-row justify="center" style="margin-top:80px">
            <label class="textHead">Premier Room</label>
          </v-row>
          <v-row justify="center" style="margin-top:20px">
            <div class="textDetaiRoomContain">
              <label class="textDetaiRoom">This 70 sqm deluxe Room has 2 room that it has a guest room and  2 king beds positioned near a large window offering natural light and pleasant views of the city. Guests can help themselves to complimentary hot drinks and drinking water.</label>
            </div>
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
  data(){
     return{
        today: "",
        dateCheckIn: new Date().toISOString().substr(0, 10),
        dateCheckOut: new Date().toISOString().substr(0, 10),
        menuCheckIn: false,
        menuCheckOut: false,
        numRoomSingle: "12",
        numRoomDouble: "12",
        numRoomSuite: "3",
        numRoomDeluxe: "4",
        numRoomPremier: "2",
        roomValue:"Single",
        numRoom:1,
        numGuest:0,
        roomCat: [
            {
                id: "rc0001",
                name: "Single",
                price: 1500
            },
            {
                id: "rc0002",
                name: "Double",
                price: 2500
            },
            {
                id: "rc0003",
                name: "Suite",
                price: 3000
            },
            {
                id: "rc0004",
                name: "Delux",
                price: 4000
            },
            {
                id: "rc0005",
                name: "Premier",
                price: 5000
            },
      ],
      invoice:{}
    }
  },
  mounted() {
    this.today = new Date().toISOString().substr(0, 10)
    const tomorrow = new Date(this.today)
    tomorrow.setDate(tomorrow.getDate() + 1)
    this.tomorrow = tomorrow.toISOString().substr(0, 10)
    this.dateCheckOut = tomorrow.toISOString().substr(0, 10)
  },
  methods: {
    onClickBooking(){
     if (this.$store.getters.getHeaderLoginState) {
        var temp = {}
        const result = this.roomCat.find( ({ name }) => name === this.roomValue );
        var dayIn = Date.parse(this.dateCheckIn)
        var dayOut = Date.parse(this.dateCheckOut)
        temp.roomType = this.roomValue
        temp.dateCheckIn = this.dateCheckIn
        temp.dateCheckOut = this.dateCheckOut
        temp.periodOfStay = ((dayOut-dayIn)/86400000)
        temp.typeID = result.id
        temp.total = temp.periodOfStay * parseInt(this.numRoom) * result.price
        temp.numberOfRoom = this.numRoom
        this.$router.push({ name: "Booking" , params: { invoice: temp } });
     } else {
        this.$router.push({ name: "Login" });
     }
    }
  }
};
</script>

<style scoped>
.main {
  background: #C0D9FF;
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
  height: 468px;
  width: 100vw;
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
  font-size: 20px;
  font-family: roboto ;
}
.SubChooseContain{
  height: 100px;
  width: 10px; 
}
.cardAbout{
  background-color: white;
  opacity:  70%;
  width: 1400px;
  height: 350px;
  margin-top: 80px;
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
  font-size: 40px;
  font-weight: bolder;
  font-family: roboto ;
  margin-top: 45px;
  margin-bottom: 25px;
}
.textDetailAboutUs{
  font-size: 20px;
  font-family: roboto ; 
  color: black; 
} 
.textDetaiCost{
  font-size: 25px;
  font-family: roboto ; 
  color: black; 
}
.cardDetaiCost{
  height: 80px;
  width: 300px;  
  background-color: #CADFFF;
  border-radius: 30px;
}
.textDetaiRoomContain{
  height: 200px;
  width: 800px; 
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
.textDetaiRoom{
  font-size: 20px;
  font-family: roboto ;
}
.v-card--reveal {
align-items: center;
bottom: 0;
justify-content: center;
opacity: .5;
position: absolute;
width: 100%;
}
</style>