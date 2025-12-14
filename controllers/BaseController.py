from helper.config import get_settings,Settings
import random
import string
import os

class BaseController:
    def __init__(self):
        self.app_settings=get_settings()
        self.base_dir=os.path.dirname(os.path.dirname(__file__))
        self.files_dir =os.path.join(self.base_dir,"assests/files")
    pass

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))