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
import ApiClient from '@/services/ApiClient'
import Storage from '@/services/Storage'

export default {
  data() {
    return {
      cars: [],
      role: null,
      dealership_id: null,
      client: new ApiClient(),
      storage: new Storage(window.localStorage)
    };
  },
  methods: {
    rentCar(id) {
        this.client.changeCarAvailability(
          id,
          this.cars
        );
    },
    addCar() {
        this.storage.set('dealership_id', this.dealership_id);
        this.$router.push('/dealerships/car/new');
    },
    deleteCar(id) {
        // тут можно добавить промежуточный слой с логикой, который будеть стучаться в ApiClient, но того не стоит
        this.client.deleteCar(id)
        .then((res) => {
            let new_cars = [];
            for (let i = 0; i < this.cars.length; i++) {
                if (this.cars[i].id != id) {
                    new_cars.push(this.cars[i]);
                }
            }
            this.cars = new_cars;
        });
    },
    getCars(dealership_id) {
      this.client.fetchCars(dealership_id)
      .then((res) => {
          this.cars = res.data;
      });
    },
  },
  created() {
    let id = this.$route.params.id.replaceAll(':', '');
    this.role = this.storage.get('role');
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