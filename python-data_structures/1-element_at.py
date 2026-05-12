#!/usr/bin/python3

"""Retrieve an element from a list.

Args:
    my_list (list): A list of integers.
    idx (int): The index of the element to retrieve.

Returns:
    The element at the specified index, or None if the index is out of bounds.
"""


def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
