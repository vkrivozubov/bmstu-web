"use strict";

import AxiosWrapper from '@/services/AxiosWrapper'
import Storage from '@/services/Storage'

export default class APIClient {
    constructor() { 
        this.storage = new Storage(window.localStorage);
    }

    login(username, password) {
        const wrapper = new AxiosWrapper('https://localhost/api/v1/users/login');
        if (password.length > 0) {
            return Promise.resolve(
                wrapper.post({
                    username: username,
                    password: password
                })
                .then(response => {
                    let data = response.data;
                    this.storage.set('token', data.token);
                    this.storage.set('role', data.role);
                    this.storage.set('id', data.id);
                })
                .catch(function (error) {
                    console.error(error.response);
                    return Promise.reject(error);
                })
            )
        } else {
            return Promise.reject("Password is necessary!");
        }
    }

    register(username, password, role) {
        const wrapper = new AxiosWrapper('https://localhost/api/v1/users/user');
        if (password.length > 0) {
            return Promise.resolve(
                wrapper.post({
                    username: username,
                    password: password,
                    role: role
                })
                .then(response => {
                    let data = response.data;
                    this.storage.set('token', data.token);
                    this.storage.set('role', data.role);
                    this.storage.set('id', data.id);
                })
                .catch(function (error) {
                    console.error(error.response);
                    return Promise.reject(error);
                })
            )
        } else {
            return Promise.reject("Password is necessary!");
        }
    }

    fetchDealerships() {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/dealerships');
        return Promise.resolve(
            wrapper.get(token)
            .catch((error) => {
                this.storage.clear();
                console.error(error);
                return Promise.reject(error);
            })
        );
    }

    addDealership(name, description) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/dealerships/dealership');
        if (name.length > 0 && description.length > 0) {
            let user_id = this.storage.get('id');
            return Promise.resolve(
                wrapper.post({
                    name: name,
                    description: description,
                    owner_id: user_id
                }, token)
                .catch(function (error) {
                    console.error(error.response);
                })
            )
        } else {
            return Promise.reject("Please, input data");
        }
    }

    deleteDealership(id) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/dealerships/' + id);
        return Promise.resolve(
            wrapper.delete(token)
            .catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }

    fetchCars(dealership_id) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/cars/'+ dealership_id);
        return Promise.resolve(
            wrapper.get(token)
            .catch((error) => {
                console.error(error);
            })
        )
    }

    addCar(model, cost, dealership_id) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/cars/car');
        if (model.length > 0 && cost.length > 0) {
            return Promise.resolve(
                wrapper.post({
                    model: model,
                    cost: cost,
                    dealership_id: dealership_id
                }, token)
                .catch(function (error) {
                    console.error(error.response);
                })
            )
        } else {
            return Promise.reject("Please, input data");
        }
    }

    deleteCar(id) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/cars/car/'+id);
        return Promise.resolve(
            wrapper.delete(token)
            .catch((error) => {
              console.error(error);
            })
        );
    }

    changeCarAvailability(id, cars) {
        const token = this.storage.get('token');
        const wrapper = new AxiosWrapper('https://localhost/api/v1/cars/car/availabilty');
        var searching_car = null;
        for (const car of cars) {
            if (car.id == id) {
                searching_car = car;
            }
        }
        return Promise.resolve(
            wrapper.patch({
                car_id: id,
                is_available: !searching_car.is_available
            }, token)
            .then(response => {
                var searching_car = null;
                for (const car of cars) {
                    if (car.id == id) {
                        searching_car = car;
                    }
                }
                searching_car.is_available = !searching_car.is_available
            })
            .catch(function (error) {
                console.error(error.response);
            })
        )
    }
}

