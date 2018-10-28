from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Mi tienda',
        'items': [
            {
                'name': 'Mi item',
                'price': 15.99
            }
        ]
    }
]

# From the server side

# GET - used to send data back only
# POST - used to receive data

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # If the store name matches, return it
    # If none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    
    return jsonify({'mensaje': 'No existe la tienda'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):

    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'mensaje': 'Tienda no encontrada'})
    

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({'mensaje': 'No existe la tienda'})    

app.run(port=5000)