
from fastapi import APIRouter, Depends,UploadFile
from helper.config import Settings, get_settings
from controllers.DataController import DataController
from controllers import DataController
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file:UploadFile,app_settings:Settings=Depends(get_settings)):
    is_valid = DataController().validate_upload_file(file=file)
    return{
        "message":f"upload file -- {is_valid}"
    }
# validate the file properties