#!/usr/bin/python3
""" module stores city info for hbnb """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class for airbnb clone """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city for airbnb clone"""
        super().__init__(*args, **kwargs)
