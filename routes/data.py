
from fastapi import APIRouter, Depends,UploadFile,status
from fastapi.responses import JSONResponse
from helper.config import Settings, get_settings
from controllers.DataController import DataController
from controllers import DataController , ProjectController
import os
import aiofiles
import logging
logger = logging.getLogger("uvicor.logger")
from models import ResponseSignal 
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_upload_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}        
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(orig_file_name=file.filename, project_id=project_id)
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
            logger.error(f"Error while uploading the file: {e}")
            return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
           "Signal":ResponseSignal.FILE_UPLOAD_FAILED.value
        }
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCESS.value,
            "file_path": file_path,
            "project_dir": project_dir_path
        }
    )

# validate the file properties