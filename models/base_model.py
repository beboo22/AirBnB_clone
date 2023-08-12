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
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                self.__dict__[key] = value.isoformat()

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
