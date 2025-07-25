#!/usr/bin/python3
"""Module that returns the representation of an object as a string."""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
