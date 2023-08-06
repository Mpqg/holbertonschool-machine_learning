#!/usr/bin/env python3
"""Summation"""


def summation_i_squared(n):
    """Summation of i sq"""
    if not isinstance(n, int) or n <= 0:
        return None
    if n == 1:
        return 1
    return n ** 2 + summation_i_squared(n - 1)
