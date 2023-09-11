from fastapi import  APIRouter,Depends
from middleware.auth_middleware import protected_route
from server.models.vehicle_modle import AddVehicle,GetVehicle,UpdateVehicle
from server.database import get_collection

router = APIRouter(dependencies=[Depends(protected_route)])
collection = get_collection("practice", "vehicles")

@router.get("/welcome",tags=["home"])
def welcome():
    return {"message":"welcome"}

@router.post("/add-vehicle")
async def add_vehicle(item:AddVehicle):
    try:
        await collection.insert_one(item)
        return {"message":"Vehicle added successfully"}
    except Exception as e:
        print(f"Error:{e}")

async def get_vehicle(id:str):
    try:
        vehicle = await collection.find_one({id})
        return {"message":"Vehicle fetched successfully", "data": vehicle}
    except Exception as e:
        print(f"Error:{e}")