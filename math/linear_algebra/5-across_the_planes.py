#!/usr/bin/env python3


def add_matrices2D(mat1, mat2):
    """
    Add two matrices element-wise and return the result as a new matrix.
    """
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if rows1 != rows2 or cols1 != cols2:
        return None
    result = []
    for i in range(rows1):
        new_row = []
        for j in range(cols1):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    return result