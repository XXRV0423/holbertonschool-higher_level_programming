#!/usr/bin/python3
"""Module that defines a VerboseList class."""


class VerboseList(list):
    """A list that prints a message when an item is added."""

    def append(self, item):
        """Appends an item to the list and prints a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list with items and prints a message."""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Removes an item from the list and prints a message."""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Removes and returns an item
        at the given index and prints a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
