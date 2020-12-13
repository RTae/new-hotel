<template>
 <v-container fluid class="main" id="login">
    <v-row class="bg">
      <v-toolbar
        src="../../../dist/img/mainFirst.svg"
        height="800px"
        width="100vw"   
        flat
      >
        <v-row justify="center" align="center">
          <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer" >
            <v-row style="margin-top: 10vh" align="center" justify="center">
              <p class="textTitle">LOGIN</p>
            </v-row>
            <v-row align="center" justify="center">
              <v-form
                ref="form"
                v-model="valid"
                @submit.prevent="submit"
                lazy-validation
              >
                <!-- Username field -->
                <div class="input_button">
                  <v-text-field
                    color="primary"
                    solo
                    rounded
                    outlined
                    v-model="account.email"
                    required
                    autocomplete="username"
                    :rules="emailRules"
                    placeholder="Email"
                    name="email"
                  />
                </div>
                <!-- Password field -->
                <div class="input_button">
                  <v-text-field
                    solo
                    rounded
                    outlined
                    placeholder="Password"
                    required
                    min="9"
                    autocomplete="password"
                    :rules="passwordRules"
                    v-model="account.password"
                    :type="showPassword ? 'text' : 'password'"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = !showPassword"
                    name="password"
                  />
                </div>

                <!-- ETC -->
                <v-row justify="center">
                  <p style="margin-right: 10px" class="text">Don't have an account?</p>
                  <router-link to="/signup">
                    <p class="text" style="color:red;">Sign up</p>
                  </router-link>
                </v-row>

                <!-- Button -->
                <v-row justify="center">
                  <button :disabled="!valid" class="signInBtn" type="submit">Sign In</button>
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
  name: "login",
  data () {
    return {
      showPassword: false,
      account: {
        email: "",
        password: ""
      },
      valid: true,
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => (v && v.length >= 6) || "Password must be more than 6 characters"
      ],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ]
    };
  },
  methods: {
    submit () {
      var state = this.$refs.form.validate();
      if (state) {
        this.$store.dispatch({
          type: "doLogin",
          email: this.account.email,
          password: this.account.password
        })
      }
    }
  }
};
</script>

<style scoped>
.main {
  background: #C0D9FF;
}

.cardContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 900px;
  height: 600px;
  margin-top: 1vh;
 }
 
.input_button {
  width: 423px;
  height: 60px;
  margin: 20px;
}

.textTitle {
  font-size: 50px;
  color: #FFFFFF;
  font-family: "Roboto";
  margin-top: 20px;
}

.text {
  font-size: 12px;
  font-family: "Roboto";
}

.signInBtn {
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

.signInBtn:hover {
  background: #C0D9FF radial-gradient(circle, transparent 1%, #47a7f5 1%)
    center/15000%;
}

.signInBtn:active {
  background-color: #6eb9f7;
  color: white;
  background-size: 100%;
  transition: background 0s;
}

</style>
