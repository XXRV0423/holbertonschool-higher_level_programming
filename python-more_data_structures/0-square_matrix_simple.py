#!/usr/bin/python3
"""Computes the square value of all integers of a matrix.

Args:
    matrix (list): A list of lists of integers.

Returns:
    A new list of lists of integers representing the square value of
    all integers of the input matrix.
"""


def square_matrix_simple(matrix=[]):
    return [[x ** 2 for x in row] for row in matrix]
