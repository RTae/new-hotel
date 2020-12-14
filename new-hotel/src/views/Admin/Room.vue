<template>
    <v-container fluid class="main" id="Room">
        <v-row justify="center">
            <v-col style="margin-top:50px" cols="10">
                <v-card color="#A0C6FF" class="cardTitleContainer">
                    <v-row justify="start">
                        <v-col class="d-flex justify-start" cols="6" offset="1">
                            <p class="fontTextTitle">Room empty: {{ totalEmpty }}</p>
                        </v-col>
                    </v-row>
                    <v-row justify="center">
                        <v-col v-for="room in roomCat" :key=room.name class="d-flex justify-center" cols="2">
                            <p class="fontTextTitle">{{ room.name }}: {{ room.count }}</p>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <!-- Table -->
        <v-row style="margin-top:50px;" justify="center">
            <v-col cols="10">
                <v-data-table
                    :headers="headers"
                    :items="rooms"
                    sort-by="roomID"
                    class="elevation-1"
                >
                    <template v-slot:top>
                    <v-toolbar
                        flat
                    >
                        <!-- Create -->
                        <v-dialog
                        v-model="dialog"
                        max-width="500px"
                        >
                            <v-overlay :value="$store.getters.getLoadingState">
                                <v-progress-circular
                                indeterminate
                                size="64"
                                ></v-progress-circular>
                            </v-overlay>
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                            color="primary"
                            dark
                            class="mb-2"
                            v-bind="attrs"
                            v-on="on"
                            >
                            New Item
                            </v-btn>
                        </template>
                        <!-- Edit -->
                        <v-card>
                            <v-card-title>
                            <span class="headline">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                            <v-container>
                                <v-row>
                                <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                                >
                                    <v-select
                                        v-model="editedItem.roomType"
                                        :items="roomCatList"
                                        label="Room Type"
                                    ></v-select>
                                </v-col>
                                <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                                >
                                    <v-select
                                        v-model="editedItem.status"
                                        :items="statusList"
                                        label="Status"
                                    ></v-select>
                                </v-col>
                                <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                                >
                                    <v-select
                                        v-model="editedItem.cleanStatus"
                                        :items="statusList"
                                        label="Clean Status"
                                    ></v-select>
                                </v-col>
                                </v-row>
                            </v-container>
                            </v-card-text>

                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="blue darken-1"
                                text
                                @click="close"
                            >
                                Cancel
                            </v-btn>
                            <v-btn
                                color="blue darken-1"
                                text
                                @click="save"
                            >
                                Save
                            </v-btn>
                            </v-card-actions>
                        </v-card>
                        <!-- Delete -->
                        </v-dialog>
                        <v-dialog v-model="dialogDelete" max-width="500px">
                            <v-overlay :value="$store.getters.getLoadingState">
                                <v-progress-circular
                                indeterminate
                                size="64"
                                ></v-progress-circular>
                            </v-overlay>
                        <v-card>
                            <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                            <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                            <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                        </v-dialog>
                    </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                        <v-icon
                            small
                            class="mr-2"
                            @click="editItem(item)"
                        >
                        mdi-pencil
                        </v-icon>
                        <v-icon
                            small
                            @click="deleteItem(item)"
                        >
                        mdi-delete
                        </v-icon>
                    </template>
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
      roomCat:[],
      totalEmpty:0,
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'Room ID',
          align: 'start',
          value: 'roomID',
        },
        { text: 'Room Type', value: 'roomType' },
        { text: 'Bed Type', value: 'bedType' },
        { text: 'Guest Room', value: 'guestRoom' },
        { text: 'Number Bed', value: 'numberBed' },
        { text: 'Fare', value: 'fare' },
        { text: 'status', value: 'status' },
        { text: 'cleanStatus', value: 'cleanStatus' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      rooms: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      roomCatList:["Single", "Double", "Suite", "Delux", "Premier"],
      statusList:["True", "False"],
      roomCatObject: [
        {
            id: "rc0001",
            name: "Single",
        },
        {
            id: "rc0002",
            name: "Double",
        },
        {
            id: "rc0003",
            name: "Suite",
        },
        {
            id: "rc0004",
            name: "Delux",
        },
        {
            id: "rc0005",
            name: "Premier",
        },
     ],
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    async created () {
        var resultCat = await api.roomSummaryByRoomCat()
        var resultSum = await api.roomSummary()
        this.rooms = resultSum.data.result
        this.roomCat = resultCat.data.result
        this.roomCat.forEach(room => {
            this.totalEmpty = this.totalEmpty + parseInt(room.count)
        });
    },

    methods: {

      editItem (item) {
        this.editedIndex = this.rooms.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.rooms.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      async deleteItemConfirm () {
        this.$store.commit("SET_LOADING_STATE", true)
        if (this.editedItem.status == "False"){
            this.closeDelete()
        } else {
            var roomID = this.editedItem.roomID
            const result = await api.deleteRoom(roomID)
            this.rooms.splice(this.editedIndex, 1)
            this.closeDelete()
        }
        this.$store.commit("SET_LOADING_STATE", false)
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },
      async save () {
        this.$store.commit("SET_LOADING_STATE", true)
        if (this.editedIndex > -1) {
          var roomID = this.editedItem.roomID
          var roomType = this.editedItem.roomType
          var status = this.editedItem.status
          var cleanStatus = this.editedItem.cleanStatus
          var roomCatID = this.roomCatObject.find( ({ name }) => name === roomType );
          roomCatID = roomCatID.id
          if (status == "False"){
            status = "0"
          }else {
            status = "1"
          }
        if (cleanStatus == "False"){
            cleanStatus = "0"
          }else {
            cleanStatus = "1"
          }
          const result = await api.updateRoom({roomID, roomCatID, status, cleanStatus, })
          Object.assign(this.rooms[this.editedIndex], this.editedItem)
        } else {
          this.rooms.push(this.editedItem)
        }
        this.close()
        this.$store.commit("SET_LOADING_STATE", false)
      },
    },
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
}
.fontTextTitle{
    font-size: 20px;
}

</style>
