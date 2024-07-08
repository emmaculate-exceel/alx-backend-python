#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay = 10):
    delay = random.uniform(10, max_delay)
    await asyncio.sleep(max_delay)
    return delay

asyncio.run(wait_random())
