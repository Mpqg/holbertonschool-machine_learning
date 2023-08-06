#!/usr/bin/env python3
"""Summation"""


def summation_i_squared(n):
    """Summation"""

    if not isinstance(n, int) or n <= 0:
        return None
    if n == 1:
        return 1
    return sum(map(lambda n: pow(n, 2), range(n + 1)))
