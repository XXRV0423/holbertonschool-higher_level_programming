#!/usr/bin/python3
"""Module that defines a function for inheritance checking."""


def inherits_from(obj, a_class):
    """Returns True if obj inherited from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
