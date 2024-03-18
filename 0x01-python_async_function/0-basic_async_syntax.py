#!/usr/bin/env python3
"""learn asyncio and random"""

import asyncio
import random


async def wait_random(max_delay=10):
    """coroutine to sleep"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay