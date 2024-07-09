#!/usr/bin/env python3
""" list comprehension """
import random
import asyncio
import typing import Generator


async def async_generator():
    """ function for generating the async loops """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1.0, 10.0)
