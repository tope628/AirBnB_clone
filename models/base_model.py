#!/usr/bin/python3
'''module: base_model
this module contains the class base_model
'''
import uuid
import datetime


class BaseModel:
    '''class: Base_model
    base model for AirBnB Clone
    '''

    def __init__(self, *args, **kwargs):
        '''method: __init__
        initializes instance of class Base_model
        '''
        self.id = uuid.uuid4()
        time_stamp = datetime.datetime.now()
        self.created_at = time_stamp
        self.updated_at = time_stamp

    def __str__(self):
        '''method: __str__
        returns string representation of Base_model object
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        '''
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        '''method: save
        info to fill in here
        '''
        pass

    def to_dict(self):
        '''method: to_dict
        accepts: an object
        adds to dict: key __class__
        created_at: converted to string, ISO format
        updated_at: converted to string, ISO format
            ex: 2017-06-14T22:31:03.285259
        returns: dictionary representation of all attributes of the object
        TODO: Keys may need to be mapped to desired values
        TODO: something, there will certainly be something to fix!!!
        '''
        new_dict = {}
        print("debug: self.__dict__:{}".format(self.__dict__))
        for key, val in self.__dict__.items():
            new_dict[key] = val
        new_dict["created_at"] = self.__dict__['created_at'].isoformat()
        new_dict["updated_at"] = self.__dict__['updated_at'].isoformat()
        return new_dict
