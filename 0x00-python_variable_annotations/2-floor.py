#!/usr/bin/env python3
"""Module for mathematical operations"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Parameters:
        n (float): The floating-point number whose floor is to be calculated.

    Returns:
        int: The largest integer less than or equal to the input
        floating-point number.
    """
    return math.floor(n)
