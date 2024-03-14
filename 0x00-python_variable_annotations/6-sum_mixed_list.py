#!/usr/bin/env python3
"""Module for summing up a list of mixed integers and floats"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list containing elements
        that can be either integers or floats.

    Returns:
        float: The sum of all the numbers in the input list.
    """
    return sum(mxd_lst)
