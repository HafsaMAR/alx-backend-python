#!/usr/bin/env python3
"""implement to wait_n routine"""

import asyncio
wait_radom = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Asynchronously spawns n instances of the wait_random coroutine
    with specified max_delay.

    args:
    n (int): the number of times to spawn the wait_random coroutine
    max_delay (int) : maximum dlay value for each wait_radom routine

    Return:
    list[float]: A sorted list  containing the delays
    """
    delays = []
    for _ in range(n):
        delay = await wait_radom(max_delay)
        delays.append(delay)
    return sorted(delays)
