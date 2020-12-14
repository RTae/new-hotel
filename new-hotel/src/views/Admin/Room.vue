<template>
    <v-container fluid class="main" id="Room">
        <v-row justify="center">
            <v-col style="margin-top:50px" cols="10">
                <v-card color="#A0C6FF" class="cardTitleContainer">
                    <v-row justify="center">
                        <v-col class="d-flex justify-start" cols="5">
                            <p class="fontTextTitle">Room empty: 20</p>
                        </v-col>
                        <v-col class="d-flex justify-end" cols="5">
                            <v-btn
                                fab
                                small
                                color="white"
                            >
                                <v-icon>
                                    mdi-plus
                                </v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                    <v-row justify="center">
                        <v-col class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">Single: 20</p>
                        </v-col>
                        <v-col class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">Double: 20</p>
                        </v-col>
                        <v-col class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">Suite: 20</p>
                        </v-col>
                        <v-col class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">Deluxe: 20</p>
                        </v-col>
                        <v-col class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">Premier: 20</p>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
  name: "Room",
  components: {
  },
  mounted() {
  },
  data () {
    return {}
  },
  methods: {},
  omputed:{}
};
</script>

<style scoped>
.main {
    background-color: #FFFFFF;
    min-height: 100vh;
}
.cardTitleContainer{
    min-height: 20vh;
    min-width: 70vw;
}
.fontTextTitle{
    font-size: 20px;
}

</style>
