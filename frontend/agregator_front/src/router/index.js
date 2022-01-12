import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Dealerships from '@/components/Dealerships'
import DealershipForm from '@/components/DealershipForm'
import Cars from '@/components/Cars'
import CarForm from '@/components/CarForm'

const routes = [
  {
    path: '/dealerships/:id',
    name: 'Cars',
    component: Cars
  },
  {
    path: '/dealerships/car/new',
    name: 'CarForm',
    component: CarForm
  },
  {
    path: '/dealerships',
    name: 'Dealerships',
    component: Dealerships
  },
  {
    path: '/dealerships/new',
    name: 'DealershipForm',
    component: DealershipForm
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
