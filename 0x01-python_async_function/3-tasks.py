#!/usr/bin/env python3
"""This module provides a function to create asyncio
tasks for asynchronous coroutines."""
import asyncio
wait_radom = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random
    coroutine with the specified max_delay.

    Args:
        max_delay (int): The maximum delay value for wait_random coroutine.

    Returns:
        asyncio.Task: An asyncio Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_radom(max_delay))
