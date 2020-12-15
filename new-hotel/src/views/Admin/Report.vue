<template>
    <v-container fluid class="main" id="Room">
        <v-row justify="center">
            <v-col style="margin-top:50px" cols="10">
                <v-card color="#A0C6FF" class="cardTitleContainer">
                    <v-row justify="center">
                        <v-col cols="5">
                            <v-btn
                                width="400"
                                @click="selectItem = 'Receipt'"
                            >
                                Receipt
                            </v-btn>
                        </v-col>
                        <v-col cols="5">
                            <v-btn
                                width="400"
                                @click="selectItem = 'Invoice'"
                            >
                                Invoice
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <!-- Table -->
        <v-row v-if="selectItem == 'Receipt'" style="margin-top:50px;" justify="center">
            <v-col cols="10">
                <v-data-table
                    :headers="headersReceipt"
                    :items="receipts"
                    class="elevation-1"
                >
                </v-data-table>
            </v-col>
        </v-row>
        <v-row v-if="selectItem == 'Invoice'" style="margin-top:50px;" justify="center">
            <v-col cols="10">
                <v-data-table
                    :headers="headers"
                    :items="rooms"
                    class="elevation-10"
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
      headersReceipt: [
        {
          text: 'Receipt ID',
          align: 'start',
          value: 'receiptID',
        },
        { text: 'Date Create', value: 'dateCreate' },
        { text: 'Name', value: 'name' },
        { text: 'Payment', value: 'paymentName' },
        { text: 'payment Reference', value: 'paymentRef' },
        { text: 'Remark', value: 'remark' },
        { text: 'Total Received', value: 'totalReceived' },
      ],
      receipts: [],
      invoices: [],
    }),
    async created () {
        this.initialize()
    },

    methods: {
      async initialize(){
        var resultReceipt = await api.summayReceipt()
        var resultInvoice = await api.summayInvoice()
        this.receipts = resultReceipt.data.result
        this.invoices = resultInvoice.data.result
        console.log(this.receipts)
        console.log(this.invoices)
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
