import os, json

# Class to handle json files in the database folder
class Users:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), 'data')

    def get_user(self, username: str) -> dict:
        with open(os.path.join(self.path, 'users.json'), 'r') as f:
            users: dict = json.load(f)
        return users.get(username)

    def add_user(self, username: str, password: str) -> None:
        with open(os.path.join(self.path, 'users.json'), 'r') as f:
            users: dict = json.load(f)
        users[username] = {'password': password}
        with open(os.path.join(self.path, 'users.json'), 'w') as f:
            json.dump(users, f)
        
    def remove_user(self, username: str) -> None:
        with open(os.path.join(self.path, 'users.json'), 'r') as f:
            users: dict = json.load(f)
        users.pop(username)
        with open(os.path.join(self.path, 'users.json'), 'w') as f:
            json.dump(users, f)