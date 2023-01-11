#!/usr/bin/python3
"""A class that defines a student"""


class Student:
    """A class that defines a student""" 
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
