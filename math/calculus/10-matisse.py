#!/usr/bin/env python3
"""Derivative of a polynomial given as a coefficient list."""


def poly_derivative(poly):
    """Return the derivative coefficients of poly, or None if invalid."""
    if type(poly) is not list or len(poly) == 0:
        return None
    if not all(type(c) in (int, float) for c in poly):
        return None
    deriv = [poly[i] * i for i in range(1, len(poly))]
    if all(c == 0 for c in deriv):
        return [0]
    return deriv
