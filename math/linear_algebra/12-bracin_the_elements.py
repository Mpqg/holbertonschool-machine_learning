#!/usr/bin/env python3
"""Bracing the elements"""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication,
    and division on two numpy.ndarrays."""
    sum = mat1 + mat2
    diff = mat1 - mat2
    prod = mat1 * mat2
    quotient = mat1 / mat2
    return sum, diff, prod, quotient
