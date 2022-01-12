<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Dealerships</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th class="left-th" scope="col">Dealership</th>
              <th class="center-th" scope="col">Info</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(dealership, index) in dealerships" :key="index"
            @click="goToDealership(dealership.id)">

              <td type="name">{{ dealership.name }}</td>
              <td align="center" type="description">{{ dealership.description }}</td>
              <td align="right">
                  <button v-if="this.role=='Dealer'" class="button-remove" v-on:click="deleteDealership(dealership.id)" >-</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="row">
            <button class="button-add" v-if="this.role=='Dealer'" v-on:click="addDealership()">+</button>
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
      dealerships: [],
      role: null
    };
  },
  methods: {
    goToDealership(id) {
      console.log(id);
      this.$router.push('/dealerships/:'+id);
    },
    getDealerships() {
      const path = 'https://localhost/api/v1/dealerships';
      console.log(localStorage.getItem('token'));
      let token = localStorage.getItem('token');
      if (token != null) {
        console.log(localStorage.getItem('token'));
        axios.get(path, {
            headers: {
                'Authorization': `${token}`
            }
        })
            .then((res) => {
                this.dealerships = res.data;
            })
            .catch((error) => {
                localStorage.removeItem('token');
                localStorage.removeItem('role');
                localStorage.removeItem('id');
                this.$router.push('/login');
                console.error(error);
            });
      }
    },
    addDealership() {
        this.$router.push('/dealerships/new');
    },
    deleteDealership(id) {
        const path = 'https://localhost/api/v1/dealerships/'+id;
        let token = localStorage.getItem('token');
        if (token != null) {
        axios.delete(path, {
            headers: {
                'Authorization': `${token}`
            }
        })
            .then((res) => {
                this.$router.push('/dealerships')
            })
            .catch((error) => {
            console.error(error);
            });
      }
    }
  },
  created() {
    this.role = localStorage.getItem('role')
    this.getDealerships();
  },
};
</script>

<style>
.row {
    justify-content: center;
    margin-left: 0;
    margin-right: 0;
}

div.row {
    --bs-gutter-x: 0;
}

tbody {
  color: #000;
  text-decoration: none;
}

a {
  color: #000;
    text-decoration: none;
}

.button-add {
    background-color: green;
    border: green;
    border-radius: 8px;
    display: flex;
    justify-content: center;
}

.button-remove {
    background-color: red;
    border: red;
    border-radius: 8px;
}

tr {
    vertical-align: middle;
    border-color: black;
}

.left-th {
    text-align: left;
}

.center-th {
    text-align: center;
}

</style>