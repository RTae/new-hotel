<template>
    <v-container fluid class="main" id="PrintPage">
        <v-overlay :value="$store.getters.getLoadingState">
              <v-progress-circular
                indeterminate
                size="64"
        ></v-progress-circular>
        </v-overlay>
        <v-row justify="center">
            <v-col cols="3">
                <v-text-field
                    label="Receipt ID"
                    v-model="receipt.receiptID"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field
                    label="Date Create"
                    v-model="receipt.dateCreate"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field
                    label="Total Received"
                    v-model="receipt.totalReceived"
                    readonly
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col cols="3">
                <v-text-field
                    label="Name"
                    v-model="receipt.name"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field
                    label="Phone Number"
                    v-model="receipt.phoneNumber"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field
                    label="Email"
                    v-model="receipt.email"
                    readonly
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col cols="3">
                <v-text-field
                    label="Payment Reference"
                    v-model="receipt.paymentRef"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field
                    label="Remark"
                    v-model="receipt.remark"
                    readonly
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-data-table
                    :headers="headers"
                    :items="receiptLine"
                    :items-per-page="5"
                    class="elevation-1"
                ></v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import api from "../../service/api"
  export default {
    name: "PrintPage",
    async mounted() {
        if (this.$route.query === undefined) {

        } else {
            this.$store.commit("SET_LOADING_STATE", true)
            var receiptID = this.$route.query.receiptID
            var result = await api.reportReceiptByReceiptID(receiptID)
            var resultLine = await api.reportReceiptLineByReceiptID(receiptID)
            this.receiptLine = resultLine.data.result
            this.receipt = result.data.result[0]
            this.receipt.name = this.receipt.firstname + " " + this.receipt.familyname
            this.$store.commit("SET_LOADING_STATE", false)
        }
    },
    data () {
      return {
        receipt:{},
        receiptLine:[],
        headers: [
          {
            text: 'Invoice ID',
            align: 'start',
            sortable: false,
            value: 'invoiceID',
          },
          { text: 'Room Type', value: 'roomType' },
          { text: 'Fare', value: 'fare' },
          { text: 'Number of Room', value: 'numberOfRoom' },
          { text: 'Period Of Stay', value: 'periodOfStay' },
          { text: 'Amount Due', value: 'amountDue' },
          { text: 'Check In', value: 'checkIn' },
          { text: 'Check Out', value: 'checkOut' },
        ],
      }
    },
  }
</script>

<style scoped>
.main {
    background-color: #FFFFFF;
    min-height: 100vh;
}
</style>
