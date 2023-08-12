#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class which defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(
         self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        map_obj = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_obj[key] = value.isoformat()
            else:
                map_obj[key] = value
            map_obj["__class__"] = self.__class__.__name__
        return map_obj
