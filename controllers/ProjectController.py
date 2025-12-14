from .BaseController import BaseController
import os
import re

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        # sanitize project_id
        safe_project_id = re.sub(r'[^\w\-]', '_', project_id)

        project_dir = os.path.join(self.files_dir, safe_project_id)
        os.makedirs(project_dir, exist_ok=True)

        return project_dir
