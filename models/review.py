#!/usr/bin/python3
""" module stores review info for hbnb """
from models.base_model import BaseModel

class Review(BaseModel):
    """ review class for airbnb clone """

    def __init__(self, *args, **kwargs):
        """initializes review for airbnb clone"""
        if len(kwargs) == 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
        super().__init__(*args, **kwargs)
