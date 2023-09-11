from pydantic import BaseModel

class AddVehicle(BaseModel):
    name:str
    color:str
    price:int
    stock: int
    company_name:str

class GetVehicle(BaseModel):
    id:str=None
    name:str
    price:int
    available:bool

class UpdateVehicle(AddVehicle):
    pass

