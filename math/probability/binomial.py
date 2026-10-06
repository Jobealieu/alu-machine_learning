#!/usr/bin/env python3
"""Binomial distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Set n and p from data, or from the given values."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for x in data:
                total += x
            mean = total / len(data)
            squares = 0
            for x in data:
                squares += (x - mean) ** 2
            variance = squares / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Return the PMF value for k successes."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        comb = self.factorial(self.n) / (
            self.factorial(k) * self.factorial(self.n - k))
        return comb * self.p ** k * (1 - self.p) ** (self.n - k)

    @staticmethod
    def factorial(m):
        """Return m! as a float."""
        result = 1.0
        for i in range(2, m + 1):
            result *= i
        return result

    def cdf(self, k):
        """Return the CDF value for k successes."""
        k = int(k)
        if k < 0:
            return 0
        if k > self.n:
            k = self.n
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
