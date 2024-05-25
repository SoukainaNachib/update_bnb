#!/usr/bin/python3
"""this module defigne a class city"""
from models.base_model import BaseModel

class City(BaseModel):
    """ Create a new city"""
    state_id = ""
    name = ""