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
                              <label style="color:black; font-size:20px;">Familyname:</label>
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
                                  <p style="margin-top:16px">Add</p>
                              </v-btn>
                          </v-col>
                      </v-row>
                  </v-form>
                  <!-- Old User -->
                  <v-form
                      v-if="userModalState === '1'"
                      ref="formOldUser"
                      v-model="validOld"
                      @submit.prevent="submitAdd"
                      lazy-validation
                      style="width:500px;"
                  >
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
                        <v-btn color="#A0C6FF">
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
          <v-card
            class="mb-12"
            color="grey lighten-1"
            height="200px"
          ></v-card>

          <v-btn
            color="primary"
            @click="e1 = 3"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card
            class="mb-12"
            color="grey lighten-1"
            height="200px"
          ></v-card>

          <v-btn
            color="primary"
            @click="e1 = 1"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>


<script>
  export default {
    name: "Stepper",
    data () {
      return {
        step: 1,
        validNew: true,
        validOld: true,
        userModalState:"0",
        userNew:{
            firstname: "",
            familyname: "",
            phonenumber: "",
            email: "",
            passwrod: "",
        },
        userOld:{
            id: "",
            firstname: "",
            email: "",
        },
        emailRules: [
          v => !!v || "E-mail is required",
          v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ],
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
