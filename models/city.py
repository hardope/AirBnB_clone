#!/usr/bin/python3
"""Module base_model

This Module contains a definition for City Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a city

    Attributes:
        name (str): name of the city
        state_id (str): the state id
    """

    state_id = ""
    name = ""
