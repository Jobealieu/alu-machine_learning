#!/usr/bin/env python3
"""Poisson distribution."""


class Poisson:
    """Represents a Poisson distribution."""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Set lambtha from data, or from the given value."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for x in data:
                total += x
            self.lambtha = float(total / len(data))

    def pmf(self, k):
        """Return the PMF value for k successes."""
        k = int(k)
        if k < 0:
            return 0
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return (self.e ** -self.lambtha) * (self.lambtha ** k) / factorial

    def cdf(self, k):
        """Return the CDF value for k successes."""
        k = int(k)
        if k < 0:
            return 0
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
