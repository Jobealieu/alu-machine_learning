#!/usr/bin/env python3
"""Integral of a polynomial given as a coefficient list."""


def poly_integral(poly, C=0):
    """Return the integral coefficients of poly with constant C."""
    if type(poly) is not list or len(poly) == 0:
        return None
    if type(C) not in (int, float):
        return None
    if not all(type(c) in (int, float) for c in poly):
        return None
    integral = [C]
    for i, c in enumerate(poly):
        term = c / (i + 1)
        integral.append(int(term) if term.is_integer() else term)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
