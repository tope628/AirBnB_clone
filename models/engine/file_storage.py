#!/usr/bin/python3
'''module: file_storage
this module contains the FileStorage class
'''
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    '''class: FileStorage
    class for implementing persistant storage of JSON formatted data
    __file_path: string name of file path
    __objects: empty dict to be populated by string representation of
        objects as follows:
        key: string = <class-name>.id
        value = JSON representation of an object
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''method: all
        returns the dictionary __objects
        '''
        return self.__objects

    def all_classes(self):
        '''method: all_classes
        returns list of all classes of objects in __objects
        '''
        classes = []
        for obj in self.__objects:
            a_class = obj.split(".")[0]
            if a_class not in classes:
                classes.append(a_class)
        return classes

    def new(self, obj):
        '''method: new
        places <obj> into __objects with this key:
            <obj class name>.id
        '''
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        '''method: self
        serializes __objects to the JSON file
        (path = __file_path)
        '''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        json_str = json.dumps(new_dict)
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        '''method: reload
        deserializes the JSON file to __objects, but only
        if JSON file exists, otherwise do nothing)
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                dict_from_json = json.load(f)
            for k, v in dict_from_json.items():
                class_name = v["__class__"]
                new_obj = eval(class_name)(**v)
                self.__objects[k] = new_obj
        except FileNotFoundError:
            return
