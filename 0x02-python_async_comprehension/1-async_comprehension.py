#!/usr/bin/env python3
"""Async comprehension"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random float numbers using async
    comprehension over async_generator

    Returns:
        List[float]: list of 10 random foat number
    """
    random_number = [number async for number in async_generator()]
    return random_number
