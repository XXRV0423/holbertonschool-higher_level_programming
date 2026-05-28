#!/usr/bin/python3
"""Module that defines a function for class inheritance check."""


def is_kind_of_class(obj, a_class):
    """Returns True if the obj is an instance of a_class or inherited"""
    return isinstance(obj, a_class)
