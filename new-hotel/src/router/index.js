import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/User/Home'
import Login from '../views/User/Login'
import Profile from '../views/User/Login/Profile.vue'
import Payment from '../views/User/Login/Payment.vue'
import Signup from '../views/User/Signup.vue'
import BookingHistory from '../views/User/Login/BookingHistory.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup
  },
  {
    path: "/payment",
    name: "Payment",
    component: Payment
  },
  {
    path: "/bookinghistory",
    name: "BookingHistory",
    component: BookingHistory
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
