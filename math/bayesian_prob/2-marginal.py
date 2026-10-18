#!/usr/bin/env python3
"""Module that calculates the marginal probability of the data"""
import numpy as np


def factorial(k):
    """Calculates the factorial of a non negative integer k"""
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result


def marginal(x, n, P, Pr):
    """Calculates the marginal probability of obtaining x and n
    over all probabilities in P

    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray of hypothetical probabilities
        Pr: 1D numpy.ndarray of prior beliefs of P

    Returns:
        the marginal probability of obtaining x and n
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    comb = factorial(n) / (factorial(x) * factorial(n - x))
    likelihood = comb * (P ** x) * ((1 - P) ** (n - x))
    return np.sum(likelihood * Pr)
