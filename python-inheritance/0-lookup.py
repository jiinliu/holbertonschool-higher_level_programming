#!/usr/bin/python3
"""
This module provides a function to listavailable attributes and metods
of an abject.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methobds of an object.
    Args:
        obj: The object to inspect.
    Returns:
        A list of strings representing the attributes and methods of
        the object.
    """
    return dir(obj)
