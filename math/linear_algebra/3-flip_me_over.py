#!/usr/bin/env python3


def matrix_transpose(matrix):
    """Returns the transposition of 2D Matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    # Create a new empty matrix to store the transpose
    transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    # Fill the transpose matrix with elements from the original matrix
    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix
