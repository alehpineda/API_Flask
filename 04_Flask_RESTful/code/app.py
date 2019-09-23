from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        # items is a list of dictionaries
        for item in items:
            # if the name in the dict equals the name of get
            if item['name'] == name:
                # return the dict
                # we don't need jsonify, restful takes care of it
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {
            'name': name,
            'price': 12.00
        }
        items.append(item)
        return item, 201

# as an api we don't need a decorator
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
