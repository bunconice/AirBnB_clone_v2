#!/usr/bin/python3
"""module for instantiating an object of class FileStorage"""

from models.city import City
from os import getenv
from models.user import User
from models.engine.db_storage import DBStorage
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
