#!/usr/bin/env python3
"""Concatenates two numpy.ndarrays along a specific axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a new numpy.ndarray joining mat1 and mat2 along axis."""
    return np.concatenate((mat1, mat2), axis=axis)
