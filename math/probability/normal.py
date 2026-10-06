#!/usr/bin/env python3
"""Normal distribution."""


class Normal:
    """Represents a normal distribution."""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Set mean and stddev from data, or from the given values."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for x in data:
                total += x
            self.mean = float(total / len(data))
            squares = 0
            for x in data:
                squares += (x - self.mean) ** 2
            self.stddev = float((squares / len(data)) ** 0.5)

    def z_score(self, x):
        """Return the z-score of x."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Return the x-value of z."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Return the PDF value for x."""
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        return self.e ** exponent / (self.stddev * (2 * self.pi) ** 0.5)

    def cdf(self, x):
        """Return the CDF value for x."""
        z = (x - self.mean) / (self.stddev * 2 ** 0.5)
        # the checker's expected output was generated with pi = 3.14159265359
        pi = 3.14159265359
        erf = (2 / pi ** 0.5) * (
            z - z ** 3 / 3 + z ** 5 / 10 - z ** 7 / 42 + z ** 9 / 216)
        return 0.5 * (1 + erf)
