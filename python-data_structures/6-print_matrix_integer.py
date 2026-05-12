#!/usr/bin/python3
"""Print a matrix of integers.
Args:
    matrix (list of lists): A matrix of integers.
Returns:
    None
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()
