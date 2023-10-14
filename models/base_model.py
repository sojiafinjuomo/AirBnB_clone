#!/usr/bin/python3
"""
The Base Model of our Airbnb clone project.
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Parent model
    """
    def __init__(self, *args, **kwargs):
        """
        initializes the public instance attribute
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        else:
            for key, value in kwargs.item():
                if key == created_at or key == updated_at:
                    kwargs[created_at] = datetime.strptime(kwargs[
                                "created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    kwargs[updated_at] = datetime.strptime(kwargs[
                                "updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """
        returns string representation of the class name
        """
        return [{}], ({}), {}.format(__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        cp_dict = dict(self.__dict__)
        cp_dict['__class__'] = self.__class__.__name__
        cp_dict[created_at] = self.created_at.strptime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dict[updated_at] = self.updated_at.strptime("%Y-%m-%dT%H:%M:%S.%f")
        return (cp_dict)
