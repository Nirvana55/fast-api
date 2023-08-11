from fastapi import  APIRouter,Depends
from middleware.auth_middleware import protected_route

router = APIRouter(dependencies=[Depends(protected_route)])

@router.get("/welcome",tags=["home"])
def welcome():
    return {"message":"welcome"}