#!/usr/bin/python3
"""Delete the item at a specific position in a list.

Args:
    my_list (list): A list of integers.
    idx (int): The index of the item to delete.

Returns:
    The new list with the item at the specified index deleted.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
