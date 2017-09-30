""" instance of HBNB app"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
