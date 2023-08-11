from fastapi import  APIRouter, Response
from server.models.auth_model import Token,SignUp, SignIn
from server.database import get_collection
from utils.password_utils import verify_password,hashed_password
from handlers.jwt_handler import generate_jwt_token

router= APIRouter()

collection = get_collection("practice","users")

@router.post("/signup", tags=["auth"])
async def sign_up(item:SignUp,res:Response):
    try:
        user = collection.find_one({"email":item.email})
        if(user):
            return {"message":"User exist"}
        token = generate_jwt_token(item.email)
        encrypt_password = hashed_password(item.password)
        collection.insert_one({"name":item.name,"email":item.email, "password":encrypt_password})
        res.set_cookie(key="Token", value=token)
        return {"message": "User created successfully"}  
    except Exception as e:
        print(f"Error:{e}")


@router.post("/login", tags=["auth"])
async def login(item:SignIn, res:Response):
    try:
        user = collection.find_one({"email":item.email})
        if not user:
            return {"message":"User does not exist"}
        compare_password = verify_password(item.password, user["password"])
        if not compare_password:
            return {"message":"Email or password does not match"}
        token = generate_jwt_token(item.email)
        res.set_cookie(key="Token", value=token)
        return {"message": "User logged in successfully"}
    except Exception as e:
        print(f"Error:{e}")


