#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function returning a Fibonacci series with a max. value."""


def fibonacci(maxint):
    """A function to print out a Fibonacci series with a max. value.

    Args:
        maxint (int): an integer that serves as the upper bound of the loop.

    Returns:
        list: a series of Fibonacci numbers.

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(20)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    a, b = 0, 1
    series = [a]
    while b <= maxint:
        series.append(b)
        a, b = b, a+b
    return series
