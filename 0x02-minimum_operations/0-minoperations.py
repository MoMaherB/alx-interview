#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Minimum Operations method
    """

    if n < 2:
        return 0
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
