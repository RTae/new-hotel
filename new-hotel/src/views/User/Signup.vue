<template>
  <v-container fluid class="main" id="signUp">
    <v-row class="bg">
    <v-toolbar
        src="../../../dist/img/mainFirst.svg"
        height="1000px"
        width="100vw"   
        flat
      >
      <v-row justify="center" align="center">
        <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer2">
          <v-row style="margin-top: 5vh" align="center" justify="center">
            <p class="textTitle">SIGN UP</p>
            </v-row>
            <v-row align="center" justify="center">
              <v-form
                ref="form"
                v-model="valid"
                @submit.prevent="submitRegister"
                lazy-validation
            >
                <!-- Name -->
                <v-row align="center" justify="center" style="margin-top: 3vh">
                <v-col>
                    <v-row class="ml-8" justify="start">
                    <label>First Name :</label>
                    </v-row>
                    <div class="inputFiled">
                    <v-text-field
                        ref="FirstName"
                        :rules="[v => !!v || 'Firstname is required']"
                        v-model="user.firstname"
                        solo
                        rounded
                        outlined
                        autocomplete="firstname"
                    />
                    </div>
                </v-col>
                <v-col>
                    <v-row class="ml-8" justify="start">
                    <label>Family Name :</label>
                    </v-row>
                    <div class="inputFiled">
                    <v-text-field
                        :rules="[v => !!v || 'Familyname is required!']"
                        v-model="user.familyname"
                        color="primary"
                        solo
                        rounded
                        outlined
                        autocomplete="familyname"
                    />
                    </div>
                </v-col>
                </v-row>

                <!-- Email -->
                <v-row align="center" justify="start">
                <v-col>
                    <v-row class="ml-8" justify="start">
                    <label>Email :</label>
                    </v-row>
                    <div class="inputFiled">
                    <v-text-field
                        solo
                        rounded
                        outlined
                        required
                        :rules="emailRules"
                        v-model="user.email"
                        autocomplete="email"
                    />
                    </div>
                </v-col>

                <!-- Phone Number -->

                <v-col>
                    <v-row class="ml-8" justify="start">
                    <label>Phone Number :</label>
                    </v-row>
                    <div class="inputFiled">
                    <v-text-field
                        :rules="[v => !!v || 'Phone number is required!']"
                        v-model="user.phone"
                        color="primary"
      
                        solo
                        rounded
                        outlined
                        autocomplete="phone"
                    />
                    </div>
                </v-col>
                </v-row>

                <!-- Password -->
                <v-row align="center" justify="start">
                <v-col col="6">
                    <v-row class="ml-8" justify="start">
                    <label class="">Password :</label>
                    </v-row>
                    <div></div>
                    <div class="inputFiled">
                    <v-text-field
                        solo
                        rounded
                        outlined
                        v-model="user.password"
                        :rules="passwordRules"
                        type="password"
                        autocomplete="password"
                    />
                    </div>
                </v-col>
                <v-col col="6">
                    <v-row class="ml-8" justify="start">
                    <label>Confirm Password :</label>
                    </v-row>
                    <div class="inputFiled">
                    <v-text-field
                        solo
                        rounded
                        outlined
                        :rules="passwordRules"
                        v-model="passwordCon"
                        type="password"
                        autocomplete="con-password"
                    />
                    </div>
                </v-col>
                </v-row>

                <!-- Button -->
               <v-row justify="center">
                <div class="text-center">
                  <v-dialog
                    v-model="dialog"
                    width="400px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        color="#47a7f5"
                        outlined
                        x-large
                        v-bind="attrs"
                        v-on="on"
                        :disabled="!valid" class="signUpBtn" type="submit"
                      >
                      Sigup
                      </v-btn>
                    </template>
              
                    <v-card>
                      <v-card-title class="cardTitle">
                        Successfully Register
                      </v-card-title>
                      <v-divider></v-divider>
              
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="primary"
                          text
                          @click="dialog = false"
                          block
                        >
                          Ok
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </div>
              </v-row> 
            </v-form>
          </v-row>
        </v-card>
      </v-row>
    </v-toolbar>  
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "signUp",
  data: () => ({
    dialog: false,
    valid: true,
    emailCon: "",
    passwordCon: "",
    user: {
      firtname: "",
      familyname: "",
      email: "",
      password: "",
      phonenumber: ""
    },
    passwordRules: [
      v => !!v || "Password is required",
      v => (v && v.length >= 6) || "Password must be more than 6 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    date: null,
    menu: false
  }),
  computed: {
  },
  methods: {
    async submitRegister () {
      this.$refs.FirstName.focus();
      var state = this.$refs.form.validate();
      if (this.user.email === this.emailCon) {
        if (this.user.password === this.passwordCon) {
          if (state) {
            this.eduTypeMapValue(this.eduValue)
            this.$store.dispatch({
              type: "doRegister",
              firstname: this.user.firstname,
              familyname: this.user.familyname,
              email: this.user.email,
              password: this.user.password,
              phonenumber: this.user.phonenumber
            });
          }
        } else {
          this.$store.dispatch({
            type: "dialogPopup",
            value: true,
            msg: "Password must be same"
          });
        }
      } else {
        this.$store.dispatch({
          type: "dialogPopup",
          value: true,
          msg: "Email must be same"
        });
      }
    }
  }
};
</script>

<style scoped>
.main {
  background: #C0D9FF;
  height: 1000px;
}
.cardContainer2 {
  color: #A0C6FF;
  border-radius: 20px;
  width: 1000px;
  height: 780px;

 }
.tectcondit {
  color: red;
}
.radioContainer {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  flex-direction: column;
}

.radioLineContainer {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  flex-direction: row;
}

.textTitle {
  font-size: 50px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 20px;
}

label {
  font-size: 18px;
  color: #5c5c5c;
  font-family: "Roboto";
  
}

.text_detail {
  margin-top: 20px;
  margin-right: 20px;
}

.text_detail2 {
  margin-top: 20px;
  margin-right: 20px;
  color: red;
}

.inputFiled {
  width: 375px;
  height: 32px;
  margin-top: 20px;
  margin-left: 20px;
  margin-right: 20px;
  margin-bottom: 35px;
}

.signUpBtn {
  background-color: white;
  background-position: center;
  font-family: "Roboto";
  border-radius: 100px;
  margin-right: 20px;
  width: 130px;
  height: 45px;
  opacity: 1;
  transition: 0.3s;
  font-size: 15px;
  text-transform: uppercase;
  color: #47a7f5;
  box-shadow: 0 0 4px #999;
  cursor: pointer;
  outline: none;
  margin-top: 50px;
}

.signUpBtn:hover {
  background: #C0D9FF radial-gradient(circle, transparent 1%, #47a7f5 1%)
    center/15000%;
}

.signUpBtn:active {
  background-color: #6eb9f7;
  color: white;
  background-size: 100%;
  transition: background 0s;
}
.cardTitle{
  background-color:#6eb9f7;
  width:400px;
  height:100px;
  size:40px;
  display: flex;
  justify-content: center;
}
</style>
