#!/usr/bin/python3

"""BaseModel module"""

import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """init"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """save object"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary representation of object"""

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """return string representation of object"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
