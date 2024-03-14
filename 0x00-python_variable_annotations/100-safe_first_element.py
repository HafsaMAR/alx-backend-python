#!/usr/bin/env python3
"""The types of the elements of the input are not know
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence safely.
    Parameters:
        lst(Sequence[Any]): The Input sequence can be any type

    Returns:
        Union[Any, None]: The first element of the sequence or None
    """
    if lst:
        return lst[0]
    else:
        return None
