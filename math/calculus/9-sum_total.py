#!/usr/bin/env python3
"""Sum of squares from 1 to n."""


def summation_i_squared(n):
    """Return the sum of i**2 for i in 1..n, or None if n is invalid."""
    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
