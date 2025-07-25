#!/usr/bin/python3
"""This module defines a Square class inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that validates size as a positive integer."""

    def __init__(self, size):
        """Initialize Square with validated size (private)."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
