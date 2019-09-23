from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

# as an api we don't need a decorator
api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
