import asyncio
from wait_random import wait_random

async def wait_n(n: int, max_delay: int):
    tasks = [wait_random(max_delay) for _ in range(n)]
