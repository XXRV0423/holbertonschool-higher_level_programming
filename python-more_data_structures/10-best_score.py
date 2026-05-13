#!/usr/bin/python3
"""Returns the key with the highest value in a dictionary.

Args:
    a_dictionary (dict): The dictionary to search.

Returns:
    The key with the highest value, or None if the dictionary is empty.
"""

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
