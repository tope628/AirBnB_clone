#!/usr/bin/python3
'''module: file_storage
this module contains the FileStorage class
'''
import json
import datetime as DT

class FileStorage:
    '''class: FileStorage
    class for implementing persistant storage of JSON formatted data
    __file_path: string name of file path
    __objects: empty di$ct to be populated by string representation of
        objects as follows:
        key: string = <class-name>.id
        value = JSON representation of an object
    '''

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        '''method: __init__
        initializes instance of class FileStorage
        '''
        pass

    def all(self):
        '''method: all
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''method: new
        places into __objects the obj with this key:
            <obj class name>.id
        '''
        key = str(obj.__class__.__name__) + "." + str(obj["id"])
        self.__objects[key] = obj

    def save(self):
        '''method: self
        serializes __objects to the JSON file
        (path = __file_path)
        '''
        for key, value in self.__objects.items():
            for k, v in value.items():
                if isinstance(v, DT.datetime):
                  FileStorage.__object[key][k] = v.isoformat()
        json_str = json.dumps(self.__objects)
        with open(__file_path, mode='w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        '''method: reload
        deserializes the JSON file to __objects, but only
        if JSON file exists, otherwise do nothing)
        '''
        try:
            with open(__filepath, mode='r', encoding='utf-8') as f:
                json_str = json.loads()
            print (json_str)
        except:
            json_str = "debug"
