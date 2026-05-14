#!/usr/bin/python3
""" Function that divides 2 integers and
prints the result.

Args:
    a (int): The first integer.
    b (int): The second integer.
Returns:
    The result of the division of a by b.
"""


def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
