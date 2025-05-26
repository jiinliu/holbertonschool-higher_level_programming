#!/usr/bin/python3
"""This module provides a function to check if an object is an instance
of a class or a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or
    an instance of a class that inherited from a_class;
    otherwise False."""
    return isinstance(obj, a_class)
