from database import Users

def login(username: str, password: str) -> dict:
    users = Users()
    user = users.get_user(username)
    return {'success': user and user['password'] == password, 'message': 'Logged in' if user and user['password'] == password else 'Invalid credentials'}

def register(username: str, password: str) -> dict:
    users = Users()
    if users.get_user(username):
        return {'success': False, 'message': 'User already exists'}
    users.add_user(username, password)
    return {'success': True, 'message': 'User registered'}

def unregister(username: str) -> dict:
    users = Users()
    if not users.get_user(username):
        return {'success': False, 'message': 'User does not exist'}
    users.remove_user(username)
    return {'success': True, 'message': 'User unregistered'}