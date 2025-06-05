#!/usr/bin/python3
def class_to_json(obj):
    """Module to convert a class instance to a JSON serializable dictionary."""
    return obj.__dict__