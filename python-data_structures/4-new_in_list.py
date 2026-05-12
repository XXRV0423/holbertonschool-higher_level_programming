#!/usr/bin/python3
"""Replace an element in a list at a specific index
without modifying the original list.
Args:
    my_list (list): A list of integers.
    idx (int): The index of the element to replace.
    element (int): The new element to insert.
Returns:
    A new list with the specified element replaced,
    or the original list if the index is out of bounds.
"""


def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    else:
        return my_list
