#!/usr/bin/python3
"""Defines a function that reads a text file
and appends a sting at the end of the file."""


def append_wirte(filename="", text=""):
    """Appends a sting at the end of a text file (UTF8)"""
    with open (filename, "a", encoding="utf-8") as f:
        return f.write(text)
