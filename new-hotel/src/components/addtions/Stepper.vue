<template>
  <div name="Stepper" id="Stepper">
    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step
          :complete="step > 1"
          step="1"
        >
          Customer Detail
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="step > 2"
          step="2"
        >
          Payment Detail
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">
          Summary
        </v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card class="cardModalContainer">
            <v-row justify="center">
                <div class="cardSelectContainer">
                    <v-radio-group
                        column
                        v-model="userModalState"
                        class="d-flex justify-center align-center"
                    >
                      <v-radio
                          color="black"
                          label="New user"
                          value="0"
                      />
                      <v-radio
                          color="black"
                          label="Exist User"
                          value="1"
                      />
                    </v-radio-group>
                </div>
            </v-row>
            <v-row>
              <!-- New User -->
              <v-form
                  v-if="userModalState === '0'"
                  ref="formNewUser"
                  v-model="validNew"
                  @submit.prevent="submitUser"
                  lazy-validation
                  style="width:500px;"
              > 
                <v-overlay :value="$store.getters.getLoadingState">
                  <v-progress-circular
                    indeterminate
                    size="64"
                  ></v-progress-circular>
                </v-overlay>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">First name:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="[v => !!v || 'Item is required']"
                            dense
                            v-model=userNew.firstname
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">Family name:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="[v => !!v || 'Item is required']"
                            dense
                            v-model=userNew.familyname
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">Email:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="[v => !!v || 'Item is required']"
                            dense
                            v-model=userNew.email
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">Phone number:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="[v => !!v || 'Item is required']"
                            dense
                            v-model=userNew.phonenumber
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">Password:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="[v => !!v || 'Item is required']"
                            dense
                            v-model=userNew.passwrod
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3" offset="4">
                        <v-btn @click="onClickCancelUser()" color="red" class="btnModal">
                            <p style="margin-top:16px">Cancel</p>
                        </v-btn>                        
                    </v-col>
                    <v-col cols="3" offset="1">
                        <v-btn type="submit" color="#A0C6FF" class="btnModal">
                            <p style="margin-top:16px">Confirm</p>
                        </v-btn>
                    </v-col>
                </v-row>
              </v-form>
              <!-- Old User -->
              <v-form
                  v-if="userModalState === '1'"
                  ref="formOldUser"
                  v-model="validOld"
                  @submit.prevent="submitNew"
                  lazy-validation
                  style="width:500px;"
              >
                <v-overlay :value="$store.getters.getLoadingState">
                  <v-progress-circular
                    indeterminate
                    size="64"
                  ></v-progress-circular>
                </v-overlay>
                <v-row>
                    <v-col cols="4" offset="1">
                        <label style="color:black; font-size:20px;">Email:</label>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field
                            :rules="emailRules"
                            dense
                            v-model=userOld.email
                        />
                    </v-col>
                </v-row>
                <v-row class="d-flex justify-end align-center mr-10">
                    <v-btn :disable="validOld" @click="search()" color="#A0C6FF">
                        <p style="margin-top:16px">Search</p>
                    </v-btn>
                </v-row>
                <v-row justify="center">
                    <p style="font-size:20px"> Customer ID: {{ userOld.id }}</p>
                </v-row>
                <v-row>
                    <v-col cols="3" offset="4">
                        <v-btn @click="onClickCancelUser()" color="red" class="btnModal">
                            <p style="margin-top:16px">Cancel</p>
                        </v-btn>                        
                    </v-col>
                    <v-col cols="3" offset="1">
                        <v-btn type="submit" color="#A0C6FF" class="btnModal">
                            <p style="margin-top:16px">Confirm</p>
                        </v-btn>
                    </v-col>
                </v-row>
              </v-form>
            </v-row>
          </v-card>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-form
            ref="formReceipt"
            @submit.prevent="submitReceipt"
            lazy-validation
          >
            <v-overlay :value="$store.getters.getLoadingState">
              <v-progress-circular
                indeterminate
                size="64"
              ></v-progress-circular>
            </v-overlay>
            <v-card >
              <v-row>
                <v-col>
                  <v-text-field
                    label="Total"
                    v-model=receiptTotal
                    readonly
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-text-field
                    label="Customer Name"
                    v-model=$store.getters.getCustomer.firstname
                    readonly
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-select
                    label="Payment medthod"
                    :items="paymentMedthod"
                    v-model=paymentReceipt.paymentMedthod
                  />
                </v-col>
              </v-row>
              <v-row v-if="paymentReceipt.paymentMedthod == 'Credit Card'" class="d-flex flex-column">
                <v-row justify="center">
                  <v-col cols="11">
                    <v-text-field
                    placeholder="Credit Card Number"
                    v-model=paymentReceipt.creditCard
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row justify="center">
                  <v-col cols="11">
                    <v-text-field
                    placeholder="CVV"
                    v-model=paymentReceipt.cvv
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-row>
              <v-row>
                <v-col>
                  <v-text-field
                    placeholder="Payment Reference"
                    v-model=paymentReceipt.paymentRef
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-text-field
                    placeholder="Remark"
                    v-model=paymentReceipt.remark
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="3" offset="7">
                    <v-btn type="submit" color="#A0C6FF" class="btnModal">
                        <p style="margin-top:16px">Confirm</p>
                    </v-btn>
                </v-col>
              </v-row>
            </v-card>
          </v-form>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card >
            <v-row>
              <v-col>
                <v-text-field
                  label="Total"
                  v-model=receiptTotal
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  label="Customer Name"
                  v-model=$store.getters.getCustomer.firstname
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  label="Payment medthod"
                  v-model=paymentReceipt.paymentMedthod
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  placeholder="Payment Reference"
                  v-model=paymentReceipt.paymentRef
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  placeholder="Remark"
                  v-model=paymentReceipt.remark
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" offset="2">
                <v-btn @click="onClickPrint()" color="#A0C6FF" class="btnModal">
                    <p style="margin-top:16px">Print</p>
                </v-btn>
              </v-col>
              <v-col cols="3" offset="2">
                <v-btn @click="onClicklastStep()" color="#A0C6FF" class="btnModal">
                    <p style="margin-top:16px">Done</p>
                </v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>


