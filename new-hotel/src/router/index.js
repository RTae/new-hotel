import Vue from 'vue'
import VueRouter from 'vue-router'
// Guest
import Home from '../views/User/Home'
import Login from '../views/User/Login'
import Signup from '../views/User/Signup.vue'
import Test from '../views/User/test.vue'
// Customer
import Profile from '../views/User/Login/Profile.vue'
import Invoice from '../views/User/Login/Invoice.vue'
import BookingHistory from '../views/User/Login/BookingHistory.vue'
import Receipt from '../views/User/Login/Receipt.vue'
import Booking from '../views/User/Login/Booking.vue'
import PaymentMethod from '../views/User/Login/PaymentMethod.vue'
// Admin
import HomeAdmin from '../views/Admin/HomeAdmin'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }, 
  {
    path: '/test',
    name: 'Test',
    component: Test
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
    path: "/invoice",
    name: "Invoice",
    component: Invoice
  },
  {
    path: "/bookinghistory",
    name: "BookingHistory",
    component: BookingHistory
  },
  {
    path: "/receipt",
    name: "Receipt",
    component: Receipt
  },
  {
    path: "/booking",
    name: "Booking",
    component: Booking
  },
  {
    path: "/paymentmethod",
    name: "PaymentMethod",
    component: PaymentMethod
  },
  {
    path: "/homeadmin",
    name: "HomeAdmin",
    component: HomeAdmin
  }
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
