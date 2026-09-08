#!/usr/bin/env python3
"""Adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return the element-wise sum, or None if the shapes differ."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
