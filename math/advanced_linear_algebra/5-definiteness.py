#!/usr/bin/env python3
"""Definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Returns the definiteness of a symmetric numpy.ndarray, or None"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError('matrix must be a numpy.ndarray')
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or
            matrix.size == 0 or not np.allclose(matrix, matrix.T)):
        return None
    ev = np.linalg.eigvalsh(matrix)
    ev[np.isclose(ev, 0)] = 0
    if np.all(ev > 0):
        return 'Positive definite'
    if np.all(ev >= 0):
        return 'Positive semi-definite'
    if np.all(ev < 0):
        return 'Negative definite'
    if np.all(ev <= 0):
        return 'Negative semi-definite'
    return 'Indefinite'
