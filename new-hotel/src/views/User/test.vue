<p class="textDetail">Customer name : {{ this.user.firstName }} {{ this.user.familyName  }}</p>
              <p class="textDetail">Payment Method: {{ this.user.paymentMethod  }}</p>
              <div class="inputFiled" style="background-color:red">
                  <v-row>
                    <v-col cols="7" style="background-color:red">
                        <p>Credit card Number</p>
                    </v-col>
                    <v-col cols="5" style="background-color:red">
                        <v-text-field
                            ref="creaditNumber"
                            :rules="[v => !!v || 'Credit card Number is required']"
                            v-model="user.firtname"
                            solo
                            rounded
                            outlined
                            autocomplete="creaditNumber"
                        />                     
                    </v-col>
                  </v-row>
              </div>
              <p class="textDetail">CVV : {{ this.user.CVV }}</p>