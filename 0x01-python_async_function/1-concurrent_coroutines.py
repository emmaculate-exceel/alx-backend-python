#!/usr/bin/env python3
""" executing multiple coroutines at same time """


import asyncio
from wait_random import wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """ await the task to get completed """
    tasks = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(tasks)
    return result
