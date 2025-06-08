#!/usr/bin/python3
"""Python module to serialize and deserialize Python objects"""
import pickle


class CustomObject:


    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        
        Args:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
        
    def display(self):
        """
        Display the object's attributes.
        
        Return:
            str: information.
        """
        return f"Name: {self.name}, Age: {self.age}, Is Student: {self.is_student}"

    def serialize(self, filename):
        """
        Serialize the CustomObject instance to a file.
        
        Args:
            filename (str): Name of the file to save the serialized object.
            
            Return:
                None
        """
        with open(filename, 'wb') as file:
            pickle.dump(self,file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file to create a CustomObject.
        
    Args:
            filename (_type_): _description_
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
