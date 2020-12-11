<template>
  <v-container fluid class="main" id="signUp">
    <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer2">
        <v-row style="margin-top: 10vh" align="center" justify="center">
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
            <v-row align="center" justify="center">
            <v-col>
                <v-row class="ml-8" justify="start">
                <label>First Name :</label>
                </v-row>
                <div class="inputFiled">
                <v-text-field
                    ref="FirstName"
                    :rules="[v => !!v || 'Firstname is required']"
                    v-model="user.firtname"
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
            <v-col>
                <v-row class="ml-8" justify="start">
                <label>Phone Number :</label>
                </v-row>
                <div class="inputFiled">
                <v-text-field
                    solo
                    rounded
                    outlined
                    required
                    :rules="emailRules"
                    v-model="user.phone"
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
            <button :disabled="!valid" class="signUpBtn" type="submit">
                Sign Up
            </button>
            </v-row>
        </v-form>
        </v-row>
    </v-card>
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
      role: "",
      sex: "",
      firtname: "",
      familyname: "",
      birthday: null,
      edu: "",
      email: "",
      password: ""
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
  watch: {
    menu (val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  },
  computed: {
  },
  methods: {
    eduTypeMapValue (eduName) {
      Object.values(this.eduType).forEach(value => {
        if (value.name === eduName) {
          this.user.edu = value.id
        }
      });
    },
    save (date) {
      this.$refs.menu.save(date);
    },
    async submitRegister () {
      this.$refs.FirstName.focus();
      var state = this.$refs.form.validate();
      if (this.user.email === this.emailCon) {
        if (this.user.password === this.passwordCon) {
          if (state) {
            this.eduTypeMapValue(this.eduValue)
            this.$store.dispatch({
              type: "doRegister",
              firtname: this.user.firtname,
              familyname: this.user.familyname,
              birthday: this.user.birthday,
              sex: this.user.sex,
              email: this.user.email,
              password: this.user.password,
              role: this.user.role,
              edu: this.user.edu
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

<style scope>
.cardContainer2 {
  color: #A0C6FF;
  border-radius: 20px;
  width: 900px;
  height: 650px;
  margin-top: 8vh;
  margin-left: 250px;
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
  font-weight: bold;
  font-size: 15px;
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
  background-color: #5cbbf6;
  background-position: center;
  font-family: "Average Sans", sans-serif;
  border-radius: 100px;
  margin-right: 20px;
  width: 130px;
  height: 45px;
  opacity: 1;
  transition: 0.3s;
  font-size: 13px;
  text-transform: uppercase;
  color: white;
  box-shadow: 0 0 4px #999;
  cursor: pointer;
  outline: none;
  margin-top: 50px;
}

.signUpBtn:hover {
  background: #47a7f5 radial-gradient(circle, transparent 1%, #47a7f5 1%)
    center/15000%;
}

.signUpBtn:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}
</style>