<script>
import api from "../../service/api"
export default {
  name: "Stepper",
  data () {
    return {
      step: 1,
      validReceipt: true,
      validNew: true,
      validOld: true,
      userModalState:"0",
      receiptTotal: 0,
      receiptID: "",
      paymentMedthod: ["Cash", "Credit Card"],
      invoicesID: [],
      paymentMedthodObject: [
        {
          id: "1",
          name: "Cash"
        },
        {
          id: "2",
          name: "Credit Card"
        },
      ],
      userNew:{
          firstname: "",
          familyname: "",
          phonenumber: "",
          email: "",
          passwrod: "",
      },
      userOld:{
          id: "",
          email: "",
      },
      paymentReceipt:{
        total: "",
        name:"",
        paymentMedthod:"Cash",
        creditCard: "",
        cvv: "",
        paymentRef:"",
        remark:"",
      },
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
    }
  },
  methods: {
    onClickCancelUser() {
      this.$emit('close', false)
    },
    async submitUser() {
      var state = this.$refs.formNewUser.validate();
      if (state){
        this.$store.commit("SET_LOADING_STATE", true)
        var resultRegis = await api.register({
          firstname: this.userNew.firstname,
          familyname: this.userNew.familyname,
          email: this.userNew.email,
          phoneNumber: this.userNew.phonenumber,
          creditCardNumber: "11",
          point: "100",
          password: this.userNew.passwrod 
        })
        var total = 0
        var invoices = this.$store.getters.getInvices
        var customerID = resultRegis.result
        var resultCustomer = await api.getCustomer(customerID)
        this.$store.commit("SET_CUSTOMER", resultCustomer.data.result)
        for(var i = 0; i < invoices.length; i++){
          var invoice = invoices[i]
          var now = new Date().toISOString().substr(0, 10)
          var resultInvoice = await api.createInvoice({
              roomCatID: invoice.typeID,
              customerID: customerID,
              dateCreate: now,
              total: invoice.total,
              vat: invoice.total*0.07,
              checkIn: invoice.dateCheckIn,
              checkOut: invoice.dateCheckOut,
              numberOfRoom: invoice.numberOfRoom
            })
          var invoiceID = resultInvoice.result
          var roomResult = await api.roomFree(invoice.typeID, invoice.numberOfRoom)
          var rooms = roomResult.data
          for(var j = 0; j < rooms.length; j++){
            await api.updateRoom({
              roomID: rooms[j].roomID,
              roomCatID: rooms[j].roomCatID,
              status: "0",
              cleanStatus: "1",
            })
            await api.createInvoiceLine({
              invoiceID: invoiceID,
              roomID: rooms[j].roomID,
              remark: "test"
            })
          }
          total = total + (invoice.total + invoice.total*0.07)
          this.invoicesID.push(invoiceID)
        }
        this.receiptTotal = total
        this.$store.commit("SET_LOADING_STATE", false)
        this.step = 2
      }
    },
    async submitNew() {
      var state = this.$refs.formOldUser.validate();
      if (state && this.userOld.id !== "User not found") {
        var total = 0
        this.$store.commit("SET_LOADING_STATE", true)
        var invoices = this.$store.getters.getInvices
        for(var i = 0; i < invoices.length; i++){
          var invoice = invoices[i]
          var now = new Date().toISOString().substr(0, 10)
          var resultInvoice = await api.createInvoice({
              roomCatID: invoice.typeID,
              customerID: this.$store.getters.getCustomer.customerID,
              dateCreate: now,
              total: invoice.total,
              vat: invoice.total*0.07,
              checkIn: invoice.dateCheckIn,
              checkOut: invoice.dateCheckOut,
              numberOfRoom: invoice.numberOfRoom
            })
          var invoiceID = resultInvoice.result
          var roomResult = await api.roomFree(invoice.typeID, invoice.numberOfRoom)
          var rooms = roomResult.data
          for(var j = 0; j < rooms.length; j++){
            await api.updateRoom({
              roomID: rooms[j].roomID,
              roomCatID: rooms[j].roomCatID,
              status: "0",
              cleanStatus: "1",
            })
            await api.createInvoiceLine({
              invoiceID: invoiceID,
              roomID: rooms[j].roomID,
              remark: "test"
            })
          }
          total = total + (invoice.total + invoice.total*0.07)
          this.invoicesID.push(invoiceID)
        }
        this.receiptTotal = total
        this.$store.commit("SET_LOADING_STATE", false)
        this.step = 2
      }
    },
    async search() {
      this.$store.commit("SET_LOADING_STATE", true)
      const result =  await api.search(this.userOld.email)
      if (result.data.status == "1") {
        this.userOld.id =  result.data.result.customerID
        this.$store.commit("SET_CUSTOMER", result.data.result)
      } else {
        this.userOld.id = result.data.msg
      }
      this.$store.commit("SET_LOADING_STATE", false)
    },
    async submitReceipt() {
      this.$store.commit("SET_LOADING_STATE", true)
      const paymentMedthod = this.paymentMedthodObject.find( ({ name }) => name === this.paymentReceipt.paymentMedthod );
      const resultReceipt = await api.createReceipt({
        customerID: this.$store.getters.getCustomer.customerID,
        paymentMedId: paymentMedthod.id,
        cuponID: "co0001",
        dateCreate: new Date().toISOString().substr(0, 10),
        paymentRef: this.paymentReceipt.paymentRef,
        totalReceived: this.receiptTotal,
        remark: "Test"
      })
      var receiptID = resultReceipt.result
      this.receiptID = receiptID
      for(var i = 0; i < this.invoicesID.length; i++){
        var invoiceID = this.invoicesID[i]
        const result = await api.createReceiptLine({
          receiptID: receiptID,
          invoiceID: invoiceID,
          remark: "Test"
        })
      }
      this.$store.commit("SET_LOADING_STATE", false)
      this.step = 3
    },
    onClicklastStep() {
      this.step = 1
      this.onClickCancelUser()
    }
  },
}
</script>

<style scoped>
.cardModalContainer{
    min-width: 20vw;
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
