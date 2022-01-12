<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Cars</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th class="left-th" scope="col">Model</th>
              <th class="center-th" scope="col">Cost/day($)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(car, index) in cars" :key="index">
              <td align="left" type="name">{{ car.model }}</td>
              <td align="center" type="cost">{{ car.cost }}</td>
              <td align="right">
                  <button v-if="this.role=='User' && car.is_available" class="button-rent" v-on:click="rentCar(car.id)" >Rent car</button>
                  <button v-if="this.role=='User' && !car.is_available" class="button-rent" v-on:click="rentCar(car.id)" >Unrent car</button>
              </td>
              <td align="right" v-if="this.role=='Dealer' && car.is_available">Available</td>
              <td align="right" v-if="this.role=='Dealer' && !car.is_available">Busy</td>
              <td align="right" v-if="this.role=='Dealer'">
                  <button v-if="this.role=='Dealer'" class="button-remove" v-on:click="deleteCar(car.id)" >-</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="row">
            <button class="button-add" v-if="this.role=='Dealer'" v-on:click="addCar()">+</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      cars: [],
      role: null,
      dealership_id: null
    };
  },
  methods: {
    rentCar(id) {
        const path = 'https://localhost/api/v1/cars/car/availabilty';
        var searching_car = null;
        for (const car of this.cars) {
            if (car.id == id) {
                searching_car = car;
            }
        }
        console.log(!searching_car.is_available);
        axios.patch(path,
            {
                car_id: id,
                is_available: !searching_car.is_available
            }, {
            headers: {
                'Authorization': `${localStorage.getItem('token')}`
            }
        })
        .then(response => {
            console.log("updated");
            var searching_car = null;
            for (const car of this.cars) {
                if (car.id == id) {
                    searching_car = car;
                }
            }
            searching_car.is_available = !searching_car.is_available
        })
        .catch(function (error) {
            console.error(error.response);
        });
    },
    addCar() {
        localStorage.setItem('dealership_id', this.dealership_id);
        this.$router.push('/dealerships/car/new');
    },
    deleteCar(id) {
        const path = 'https://localhost/api/v1/cars/car/'+id;
        let token = localStorage.getItem('token');
        axios.delete(path, {
            headers: {
                'Authorization': `${token}`
            }
        })
        .then((res) => {
            let new_cars = [];

            for (let i = 0; i < this.cars.length; i++) {
                if (this.cars[i].id != id) {
                    new_cars.push(this.cars[i]);
                }
            }

            this.cars = new_cars;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getCars(dealership_id) {
      axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      const path = 'https://localhost/api/v1/cars/'+ dealership_id;
      axios.get(path, {
          headers: {
            'Authorization': `${localStorage.getItem('token')}`
          }
      })
        .then((res) => {
          this.cars = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    let id = this.$route.params.id.replaceAll(':', '');
    this.role = localStorage.getItem('role');
    this.dealership_id = id
    this.getCars(id);
  },
};
</script>

<style>
.right-th {
    text-align: right;
}

.button-rent {
    background-color: black;
    border: black;
    border-radius: 8px;
}
</style>