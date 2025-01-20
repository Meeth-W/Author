import os
import json
import datetime
from typing import Optional

from jwt import JWT, exceptions, AbstractJWKBase
from jwcrypto import jwk

# Initialize the JWT instance
instance = JWT()

# Function to load or create the secret key
def load_or_create_secret_key():
    secret_key_path = os.path.join(os.path.dirname(__file__), 'data/secret_key.json')
    if not os.path.exists(secret_key_path):
        # Generate a new symmetric JWK
        key = jwk.JWK.generate(kty='oct', size=256)
        with open(secret_key_path, 'w') as f:
            f.write(key.export(private_key=True))
    else:
        with open(secret_key_path, 'r') as f:
            key = AbstractJWKBase.from_dict(json.load(f))
    return key

# Use the secret key directly without exporting as PEM
SECRET_KEY = load_or_create_secret_key()  # This exports the symmetric key

# Users class for managing user data
class Users:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), 'data')

    def get_user(self, username: str) -> Optional[dict]:
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
        users.pop(username, None)
        with open(os.path.join(self.path, 'users.json'), 'w') as f:
            json.dump(users, f)


# Tokens class for handling JWT tokens
class Tokens:
    def create_token(self, username: str) -> str:
        """
        Create a JWT token with an expiration time of 1 hour.
        """
        payload = {
            "sub": username,
            "exp": int((datetime.datetime.now() + datetime.timedelta(hours=1)).timestamp())
        }
        try:
            token = instance.encode(payload, SECRET_KEY, alg="HS256")
            return token
        except exceptions.JWTEncodeError as e:
            raise Exception(f"Error encoding the token: {e}")

    def verify_token(self, token: str) -> Optional[str]:
        """
        Verify a JWT token and return the username (sub) if valid.
        """
        try:
            payload = instance.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload["sub"]
        except exceptions.JWTDecodeError:
            print("Token decoding failed.")
            return None
        except exceptions.JWTException as e:
            print(f"General JWT error: {e}")
            return None
