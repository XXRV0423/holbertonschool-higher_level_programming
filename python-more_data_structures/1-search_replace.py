#!/usr/bin/python3
"""Search and replace all occurrences of an element in a list.

Args:
    my_list (list): The list to search through.
    search: The element to search for.
    replace: The element to replace the searched element with.

Returns:
    A new list with the searched element replaced by the new element.
"""


def search_replace(my_list, search, replace):
    return [replace if element == search else element for element in my_list]
