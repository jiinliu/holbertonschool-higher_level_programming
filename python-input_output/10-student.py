#!/usr/bin/python3
"""Defines a Student class with optional JSON serialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs,
                    list) and all(type(attr) == str for attr in attrs):
            return {attr: getattr(self,
                               attr) for attr in attrs if hasattr(self, attr)}
