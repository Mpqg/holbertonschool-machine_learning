#!/usr/bin/env python3


import numpy as np

def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division on two numpy.ndarrays.
    """
    elementwise_sum = mat1 + mat2
    elementwise_diff = mat1 - mat2
    elementwise_prod = mat1 * mat2
    elementwise_quotient = mat1 / mat2
    return elementwise_sum, elementwise_diff, elementwise_prod, elementwise_quotient
