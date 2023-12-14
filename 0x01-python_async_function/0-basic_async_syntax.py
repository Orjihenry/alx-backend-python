#!/usr/bin/env python3
'''
Waits a random number of seconds and returns it.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' waits for a random time '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
