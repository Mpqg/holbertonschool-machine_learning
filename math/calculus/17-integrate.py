#!/usr/bin/env python3
"""integrate"""


def poly_integral(poly, C=0):
    """integrate"""
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float))
                                             for coeff in poly):
        return None
    if not isinstance(C, int):
        return None
    integral = [coeff / (power + 1) if power > 0 else coeff for power,
                coeff in enumerate(poly)]
    integral.insert(0, C)
    return integral
