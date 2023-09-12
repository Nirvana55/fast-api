from fastapi import  APIRouter,Depends
from middleware.auth_middleware import protected_route
from server.models.vehicle_modle import AddVehicle,GetVehicle,UpdateVehicle
from server.database import get_collection
from bson.objectid import ObjectId
from bson import json_util
import json
from pymongo.collection import ReturnDocument


router = APIRouter(dependencies=[Depends(protected_route)])
collection = get_collection("practice", "vehicles")

@router.get("/welcome",tags=["home"])
def welcome():
    return {"message":"welcome"}

@router.post("/add-vehicle")
async def add_vehicle(item:AddVehicle):
    try:
        collection.insert_one(dict(item))
        return {"message":"Vehicle added successfully"}
    except Exception as e:
        return f"Error:{e}"

@router.get("/{id}")
async def get_vehicle(id:str):
    try:
        vehicle = collection.find_one({"_id":ObjectId(id)})
        if vehicle is None:
             return {"message":"Vehicle not found"}
        return {"message":"Vehicle fetched successfully", "data": json.loads(json_util.dumps(vehicle))}
    except Exception as e:
        return f"Error:{e}"

@router.delete("/{id}")
async def get_vehicle(id:str):
    try:
        vehicle = collection.delete_one({"_id":ObjectId(id)})
        if vehicle is None:
                return {"message":"Vehicle not found"}
        return {"message":"Vehicle removed successfully"}
    except Exception as e:
        return f"Error:{e}"
    
@router.put("/{id}")
async def get_vehicle(id:str,item:AddVehicle):
    try:
        vehicle = collection.find_one_and_update({"_id":ObjectId(id)},{"$set": dict(item)} ,return_document=ReturnDocument.AFTER)
        if vehicle is None:
                return {"message":"Vehicle not found"}
        return {"message":"Vehicle updated successfully"}
    except Exception as e:
        return f"Error:{e}"