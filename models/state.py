#!/usr/bin/python3
""" module stores state info for hbnb """

from models.base_model import BaseModel


class State(BaseModel):
    """ state class for airbnb clone """
    dict_attrs = {"name": str}
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state for airbnb clone"""
        super().__init__(*args, **kwargs)
