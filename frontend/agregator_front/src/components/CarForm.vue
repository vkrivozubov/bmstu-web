<template>
    <div type="login">
        <h4 class="h">New car</h4>
        <form>
            <label for="name">Model</label>
            <div>
                <input type="username" v-model="model" required autofocus>
            </div>
            <div>
                <label for="password">Cost</label>
                <div>
                    <input type="username" v-model="cost" required>
                </div>
            </div>
            <div>
                <button class="button3" @click="handleAddNewCar()">
                    Add
                </button>
            </div>
            <div>
                <button class="button3" @click="goBack()">
                    Back
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            model: "",
            cost: "",
            dealership_id: ""
        }
    },
    methods: {
        handleAddNewCar() {
            if (this.model.length > 0 && this.cost.length > 0) {
                axios.post('https://localhost/api/v1/cars/car',
                    {
                        model: this.model,
                        cost: this.cost,
                        dealership_id: this.dealership_id
                    }, {
                    headers: {
                        'Authorization': `${localStorage.getItem('token')}`
                    }
                })
                .catch(function (error) {
                    console.error(error.response);
                });
            } else {
                this.model = "";
                this.cost = "";
            }
        },
        goBack() {
            this.$router.push('/dealerships/'+this.dealership_id);
        }
    },
    created() {
        this.dealership_id = localStorage.getItem('dealership_id');
    }
}
</script>

<style>

</style>
