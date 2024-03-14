#!/usr/bin/env python3
"""Module for creating key-value tuples with squared values"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k and
    the second element
    is the square of the int/float v.

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """

    return k, v ** 2.0
