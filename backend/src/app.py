from flask import Flask, request, send_from_directory
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
from flask_cors import CORS
from jwt import TokenStorage
from OpenSSL import SSL

import argparse

app = Flask(__name__)

cors = None
fabrique = None
user_repository = None
dealership_respository = None
car_repository = None
token_storage = TokenStorage()

api_doc(app, config_path='../config/swagger.yaml', url_prefix='/api/v1', title='API doc')

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

@app.route("/api/v1/swagger/<path:path>")
def send_index(path):
    return send_from_directory("/Users/vlad/Downloads/bmstu-web/backend/static/dist/", path)

@app.route("/api/v1/users/user", methods=['POST'])
def register_user():
    req = request.json
    if not req or not 'username' in req or not 'password' in req or not 'role' in req:
        return send_error(400)

    new_user_domain = User(
        None,
        req['username'],
        req['password'],
        req['role']
    )
    users = user_repository.get_all_users()
    
    for user in users:
        if user.username == new_user_domain.username:
            return send_error(400)

    user_repository.add_new_user(new_user_domain)

    users = user_repository.get_all_users()

    for user in users:
        if user.username == new_user_domain.username:
            token_string = token_storage.create_token()
            response = {
                'id': user.id,
                'role': new_user_domain.role,
                'token': token_string
            }
            return jsonify(response), 200

    return send_error(400)

@app.route("/api/v1/users/login", methods=['POST'])
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
                print(users)
                token_string = token_storage.create_token()
                response = {
                    'id': user.id,
                    'role': user.role,
                    'token': token_string
                }
                return jsonify(response), 200
            else:
                return send_error(400)

    return send_error(400)

@app.route("/api/v1/dealerships", methods=['GET'])
def get_dealerships():
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)

    dealerships = dealership_respository.get_dealerships()
    DTO_dealerships = []
    converter = DealershipDomainToDTOConverter()

    for dealer in dealerships:
        DTO_dealerships.append(converter.convert(dealer).get_dict())

    return jsonify(DTO_dealerships), 200

@app.route("/api/v1/dealerships/dealership", methods=['POST'])
def create_dealership():
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
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
    print(new_dealership_domain)
    try:
        dealership_respository.create_dealership(new_dealership_domain)
    except:
        return send_error(500)

    return send_ok()

@app.route("/api/v1/dealerships/<int:id>", methods=['DELETE'])
def delete_dealership(id):
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
    try:
        dealership_respository.remove_dealership(id)
    except:
        return send_error(500)

    return send_ok()

@app.route("/api/v1/cars/<int:dealership_id>", methods=['GET'])
def get_cars_for_dealership(dealership_id):
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
    cars = car_repository.get_cars(dealership_id)

    converter = CarDomainToDTOConverter()
    DTO_cars = []

    for car in cars:
        DTO_cars.append(converter.convert(car).get_dict())

    return jsonify(DTO_cars), 200

@app.route("/api/v1/cars/car/<int:id>", methods=['DELETE'])
def delete_car(id):
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
    try:
        car_repository.delete_car(id)
    except:
        return send_error(500)

    return send_ok()

@app.route("/api/v1/cars/car", methods=['POST'])
def create_car():
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
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

@app.route("/api/v1/cars/car/availabilty", methods=['PATCH'])
def change_car_availability():
    token_string = request.headers['Authorization']
    if not token_storage.token_exists(token_string):
        return send_error(401)
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
    parser.add_argument('--back_port', type=str)
    args = parser.parse_args()

    fabrique = RepositoryFabrique(args.port, True if args.readonly == "true" else False)

    user_repository = fabrique.create_user_repository()
    dealership_respository = fabrique.create_dealership_repository()
    car_repository = fabrique.create_car_repository()

    cors = CORS(app)
    app.logger.disabled = True
    app.run(debug=False,port=int(args.back_port),ssl_context=('localhost.crt', 'localhost.key'))
