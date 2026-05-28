#!/usr/bin/env python3
"""Module that demonstrates mixins."""


class SwimmingMixin:
    """Mixin class for swimming behavior."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyingMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimmingMixin, FlyingMixin):
    """Dragon class that can both swim and fly."""

    def roar(self):
        """Prints dragon roaring message."""
        print("The dragon roars!")
