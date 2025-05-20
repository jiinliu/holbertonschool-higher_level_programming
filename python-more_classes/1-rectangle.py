#!/usr/bin/python3
"""
This module defines a class named Rectangle.
"""


class Rectangle:
    """
    Class for Rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the size of the Rectangle.

        Returns:
            int: The size of the Rectangle.
        """
        return self.__width

    @width.setter
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
        self.__width = value

    @property   
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
    @height.setter
    def height(self, value):
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
