#!/usr/bin/python3
"""Module that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices."""

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []

    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            result = 0
            for i in range(len(m_b)):
                result += row[i] * m_b[i][col]
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix


def validate_matrix(matrix, name):
    """Validates a matrix."""

    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("{} must be a list of lists".format(name))

    if matrix == [] or matrix == [[]]:
        raise ValueError("{} can't be empty".format(name))

    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(
                    "{} should contain only integers or floats".format(name)
                )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "each row of {} must be of the same size".format(name)
            )
