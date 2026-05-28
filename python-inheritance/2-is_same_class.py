#!/usr/bin/python3
"""Module that defines a function for checking exact class"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exactly
    an instance of the specified class, otherwise False."""
    return type(obj) is a_class
