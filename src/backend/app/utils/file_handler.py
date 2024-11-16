import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

class FileHandler:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @staticmethod
    def save_file(file):
        if file and FileHandler.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            temp_path = f"temp/{filename}"
            file.save(temp_path)
            return temp_path
        raise ValueError("Invalid file type")