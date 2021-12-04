from flask import Flask, request
from flask.json import jsonify
from werkzeug.exceptions import abort
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import*
from swagger_ui import api_doc

app = Flask(__name__)

api_doc(app, config_path='../config/swagger.yaml', url_prefix='/api/doc', title='API doc')

spec = APISpec(
    title="flask-api-swagger-doc",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/api/user", methods=['POST'])
def register_user():
    req = request.json
    if not req or not 'username' in req or not 'password' in req or not 'role' in req:
        error = {
            'status': '400',
            'message': "Invalid request"
        }
        return jsonify(error), 400

    response = {
        'status': '200',
        'message': "OK"
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
