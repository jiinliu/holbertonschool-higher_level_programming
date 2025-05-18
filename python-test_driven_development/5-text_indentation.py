#!/usr/bin/python3
"""
This module provides a function to print text with specific indentation rules.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
