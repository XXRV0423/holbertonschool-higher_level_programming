#!/usr/bin/python3
"""Module that defines abstract Animal classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns animal sound."""
        pass


class Dog(Animal):
    """Class that represents a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Class that represents a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
