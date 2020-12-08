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
          <v-col>
            <v-row>
              <v-col>
                <v-row class="ml-8" justify="start">
                <label>Room Type</label>
                </v-row>
                <div class="inputFiled">
                  <v-select
                    v-model="roomValue"
                    :items="roomType"
                    :rules="[v => !!v || 'Item is required']"
                    label="Choose room type"
                    solo
                    rounded
                    outlined
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
    roomValue: "",
  }),
  mounted () {
    this.$store.dispatch({ type: "enterHome" });
  },
  methods: {
    onClickCourse (name) {
      this.$router.push({ name: "CoursesPage", params: { title: name } })
    },
    onClickSubject (n) {
      this.model = n - 1;
      this.$router.push({ name: "CoursesPage", params: { titleName: this.items[n - 1] } })
    }
  }
};
</script>

<style scoped>
.main {
  background: rgb(239, 239, 239);
  min-height: 100vh;
}

.bg {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  justify-content: center;
  height: 465px;
  width: 100vw;
}
.cardChoose {
  display: flex;
  background-color: #CADFFF;
  height: 93px;
  width: 1074px;
  justify-content: center;
  align-items: center;
  border-radius: 32px;
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
