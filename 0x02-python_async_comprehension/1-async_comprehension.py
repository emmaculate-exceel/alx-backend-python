#!/usr/bin/env python3
""" async List comprehension """
from typing import Generator
import asyncio
import random
from 0-async_generator import async_generator


async def async_comprehension() -> Generator[float, None, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        random.randint(1.0, 10.0) 
