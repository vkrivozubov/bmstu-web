from flask import Flask
from flask.json import jsonify
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import*
from swagger_ui import api_doc

app = Flask(__name__)

api_doc(app, config_path='./config/test.yaml', url_prefix='/api/doc', title='API doc')

@app.route("/")
def hello():
    return "Hello world!"

spec = APISpec(
    title="flask-api-swagger-doc",
    version="1.0.0",
    openapi_version="3.0.1",
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict()) 

class TodoResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    status = fields.Boolean()

class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))

@app.route("/todo")
def todo():
    """Get list of Todo
        ---
        get:
            description: Return a todo list
            content: 
                application/json:
                    schema: TodoListResponseSchema
    """

    dummy_data = [{
        "id": 1,
        "title": "Finish this task",
        "status": False
    }, {
        "id": 1,
        "title": "Finish hue task",
        "status": True
    }]

    return TodoListResponseSchema().dump({ 'todo_list': dummy_data })

with app.test_request_context():
    spec.path(view=todo)

if __name__ == "__main__":
    app.run(debug=True)
