#!/usr/bin/python3
"""
Module: FileStorage
Desc: Serializes instances to a JSON file
\and deserializes JSON file to instances
Author: Mire
"""


class FileStorage():
    """Serialization and Deserialization of Instances to and fro JSON file"""

    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        """Returns all objects in the file storage"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the file storage object class"""
        class_name = self.__class__.__name__
        instance_id = self.id
        store_object = f"{class_name}.{instance_id}"
        self.__objects[store_object] = obj.__dict__

    def save(self):
        """Serializes object dictionary to json file"""
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        """Deserializes object dictionary from json file"""
        try:
            with open("storage.json", "r") as storage_file:
                self.__objects = json.load(storage_file)
        except FileNotFoundError:
            pass
