#!/usr/bin/env python3
"""Module for summing up a list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.

    Parameters:
        input_list (List[float]): A list containing floating-point numbers.

    Returns:
        float: The sum of all the numbers in the input list.
    """
    return sum(input_list)
