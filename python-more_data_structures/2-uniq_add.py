#!/usr/bin/python3
"""Adds all unique integers in a list (only once for each integer).
Args:
    my_list (list): The list of integers to add.
Returns:
    The sum of all unique integers in the list.
"""


def uniq_add(my_list=[]):
    unique_numbers = []
    total = 0

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            total += number
    return total
