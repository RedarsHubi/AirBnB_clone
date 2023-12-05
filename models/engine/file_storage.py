#!/usr/bin/python3
"""Module for file storage class"""


class FileStorage:
    """Represents filestorage class"""

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self._objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj


