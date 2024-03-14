#!/usr/bin/env python3
"""Module for creating multiplier functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float
        as input and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
