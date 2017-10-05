#!/usr/bin/python3
""" module stores amenity info for hbnb """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ amenity class for airbnb clone """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity for airbnb clone"""
        super().__init__(*args, **kwargs)
