<template>
  <v-container fluid class="main" id="login">
    <v-card style="background-color:#A0C6FF; border-radius: 20px;" class="cardContainer">
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
              <p style="color:#FFFFFF" class="text">Sign up</p>
            </router-link>
          </v-row>

          <!-- Button -->
          <v-row justify="center">
            <button :disabled="!valid" class="signInBtn" type="submit">Sign In</button>
          </v-row>

        </v-form>
      </v-row>
    </v-card>

      <!-- Image -->
      <div class="d-flex flex-column justify-bottom align-center">
        <v-img
          alt="bitButton"
          contain
          style="margin-top: 100px"
          width="1290"
        />
      </div>

      <!-- Dialog -->
      <v-dialog v-model="$store.getters.getDialogState" width="500">
        <v-card>
          <v-card-title class="primary mb-6"> Alert </v-card-title>
          <v-card-text class="popUpText">
            {{ $store.getters.getDialogMsg }}
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="
                $store.dispatch({ type: 'dialogPopup', value: false, msg: '' })
              "
            >
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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

<style scope>
.main {
  background: rgb(239, 239, 239);
  min-height: 100vh;
}

.cardContainer {
  color: #A0C6FF;
  border-radius: 20px;
  width: 900px;
  height: 500px;
  margin-top: 15vh;
  margin-left: 250px;
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
  background-color: #C4C4C4;
  background-position: center;
  font-family: "Roboto";
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

.signInBtn:hover {
  background: #989191
    radial-gradient(circle, transparent 1%, #989191 1%) center/15000%;
}
.signInBtn:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}

.popUpText {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
}

</style>
