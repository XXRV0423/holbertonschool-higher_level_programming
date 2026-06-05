#!/usr/bin/python3
"""Module that inserts a line of text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string."""
    new_content = ""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_content += line

            if search_string in line:
                new_content += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
