#!/usr/bin/python3
"""Module to create an object from a JSON file and add it to a file."""
import sys


if __name__ == "__main__":

    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    file_name = "add_item.json"

    try:
        json_file = load_from_json_file(file_name)
    except FileNotFoundError:
        json_file = []

    arg_list = sys.argv[1:]
    json_file.extend(arg_list)

    save_to_json_file(json_file, file_name)
