#!/usr/bin/env python3

  def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.
    Args:
        matrix (list): The input matrix.
    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape
