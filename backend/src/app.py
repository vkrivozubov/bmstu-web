from flask import Flask, request
from flask.json import jsonify
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from repository_fabruque import RepositoryFabrique
from marshmallow import*
from swagger_ui import api_doc
from Domain.user import *

app = Flask(__name__)

fabrique = RepositoryFabrique()
user_repository = fabrique.create_user_repository()
dealership_respository = fabrique.create_dealership_repository()
car_repository = fabrique.create_car_repository()

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
    ()

@app.route("/api/dealership", methods=['POST'])
def create_dealership():
    ()

@app.route("/api/dealership/<int:id>", methods=['DELETE'])
def delete_dealership(id):
    ()

@app.route("/api/car/cars/<int:dealership_id>", methods=['GET'])
def get_cars_for_dealership(dealership_id):
    ()

@app.route("/api/car/<int:id>", methods=['DELETE'])
def delete_car(id):
    ()

@app.route("/api/car", methods=['POST'])
def create_car():
    ()

@app.route("/api/car/availabilty", methods=['PATCH'])
def change_car_availability():
    ()

if __name__ == "__main__":
    app.run(debug=True)
