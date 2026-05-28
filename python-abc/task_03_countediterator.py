#!/usr/bin/python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """An iterator that counts iterated items."""

    def __init__(self, iterable):
        """Initializes the iterator and counter."""
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next item and increments the counter."""
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Returns the number of iterated items."""
        return self._count
