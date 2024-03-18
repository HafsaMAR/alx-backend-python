#!/usr/bin/env python3
""" Module: measure_runtime
This module provides functionality for mesuring the runtime
performance of asychronous coroutines
"""


from typing import List
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per iteration for wait_n

    Args:
        n (int): the number of times to spawn the wait_random
        max_delay (int): the maximum delay value for each routine

    Returns:
        float: the average execution time per iteration
    """

    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
