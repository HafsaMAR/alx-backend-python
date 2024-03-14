#!/usr/bin/env python3
"""Annotation of the function paramters"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples when each tuple contains an element from
    the input iterable and its corresponding length

    Parameters:
        lst (Iterable[Sequence]): the input itereable containing sequences

    Returns:
        List[Tuple[sequence, int]]: A list of tuples each tuple contains an
        element from the input iterable and its lenght
    """
    return [(i, len(i)) for i in lst]
