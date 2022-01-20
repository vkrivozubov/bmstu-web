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
import ApiClient from '@/services/ApiClient'
import Storage from '@/services/Storage'

export default {
  data() {
    return {
      dealerships: [],
      role: null,
      client: null,
      storage: null
    };
  },
  methods: {
    goToDealership(id) {
      this.$router.push('/dealerships/:'+id);
    },
    getDealerships() {
      this.client.fetchDealerships()
      .then((res) => {
          this.dealerships = res.data;
      })
      .catch((error) => {
          this.$router.push('/login');
      })
    },
    addDealership() {
        this.$router.push('/dealerships/new');
    },
    deleteDealership(id) {
        this.client.deleteDealership(id)
        .then((res) => {
          this.$router.push('/dealerships')
        })
    }
  },
  created() {
    const storage = new Storage(window.localStorage);
    this.role = storage.get('role');
    this.storage = storage;
    this.client = new ApiClient();
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