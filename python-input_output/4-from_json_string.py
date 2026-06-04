#!/usr/bin/python3
"""MOdule that converts a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object."""
    return json.loads(my_str)
