#!/usr/bin/env python3
""" list comprehension """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ function for generating the async loops """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
