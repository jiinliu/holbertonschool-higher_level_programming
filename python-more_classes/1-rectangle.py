#!/usr/bin/python3
"""
This module defines a class named Rectangle.
"""


class Rectangle:
    """
    Class for Rectangle.
    """
    def __init__(self, size=0):
        """Initialize a new Rectangle instance.

        This constructor validates and sets the size of the square.

        Args:
            size (int, optional): The size of the Rectangle. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the Rectangle.

        Returns:
            int: The size of the Rectangle.
        """
        return self.__size

    @size.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The new size of the Retangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__size = value

def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
        self.__height = value

    
    
    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height


