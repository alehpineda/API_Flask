from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = '12345'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    def get(self, name):
        # filter(lambda, iterator) return filter object.
        # filter object is a generator
        # If the generator is empty, return None
        item = next(filter(lambda x: x['name'] == name, items), None)
        # return item, and code using terniary operators
        # code 200 ok, code 404 not found
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # if the item already exist, return message and code 400 bad request
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # get_json has two parameters force, silent
        data = request.get_json()
        item = {
            'name': name,
            'price': data['price']
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

# as an api we don't need a decorator
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# Disable debug in production
app.run(port=5000, debug=True)
