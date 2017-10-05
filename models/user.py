#!/usr/bin/python3
""" module stores user info for hbnb """

from models.base_model import BaseModel


class User(BaseModel):
    """ user class for airbnb clone """
    dict_attrs = {"email": str, "password": str, "first_name": str,
                  "last_name": str}
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user for airbnb clone"""
        super().__init__(*args, **kwargs)
