#!/usr/bin/python3

"""Deletes a key in a dictionary.

Args:
    a_dictionary (dict): The dictionary.
    key (str): The key to delete.

Returns:
    The dictionary after deletion of the key.
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
