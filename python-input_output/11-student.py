#!/usr/bin/python3
"""This module defines a Student class for serialization"""
class Student:
    """Defines a student by first_name, last_neme, and age."""
    
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """Return dictionart representation of the Student, optionallly filtered by attrs."""
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def relod_from_json(self, json):
        """Replace attributes from a dictionary"""
        for key, value in json:
            setattr(self, key, value)
        