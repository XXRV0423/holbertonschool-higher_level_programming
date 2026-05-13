#!/usr/bin/python3
"""Find all multiples of 2 in a list.

Args:
    my_list (list): A list of integers.

Returns:
    A list of True or False, depending on whether the integer at the same
    position in the original list is a multiple of 2.
"""


def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]
