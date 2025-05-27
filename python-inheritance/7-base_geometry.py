#!/usr/bin/python3
"""This module defines a base geometry class."""


class BaseGeometry:
    """BaseGeometry class for geometry operations."""
    
    def area(self):
        """Raises an Exception for area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.
        
        Args:
            name (str): The name of the value (for error message).
            value (int): The value to validate.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
