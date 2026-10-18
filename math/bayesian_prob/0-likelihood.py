#!/usr/bin/env python3
"""Module that calculates the likelihood of binomial data"""
import numpy as np


def likelihood(x, n, P):
    """Calculates the likelihood of obtaining x successes in n trials
    for each hypothetical probability in P

    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray of hypothetical probabilities

    Returns:
        1D numpy.ndarray containing the likelihood for each value in P
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    comb = factorial(n) / (factorial(x) * factorial(n - x))
    return comb * (P ** x) * ((1 - P) ** (n - x))


def factorial(k):
    """Calculates the factorial of a non negative integer k"""
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result
