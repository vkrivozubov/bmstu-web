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
import ApiClient from '@/services/ApiClient'

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
            const client = new ApiClient();
            client.addCar(
                this.model,
                this.cost,
                this.dealership_id
            );
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
