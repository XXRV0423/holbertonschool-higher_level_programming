#!/usr/bin/python3
"""Module that converts a Python objesct to a JSON string."""

import json


def to_json_string(my_obj):
    """Converts a Python objesct to a JSON string."""
    return json.dumps(my_obj)
