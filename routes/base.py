# routes

from fastapi import FastAPI,APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "message":f"Hello, and welcome to our {app_name} system version {app_version}! 🤖"
    }
