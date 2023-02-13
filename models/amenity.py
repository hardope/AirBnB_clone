#!/usr/bin/python3
"""Module base_model

This Module contains a definition for Amenity Class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that represents a amenity

    Attribute:
        name (str): the name of the amenity
    """

    name = ""
