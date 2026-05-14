#!/usr/bin/python3
"""Print x elements of a list.

Args:
    my_list (list): The list to print from.
    x (int): The number of elements to print.

Returns:
    int: The actual number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass

    print()
    return count
