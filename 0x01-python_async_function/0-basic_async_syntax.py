#!/usr/bin/env python3
""" asynchronous coroutine for the integer argument """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waiting period for the async function """
    delay = random.uniform(10, max_delay)
    await asyncio.sleep(max_delay)
    return delay

asyncio.run(wait_random())
