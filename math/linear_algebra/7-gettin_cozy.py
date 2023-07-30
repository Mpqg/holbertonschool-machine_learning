#!/usr/bin/env python3


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specific axis and return the result as a new matrix.
    """
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if axis == 0:
        if cols1 != cols2:
            return None
        result = mat1 + mat2
    elif axis == 1:
        if rows1 != rows2:
            return None
        result = [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        raise ValueError("Cannot create concatenation.")
    return result