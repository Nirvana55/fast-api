from pymongo import MongoClient
import os

CONNECTION_STRING = os.environ.get("MONGOSTRING")
client = MongoClient(CONNECTION_STRING)

async def connect_to_mongo():
    try:
        client.practice.command("ping")
        print("database connected successfully.")
        return True
    except Exception as e:
        print(f"Error:{e}")
        return False

async def close_mongo_connection():
    try:
        client.close()
    except Exception as e:
        print(f"Error closing mongodb connection:{e}")
        raise e

def get_database(db_name:str):
    return client.get_database(db_name)

def get_collection(db_name:str, collection_name:str):
    db = get_database(db_name)
    return db.get_collection(collection_name)

