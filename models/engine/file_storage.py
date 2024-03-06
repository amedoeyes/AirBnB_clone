#!/usr/bin/python3

"""FileStorage module"""

import json
import models


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"

    def __init__(self):
        """init"""

        self.__objects = {}

    def all(self) -> dict:
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj: object) -> None:
        """sets in __objects the obj with key <obj class name>.id"""

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self) -> None:
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, "r") as f:
                for obj in json.load(f).values():
                    self.new(models.classes[obj["__class__"]](**obj))
        except Exception:
            pass
