#!/usr/bin/python3
""" module stores review info for hbnb """

from models.base_model import BaseModel


class Review(BaseModel):
    """ review class for airbnb clone """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review for airbnb clone"""
        super().__init__(*args, **kwargs)
