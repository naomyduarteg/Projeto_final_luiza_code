from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from src.routes.api import router as api_router
from dotenv import load_dotenv
import os

app = FastAPI()

@app.on_event("startup")
def startup_db_client(): 
    load_dotenv()
 
    ATLAS_URI = os.environ.get('ATLAS_URI')
    DB_NAME = os.environ.get("DB_NAME")
    
    app.mongodb_client = MongoClient(ATLAS_URI)
    app.database = app.mongodb_client[DB_NAME]
    print("Project connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(api_router)

if __name__ == '__main__':
    PORT = os.environ.get("PORT")
    HOST = os.environ.get("HOST")#indicates that this programm is a script to be run, not imported or just a library
    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info", reload = True)
    # uvicorn.run("main:app")
