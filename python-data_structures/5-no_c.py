#!/usr/bin/python3
"""Remove all characters 'c' and '
C' from a string.
Args:
    my_string (str): The input string.
Returns:
    str: The string with all 'c' and 'C' characters removed.
"""


def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char not in ('c', 'C'):
            new_string += char
    return new_string
