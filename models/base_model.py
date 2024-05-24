#!/usr/bin/python3
"""
Module defining BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Initialisation common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initailisation BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates updated_at attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] =self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr



