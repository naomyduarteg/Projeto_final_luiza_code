from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.api import router as api_router
config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(api_router)

if __name__ == '__main__': #indicates that this programm is a script to be run, not imported or just a library
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)
