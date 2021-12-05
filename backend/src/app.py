from flask import Flask, request
from flask.json import jsonify
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from repository_fabruque import RepositoryFabrique
from marshmallow import*
from swagger_ui import api_doc
from Domain.user import*
from Domain.dealership import*
from Domain.car import*
import argparse

app = Flask(__name__)

fabrique = None
user_repository = None
dealership_respository = None
car_repository = None

api_doc(app, config_path='../config/swagger.yaml', url_prefix='/api/doc', title='API doc')

spec = APISpec(
    title="flask-api-swagger-doc",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

def send_error(error_code):
    message = "Unknown"
    if error_code == 400:
        message = "Invalid request"
    else:
        message = "Internal error"

    error = {
        'status': f'{error_code}',
        'message': message
    }

    return jsonify(error), error_code


def send_ok():
    response = {
        'status': '200',
        'message': "OK"
    }
    return jsonify(response), 200

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/api/user", methods=['POST'])
def register_user():
    req = request.json
    if not req or not 'username' in req or not 'password' in req or not 'role' in req:
        return send_error(400)

    new_user_domain = User(
        req['username'],
        req['password'],
        req['role']
    )
    users = user_repository.get_all_users()
    
    for user in users:
        if user.username == new_user_domain.username:
            return send_error(400)
    
    user_repository.add_new_user(new_user_domain)

    return send_ok()

@app.route("/api/user/login", methods=['POST'])
def login_user():
    req = request.json
    if not req or not 'username' in req or not 'password' in req:
        return send_error(400)

    users = user_repository.get_all_users()
    username = req['username']
    password = req['password']

    for user in users:
        if user.username == username:
            if user.password == password:
                return send_ok()
            else:
                return send_error(400)

    return send_error(400)

@app.route("/api/dealership/dealerships", methods=['GET'])
def get_dealerships():
    dealerships = dealership_respository.get_dealerships()
    
    DTO_dealerships = []
    converter = DealershipDomainToDTOConverter()

    for dealer in dealerships:
        DTO_dealerships.append(converter.convert(dealer).get_dict())

    return jsonify(DTO_dealerships), 200

@app.route("/api/dealership", methods=['POST'])
def create_dealership():
    req = request.json
    if not req or not 'name' in req or not 'description' in req or not 'owner_id' in req:
        return send_error(400)

    new_dealership_domain = Dealership(
        None,
        req['name'],
        req['description'],
        req['owner_id']
    )

    dealerships = dealership_respository.get_dealerships()

    for dealer in dealerships:
        if dealer.name == new_dealership_domain.name:
            return send_error(400)

    try:
        dealership_respository.create_dealership(new_dealership_domain)
    except:
        return send_error(500)

    return send_ok()


@app.route("/api/dealership/<int:id>", methods=['DELETE'])
def delete_dealership(id):
    try:
        dealership_respository.remove_dealership(id)
    except:
        return send_error(500)

    return send_ok()

@app.route("/api/car/cars/<int:dealership_id>", methods=['GET'])
def get_cars_for_dealership(dealership_id):
    cars = car_repository.get_cars(dealership_id)

    converter = CarDomainToDTOConverter()
    DTO_cars = []

    for car in cars:
        DTO_cars.append(converter.convert(car).get_dict())

    return jsonify(DTO_cars), 200

@app.route("/api/car/<int:id>", methods=['DELETE'])
def delete_car(id):
    try:
        car_repository.delete_car(id)
    except:
        return send_error(500)

    return send_ok()

@app.route("/api/car", methods=['POST'])
def create_car():
    req = request.json
    if not req\
        or not 'model' in req\
        or not 'cost' in req\
        or not 'dealership_id' in req:
        return send_error(400)

    new_car_domain = Car(
        None,
        req['model'],
        req['cost'],
        req['dealership_id'],
        True
    )

    try:
        car_repository.create_car(new_car_domain)
    except:
        return send_error(500)
    
    return send_ok()

@app.route("/api/car/availabilty", methods=['PATCH'])
def change_car_availability():
    req = request.json
    if not req or not 'is_available' in req or not 'car_id' in req:
        return send_error(400)

    car_id = req['car_id']

    try:
        if req['is_available']:
            car_repository.rent_car(car_id)
        else:
            car_repository.unrent_car(car_id)
    except:
        return send_error(500)

    return send_ok()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int)
    parser.add_argument('--readonly', type=str)
    args = parser.parse_args()

    fabrique = RepositoryFabrique(args.port, True if args.readonly == "true" else False)

    user_repository = fabrique.create_user_repository()
    dealership_respository = fabrique.create_dealership_repository()
    car_repository = fabrique.create_car_repository()

    app.run(debug=True)
