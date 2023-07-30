#!/usr/bin/env python3
"""Cats got your tongue"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis and
    return the result as a new numpy.ndarray."""
    return np.concatenate((mat1, mat2), axis=axis)
