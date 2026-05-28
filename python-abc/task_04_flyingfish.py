#!/bin/usr/python3
"""Module that demostrates multiple inheritance."""


class Fish:
    """Fish class."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming.")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water.")


class Bird:
    """Bird class."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying.")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from Fish and Bird."""

    def fly(self):
        """Prints flying fish flying message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints flying fish swimming message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
