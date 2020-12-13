<template>
  <div id="header">
      <v-app-bar color="primary" dark app height="70px">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </v-app-bar>
      <v-navigation-drawer 
        v-model="drawer"
        absolute
        bottom
        temporary
      >
					<template>
						<v-list nav dense>
							<v-list-item-group style="margin-top:40px" v-model="group" active-class="deep-purple--text text--accent-4">
								<v-list-item class="buttonContainer">
                  <v-list-item-title class="textMenu">
                    <v-btn
                      block
                      color="#8FBBFE"
                      elevation="2"
                      tile
                      x-large
                      @click="onClickBooking()"
                    >
                      Booking
                    </v-btn>
                  </v-list-item-title>
                </v-list-item>

								<v-list-item class="buttonContainer">
                  <v-list-item-title class="textMenu">
                    <v-btn
                      block
                      color="#8FBBFE"
                      elevation="2"
                      tile
                      x-large
                      @click="onClickRoom()"
                    >
                        Room
                    </v-btn>
                  </v-list-item-title>
                </v-list-item>

                <v-list-item class="buttonContainer">
                  <v-list-item-title class="textMenu">
                    <v-btn
                      block
                      color="#8FBBFE"
                      elevation="2"
                      tile
                      x-large
                      @click="onClickManage()"
                    >
                      Manage
                    </v-btn>
                  </v-list-item-title>
                </v-list-item>

                <v-list-item class="buttonContainer">
                  <v-list-item-title class="textMenu">
                    <v-btn
                      block
                      color="#8FBBFE"
                      elevation="2"
                      tile
                      x-large
                      @click="onClickReport()"
                    >
                      Report
                    </v-btn>
                  </v-list-item-title>
                </v-list-item>
							</v-list-item-group>
						</v-list>
					</template>
			</v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "Header",
  data: () => ({
    drawer: false,
    group: null,
  }),
  methods: {
    onClickBooking(){
      this.$router.push({name:"HomeAdmin"})
    },
    onClickRoom(){
      this.$router.push({name:"Room"})
    },
    onClickManage(){
      this.$router.push({name:"Manage"})
    },
    onClickReport(){
      this.$router.push({name:"Report"})
    }
  },
  watch: {
    group () {
      this.drawer = false
    },
  },
};
</script>

<style>
.cardMenu{
  width: 50px;
  height: 80px;
}
.text {
  color: black;
  font-family: "Average Sans", sans-serif;
  font-size: 50px;
}
.buttonContainer{
  margin-top:20px;
  margin-bottom: 20px;
}
.btnDrawer{
  border-radius: 30px;
}
.textMenu {
  color: black;
  font-family: "Average Sans", sans-serif;
  font-size: 50px;
}
.imgHome{
  width: 50px;
}
.btnHome {
  margin-left: 20px;
  margin-top: 8px;
}
</style>




