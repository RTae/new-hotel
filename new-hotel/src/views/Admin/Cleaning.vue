<template>
    <v-container fluid class="main" id="Room">
        <!-- Table -->
        <v-row v-if="selectItem == 'Receipt'" style="margin-top:50px;" justify="center">
            <v-col cols="10">
                <v-data-table
                    :headers="headers"
                    :items="cleaning"
                    class="elevation-1"
                >
                </v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import api from "../../service/api"
export default {
  name: "Room",
  components: {
  },
    data: () => ({
      selectItem: "Receipt",
      headers: [
        { text: 'Employee ID', value: 'employeeID',},
        { text: 'Room ID', value: 'roomID' },
        { text: 'Start Date Time', value: 'startDateTime' },
        { text: 'End Date Time', value: 'endDateTIme' },
      ],
      cleaning: [],
    }),
    async created () {
        this.initialize()
    },

    methods: {
      async initialize(){
        var resultCleaning = await api.getAllCleaning()
        this.cleaning = resultCleaning.data
      },
    }
  }
</script>

<style scoped>
.main {
    background-color: #FFFFFF;
    min-height: 100vh;
}
.cardTitleContainer{
    min-height: 20vh;
    min-width: 70vw;
    display: flex;
    align-items: center;
}
.fontTextTitle{
    font-size: 20px;
}

</style>
