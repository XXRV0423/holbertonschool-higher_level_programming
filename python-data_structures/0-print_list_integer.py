#!/usr/bin/python3

"""Print all integers of a list.

Args:
    my_list (list): A list of integers.

Returns:
    None
"""
    
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
