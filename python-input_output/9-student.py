#!/usr/bin/python3
"""Modle that defines a student class."""
class Student:
    """A class that defines a student."""
    
    def __innit__(self, first_name, last_name, age):
        """Initializes the student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """Returns the dictionary reprsentation of the Student."""
        return self.__dict__
