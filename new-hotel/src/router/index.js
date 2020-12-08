import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/User/Home'
import Login from '../views/User/Login'
import Profile from '../views/User/Profile'


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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
