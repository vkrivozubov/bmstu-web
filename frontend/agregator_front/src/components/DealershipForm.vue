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
import axios from 'axios';
export default {
    data() {
        return {
            name: "",
            description: ""
        }
    },
    methods: {
        handleAddNewDealership() {
            if (this.name.length > 0 && this.description.length > 0) {
                let user_id = localStorage.getItem('id');
                axios.post('https://localhost/api/v1/dealerships/dealership',
                    {
                        name: this.name,
                        description: this.description,
                        owner_id: user_id
                    }, {
                    headers: {
                        'Authorization': `${localStorage.getItem('token')}`
                    }
                }).catch(function (error) {
                    this.$router.push('/login');
                    console.error(error.response);
                });
            } else {
                this.name = "";
                this.description = "";
            }
        },
        goBack() {
            this.$router.push('/dealerships');
        }
    }
}
</script>

<style>

</style>
