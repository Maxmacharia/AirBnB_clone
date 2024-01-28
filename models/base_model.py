#!/usr/bin/python3

"""Defines a BaseModel class the defines all common attributes"""

from datetime import datetime
import uuid


class BaseModel:
    """Defines a BaseModel class the defines all common attributes"""

    def __init__(self):
        """Defines the construtor of the Base Model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Defines the str method which returns a string object"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Defines the save method the save the updated time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Defines the to_dict method that
        return the dictionary of the object instances"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
