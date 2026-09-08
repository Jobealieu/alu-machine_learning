#!/usr/bin/env python3
"""Performs matrix multiplication on two 2D matrices."""


def mat_mul(mat1, mat2):
    """Return the matrix product, or None if inner dimensions differ."""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
             for j in range(len(mat2[0]))]
            for i in range(len(mat1))]
