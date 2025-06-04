#!/usr/bin/python3
"""Module to turns JSON string to object."""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string."""
    return json.loads(my_str)
