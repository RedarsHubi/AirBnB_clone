#!/usr/bin/python3
"""Module for file storage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents filestorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    class_type = eval(class_name)
                    obj_instance = class_type(**obj_data)
                    self.__objects[key] = obj_instance
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            pass
