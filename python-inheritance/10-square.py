#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectnagle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes Square with validated size (private)."""
        self.integer_validator("size, size")
        self.__size = size
        super().__init__(size, size)
      
    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
