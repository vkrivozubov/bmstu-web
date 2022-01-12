<template>
  <div id="app">
    <div class="topnav">
      <a class="active" href="/">Cars Aggregator</a>
      <a v-if="this.token == null && this.role == null" href="/login">Sign In</a>
      <a v-if="this.token == null && this.role == null" href="/register">Sign Up</a>
      <a v-if="this.token != null && this.role != null" v-on:click="logout()" href="/login" >Log out</a>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      token: null,
      role: null
    };
  },
  methods: {
      logout() {
          localStorage.removeItem('token');
          localStorage.removeItem('role');
          localStorage.removeItem('id');
      }
    },
  created() {
    this.token = localStorage.getItem('token');
    this.role = localStorage.getItem('role');
  },
  watch: {
    $route (to, from) {
      this.token = localStorage.getItem('token');
      this.role = localStorage.getItem('role');
    }
  }
};

</script>

<style>
.topnav {
  background-color: #000;
  overflow: hidden;
}

.topnav a {
  margin: 0px;
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #000;
  color: white;
}

</style>
