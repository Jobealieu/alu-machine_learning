#!/usr/bin/env python3
"""Performs element-wise arithmetic on two numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Return the element-wise sum, difference, product and quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
