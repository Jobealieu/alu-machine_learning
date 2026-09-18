#!/usr/bin/env python3
"""Determinant of a matrix"""


def _det(m):
    """Determinant of a valid square matrix by Laplace expansion"""
    if len(m) == 1:
        return m[0][0]
    # ponytail: Laplace expansion is O(n!), fine for small matrices
    return sum((-1) ** j * m[0][j] *
               _det([row[:j] + row[j + 1:] for row in m[1:]])
               for j in range(len(m)))


def determinant(matrix):
    """Returns the determinant of a square matrix (list of lists)"""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError('matrix must be a list of lists')
    if matrix == [[]]:
        return 1
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError('matrix must be a square matrix')
    return _det(matrix)
