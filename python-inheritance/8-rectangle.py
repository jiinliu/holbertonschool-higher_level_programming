#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BassGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that ingherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height