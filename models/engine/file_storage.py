#!/usr/bin/python3
'''module: file_storage
this module contains the FileStorage class
'''


class FileStorage:
    '''class: FileStorage
    class for implementing persistant storage of JSON formatted data
    __file_path: string name of file path
    __objects: empty di$ct to be populated by string representation of
        objects as follows:
        key: string = <class-name>.id
        value = JSON representation of an object
    '''

    __file_path = ""
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
        pass

    def new(self, obj):
        '''method: new
        places into __objects the obj with this key:
            <obj class name>.id
        '''
        pass

    def save(self):
        '''method: self
        serializes __objects to the JSON file
        (path = __file_path)
        '''
        pass

    def reload(self):
        '''method: reload
        deserializes the JSON file to __objects, but only
        if JSON file exists, otherwise do nothing)
        '''
        pass
