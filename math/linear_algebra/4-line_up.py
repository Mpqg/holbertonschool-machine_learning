#!/usr/bin/env python3


def add_arrays(arr1, arr2):
    """OK
    """
    if len(arr1) != len(arr2):
        return None
    result = []
    for x in range(len(arr1)):
        new_row = arr1[x] + arr2[x]
        result.append(new_row)
    return result
