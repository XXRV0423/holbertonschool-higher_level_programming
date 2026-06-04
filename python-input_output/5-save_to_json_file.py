#!/usr/bin/python3
"""Module that saves a Python object to JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
