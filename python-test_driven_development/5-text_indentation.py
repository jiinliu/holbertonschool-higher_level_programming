#!/usr/bin/python3
"""
This module provides a function to print text with specific
indentation rules.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    split_chars = ('.', '?', ':')
    line = ""
    for char in text:
        line += char
        if char in split_chars:
            print(line.strip())
            print()
            line = ""
    if line.strip():  # Print the last piece if not empty
        print(line.strip())
