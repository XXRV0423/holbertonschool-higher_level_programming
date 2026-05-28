#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
