from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from .database import connect_to_mongo,close_mongo_connection
from middleware.auth_middleware import protected_route
from server.routes.auth_route import router as user_router
from server.routes.home_route import router as welcome

app = FastAPI()

origins = []
app.add_middleware(CORSMiddleware,allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
async def start_db_client():
   await connect_to_mongo()

@app.on_event("shutdown")
async def close_db_client():
   await close_mongo_connection()

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
   return RedirectResponse(url='/docs')

app.include_router(user_router, tags=["auth"])
app.include_router(welcome,dependencies=[Depends(protected_route)])


