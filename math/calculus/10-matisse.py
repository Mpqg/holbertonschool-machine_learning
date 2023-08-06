#!/usr/bin/env python3
"""matisse"""


def poly_derivative(derivative):
    """return derivatives"""
    if type(derivative) != list or len(derivative) == 0:
        return None
    if len(derivative) == 1:
        return [0]
    for x in range(1, len(derivative)):
        derivative[x] = derivative[x] * x
    derivative.pop(0)
    return derivative
