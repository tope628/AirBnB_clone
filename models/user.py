#!/usr/bin/python3
""" module stores user info for hbnb """

from models.base_model import BaseModel


class User(BaseModel):
    """ user class for airbnb clone """
    dict_attrs = {"email": str, "password": str, "first_name": str,
                  "last_name": str}

    def __init__(self, *args, **kwargs):
        """initializes user for airbnb clone"""
        if len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
        super().__init__(*args, **kwargs)
