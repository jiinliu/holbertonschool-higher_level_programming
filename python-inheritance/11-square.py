#!/usr/bin/python3
"""This module defines a Rectangle class that inheriting from Rectangle with
custom __str_. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that validates size as a positive integer."""
    
    
    def __init__(self, size):
        """Initialize Square with validateed size (private)."""
        self.interger_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        
        
        def area(self):
            """Returns the area of the square."""
            return self.__size * self.__size
        
        
        def __str__(self):
            """Returns a string representation: [Square] <size>."""
            return "[Square] {}/{}".format(self.__size, self.__size)
