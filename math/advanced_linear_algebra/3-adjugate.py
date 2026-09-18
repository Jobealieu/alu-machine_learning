#!/usr/bin/env python3
"""Adjugate matrix of a matrix"""


def _det(m):
    """Determinant of a valid square matrix by Laplace expansion"""
    if len(m) == 1:
        return m[0][0]
    # ponytail: Laplace expansion is O(n!), fine for small matrices
    return sum((-1) ** j * m[0][j] *
               _det([row[:j] + row[j + 1:] for row in m[1:]])
               for j in range(len(m)))


def adjugate(matrix):
    """Returns the adjugate matrix of a non-empty square matrix"""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError('matrix must be a list of lists')
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')
    if n == 1:
        return [[1]]
    # adjugate[i][j] = cofactor[j][i], so drop row j and column i
    return [[(-1) ** (i + j) *
             _det([r[:i] + r[i + 1:] for r in matrix[:j] + matrix[j + 1:]])
             for j in range(n)] for i in range(n)]
