#!/usr/bin/env python3
"""Transposes a 2D matrix."""


def matrix_transpose(matrix):
    """Return a new matrix that is the transpose of matrix."""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
