#!/usr/bin/env python3
"""matisse"""


def poly_derivative(poly):
    """poly"""
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float))
                                             for coeff in poly):
        return None
    derivative = [coeff * power for power,
                  coeff in enumerate(poly[1:], start=1)]
    if all(deriv_coeff == 0 for deriv_coeff in derivative):
        return [0]
    return derivative
