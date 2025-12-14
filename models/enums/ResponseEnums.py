from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCESS = "file validate sucessfully"
    FILE_TYPE_NOT_SUPPORTED="file not supported"
    FILE_SIZE_IS_MAX   = "file size is too large"
    FILE_UPLOAD_SUCESS =   "Sucess"
    FILE_UPLOAD_FAILED =   "file upload failed"
     