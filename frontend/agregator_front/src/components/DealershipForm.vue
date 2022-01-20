<template>
    <div type="login">
        <h4 class="h">New dealership</h4>
        <form>
            <label for="name">Name</label>
            <div>
                <input type="username" v-model="name" required autofocus>
            </div>
            <div>
                <label for="password">Description</label>
                <div>
                    <input type="username" v-model="description" required>
                </div>
            </div>
            <div>
                <button class="button3" @click="handleAddNewDealership()">
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
            name: "",
            description: ""
        }
    },
    methods: {
        handleAddNewDealership() {
            const client = new ApiClient();
            client.addDealership(
                this.name,
                this.description,
            )
            .catch(function (error) {
                this.$router.push('/login');
            });
        },
        goBack() {
            this.$router.push('/dealerships');
        }
    }
}
</script>

<style>

</style>
