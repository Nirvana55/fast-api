import jwt
from server.models.auth_model import SignUp

SECRET_KEY = "Hello123@@:"

def generate_jwt_token(data:str):
    encoded_jwt = jwt.encode({"data":data}, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_jwt_token(encoded_jwt:str):
    decoded_jwt = jwt.decode(encoded_jwt, SECRET_KEY, algorithms="HS256")
    return decoded_jwt