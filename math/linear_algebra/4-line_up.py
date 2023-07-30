#!/usr/bin/env python3
"""Line up"""


def add_arrays(arr1, arr2):
    """Function that adds two arrays element-wise"""
    if len(arr1) != len(arr2):
        return None
    result = []
    for x in range(len(arr1)):
        new_row = arr1[x] + arr2[x]
        result.append(new_row)
    return result
