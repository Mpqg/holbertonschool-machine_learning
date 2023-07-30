#!/usr/bin/env python3
"""OK"""
def matrix_shape(matrix):
    """OK"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape
