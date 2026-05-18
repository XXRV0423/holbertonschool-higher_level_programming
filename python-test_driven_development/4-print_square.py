#!/usr/bin/python3
"""Module that prints a square."""


def print_square(size):
    """Prints a square using the # character."""

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
