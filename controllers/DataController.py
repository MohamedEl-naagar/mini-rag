from .BaseController import BassController

from fastapi import UploadFile
class DataController(BassController):
    
    def __init__(self):
         super().__init__()
         self.size_scale = 1048576
    def validate_upload_file(self,file:UploadFile):
         if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENTIONS:
              return False
         if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
              return False
         
         return True