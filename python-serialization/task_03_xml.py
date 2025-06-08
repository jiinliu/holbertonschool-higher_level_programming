#!/usr/bin/python3
"""
Module for serializing and deserializtion using XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML.

    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): xml file name.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        item.set("key", key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): xml file name.
    
    Returns:
        dict: Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        
        for item in root.findall("item"):
            key = item.get("key")
            value = item.text
            data[key] = value
        
        return data
    except (FileNotFoundError, ET.ParseError):
        return None
