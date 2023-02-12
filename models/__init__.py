#!/usr/bin/python3
"""Creates a unique FileStorage instance for the application"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()