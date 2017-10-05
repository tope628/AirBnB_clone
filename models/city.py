#!/usr/bin/python3
""" module stores city info for hbnb """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class for airbnb clone """
    dict_attrs = {"state_id": str, "name": str}
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city for airbnb clone"""
        super().__init__(*args, **kwargs)
