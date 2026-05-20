#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality of square areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare inequality of square areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if current square is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if current square is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if current square is greater."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if current square is greater or equal."""
        return self.area() >= other.area()
