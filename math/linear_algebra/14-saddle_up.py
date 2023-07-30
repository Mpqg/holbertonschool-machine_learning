#!/usr/bin/env python3


import numpy as np


def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication on two numpy.ndarrays
    and return the result as a new numpy.ndarray.
    """
    return np.dot(mat1, mat2)
