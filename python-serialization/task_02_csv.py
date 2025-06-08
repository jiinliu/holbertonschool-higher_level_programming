#!/usr/bin/python3
"""Module for serialization."""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert csv file to JSON file.

    Args:
        csv_file (str): CSV file name.
        
    Return:
        bool: True if conversion is successful.
    """
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        with open("data.json", mode='w') as file:
            json.dump(data, file)

        return True
    except (FileNotFoundError):
        return False
