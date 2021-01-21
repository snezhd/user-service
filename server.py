from flask import (Flask, abort, request)

app = Flask(__name__)

users = {}

counter = 0

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        return users[id]
    except KeyError:   
        return 'Not Found', 404


@app.route('/api/users', methods=['GET'])
def get_users():
    return {'users': list(users.values())}


@app.route('/api/users', methods=['POST']) 
def create_user():
    global counter
    counter += 1
    body = request.json
    user = {
        'id': counter,
        'name': body['name'],
        'email': body['email']
    }
    users[counter] = user

    return {'id': counter}, 201

   
    # TODO: if user already exist return 409 - Conflict
    # TODO: email regex validator


@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    if id in users.keys():
        user = users[id]
        body = request.json
        user = {
            'id': user['id'],
            'name': body['name'],
            'email': body['email']
        }
        users[id] = user
    return 'updated user'


@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id not in users:
        return 'Not found', 404
    else:
        del users[id]    
        return 'deleted user'


if __name__ == '__main__':
    app.run(debug=True)
