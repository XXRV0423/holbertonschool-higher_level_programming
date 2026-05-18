#!/usr/bin/python3
"""Module that multiplies matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    return np.matrix(m_a) * np.matrix(m_b)
