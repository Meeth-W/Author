from database import Users, Tokens

users = Users()
tokens = Tokens()

def login(username: str, password: str) -> dict:
    user = users.get_user(username)
    if not user or user['password'] != password:
        return {'success': False, 'message': 'Invalid credentials'}
    token = tokens.create_token(username)
    return {'success': True, 'token': token}

def register(username: str, password: str) -> dict:
    if users.get_user(username):
        return {'success': False, 'message': 'User already exists'}
    users.add_user(username, password)
    return {'success': True, 'message': 'User registered'}

def unregister(username: str) -> dict:
    if not users.get_user(username):
        return {'success': False, 'message': 'User does not exist'}
    users.remove_user(username)
    return {'success': True, 'message': 'User unregistered'}

def verify_user(token: str) -> dict:
    username = tokens.verify_token(token)
    if not username:
        return {'success': False, 'message': 'Invalid or expired token'}
    return {'success': True, 'username': username}
