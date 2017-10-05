#!/usr/bin/python3
""" module stores user info for hbnb """

from models.base_model import BaseModel


class User(BaseModel):
    """ user class for airbnb clone """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user for airbnb clone"""
        super().__init__(*args, **kwargs)
