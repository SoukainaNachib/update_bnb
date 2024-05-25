#!/usr/bin/python3
"""this module define a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Create a new user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""