from user import User
users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {
    # set comprehension
    u.username: u for u in users
}

userid_mapping = {
    u.id: u for u in users
}

def authenticate(username, password):
    # .get other way to access a dict, also map None
    user = username_mapping.get(username_mapping, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
