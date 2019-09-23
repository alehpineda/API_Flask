from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        # filter(lambda, iterator) return filter object.
        # filter object is a generator
        item = next(filter(lambda x: x['name'] == name, items), None)
        # return item, and code using terniary operators
        return {'item': item}, 200 if item else 404

    def post(self, name):
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
