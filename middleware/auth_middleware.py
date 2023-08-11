from fastapi import Request, HTTPException
from handlers.jwt_handler import verify_jwt_token
from server.database import get_collection

collection = get_collection("practice", "users")

async def protected_route(req: Request):
    try:
        cookie_data = req.cookies.get("Token")
        if cookie_data is None:
            raise HTTPException(status_code=401, detail="Invalid or missing token")
        else:
            token = verify_jwt_token(cookie_data)
            user = collection.find_one({"email": token["data"]})
            if user is None:
                raise HTTPException(status_code=401, detail="User not found")
            return user
    except HTTPException as e:
        raise e
