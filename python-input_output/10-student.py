#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance."""
        if attrs is not None and type(attrs) is list:
            new_dict = {}

            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]

            return new_dict

        return self.__dict__
