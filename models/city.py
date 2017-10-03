#!/usr/bin/python3
""" module stores city info for hbnb """
from models.base_model import BaseModel

class City(BaseModel):
    """ city class for airbnb clone """

    def __init__(self, *args, **kwargs):
        """initializes city for airbnb clone"""
        if len(kwargs) == 0:
            self.state_id = ""
            self.name = ""
        super().__init__(*args, **kwargs)
