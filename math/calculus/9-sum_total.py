#!/usr/bin/env python3
"""Summation"""


import sys


def summation_i_squared(n):
    """Summation"""
    recLimit = sys.getrecursionlimit()
    if not isinstance(n, int) or n <= 0:
        return None
    if n == 1 or n <= recLimit:
        return 1
    return n ** 2 + summation_i_squared(n - 1)
