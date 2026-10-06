#!/usr/bin/env python3
"""Exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""

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
            self.lambtha = float(1 / (total / len(data)))

    def pdf(self, x):
        """Return the PDF value for time period x."""
        if x < 0:
            return 0
        return self.lambtha * self.e ** (-self.lambtha * x)

    def cdf(self, x):
        """Return the CDF value for time period x."""
        if x < 0:
            return 0
        return 1 - self.e ** (-self.lambtha * x)
