#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects[__class__.__name__+ '.'+str(obj)] = obj
    def save(self):
        with open(self.__file_path,'w+')as f:
            json.dump ()
