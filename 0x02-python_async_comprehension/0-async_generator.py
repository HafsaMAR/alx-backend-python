#!/usr/bin/env python3
"""This module contains an asynchronous
generator coroutine that yields random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None, None]:
    """ An asynchonous generator that yields random numbers.

    This coroutine loops 10 times, each time asynchronously waiting
    for 1 second and then yielding a random number between 0 and 10

    Yields:
        int: A random integer between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
