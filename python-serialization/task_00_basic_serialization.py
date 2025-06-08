#!/usr/bin/python3
"""Module to seialize and deserialize Python Dictionary"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize Python Dictionary to a JSON file.
    
    Args:
        data (dict): Python Dictionary.
        filename (str): Name of the file.
    
    Return:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Deserialize a JSON file to Python Dictionary.
    
    Args:
        filename (str): Name of the file.
    
    Return:
        None
    """
    with open(filename, 'r') as file:
        return json.load(file)
