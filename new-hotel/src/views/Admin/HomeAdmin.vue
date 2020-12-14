<template>
    <v-container fluid class="main" id="HomeAdmin">
        <v-row justify="center" align="center">
            <v-card style="background-color: #A0C6FF; border-radius: 40px;" class="cardContainer">
                <v-row>
                    <v-col style="margin-left:50px;">
                        <h1 style="font-size:50px">Booking</h1>
                    </v-col>
                    <v-col style="display: flex; justify-content: flex-end; margin-top:20px; margin-right:30px">
                        <v-btn
                            class="mx-2"
                            fab
                            color="white"
                            @click="onClickAdd()"
                        >
                        <h1>+</h1>
                        </v-btn>
                    </v-col>
                </v-row>
                <v-row justify="center" v-for="(invoice) in invoices" :key="invoice.id">
                    <v-card style="border-radius: 25px;" class="cardOrder">
                        <v-row justify="center" align="center">
                            <v-col class="textContainer">
                                <p class="textShow">Room Type: {{ invoice.roomType }}</p>
                            </v-col>
                            <v-col class="textContainer">
                                <p class="textShow">Arrival Date: {{ invoice.dateCheckIn }}</p>
                            </v-col>
                            <v-col class="textContainer">
                                <p class="textShow">Peroid of Stay: {{ invoice.periodOfStay }}</p>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="textContainer">
                                <p class="textShow">Number of Room: {{ invoice.numberOfRoom }}</p>
                            </v-col>
                            <v-col class="textContainer">
                                <p class="textShow">Departure Date: {{ invoice.dateCheckOut }}</p>
                            </v-col>
                            <v-col class="textContainer">
                                <p class="textShow">Total: {{ invoice.total }}</p>
                            </v-col>
                        </v-row>
                    </v-card>
                </v-row>
            </v-card>
        </v-row>
        <v-row justify="center">
            <div class="btnContainer">
                <v-btn @click="onClickDone" :disabled="this.invoices.length === 0" style="width: 139px; height: 51px; background: #A0C6FF; border-radius: 30px;">
                    Done
                </v-btn>
            </div>
        </v-row>
        <!-- Add Invoice -->
        <v-dialog
          :value="modalAdd"
          persistent
          max-width="600"          
        >
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
                                :min="this.today"
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
                                :min="this.invoice.dateCheckIn"
                                no-title
                                @input="menuCheckOut = false"
                            ></v-date-picker>
                            </v-menu>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="3" offset="4">
                            <v-btn @click="onClickInvoiceCancel()" color="red" class="btnModal">
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
        <!-- Stepper -->
        <v-dialog 
            :value="modalStepper"
            persistent
            width="550"
        >
            <Stepper @close="onClickCancel" />
        </v-dialog>
    </v-container>
</template>

<script>
import Stepper from "../../components/addtions/Stepper"
export default {
  name: "HomeAdmin",
  components: {
    Stepper
  },
  mounted() {
    this.today = new Date().toISOString().substr(0, 10)
    const tomorrow = new Date(this.today)
    tomorrow.setDate(tomorrow.getDate() + 1)
    this.tomorrow = tomorrow.toISOString().substr(0, 10)
    this.invoice.dateCheckOut = tomorrow.toISOString().substr(0, 10)
  },
  data () {
    return {
        today: "",
        tomorrow: "",
        menuCheckIn: false,
        menuCheckOut: false,
        modalAdd: false,
        modalStepper: false,
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
        invoices: []
        };
    },
    methods: {
        onClickAdd() {
            this.modalAdd = true
        },
        onClickInvoiceCancel(){
            this.modalAdd = false
        },
        onClickCancel( value ) {
            this.modalStepper = value
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
                this.invoices.push(temp)
                this.counter = this.counter + 1
                this.modalAdd = false
            }
        },
        onClickDone() {
            this.modalStepper = true
            this.$store.commit("SET_INVOICES", this.invoices)
        }
    },
    computed:{
        checkState(){
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

.cardSelectContainer{
    margin-top: 20px;
    background-color: #A0C6FF;
    width:  200px;
    height: 100px;
    border: 2px solid black;
    border-radius: 20px;
    display: flex;
    justify-content: center;
}

</style>
