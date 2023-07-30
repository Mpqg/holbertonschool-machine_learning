#!/usr/bin/env python3
"""Function calculating the shape of a matrix"""


def matrix_shape(matrix):
    """Return shape"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape
