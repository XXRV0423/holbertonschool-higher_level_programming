#!/usr/bin/python3
"""Find the biggest integer of a list.
Args:
    my_list (list): The list to search.
Returns:
    The biggest integer in my_list, or None if my_list is empty.
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_int = my_list[0]
    for num in my_list:
        if num > max_int:
            max_int = num

    return max_int
