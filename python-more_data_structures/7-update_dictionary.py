#!/usr/bin/python3
"""Replace or add key in a dictionary.
Args:
    a_dictionary (dict): The dictionary.
    key: The key to replace or add.
    value: The value associated with the key.
Returns:
    The updated dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
