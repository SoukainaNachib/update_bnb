#!/usr/bin/python3
"""this module define a class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ it represents a place/house """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []