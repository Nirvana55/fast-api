from pydantic import BaseModel

class SignUp(BaseModel):
    id:str = None
    name:str
    email:str
    password:str


class SignIn(BaseModel):
    email:str
    password:str

class SystemUser(SignIn):
    id:str


class Token(BaseModel):
    message: str
    token: str