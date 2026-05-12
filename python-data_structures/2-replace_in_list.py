#!/usr/bin/python3

"""Replace an element in a list at a specific index.

Args:
    my_list (list): A list of integers.
    idx (int): The index of the element to replace.
    element (int): The new element to insert.

Returns:
    The modified list.
"""


def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
