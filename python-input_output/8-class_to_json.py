#!/usr/bin/python3
"""Defines a function that returns the dictionary description for JSON serialization of an object."""
def class_to_json(obj):
    return obj.__dict__
