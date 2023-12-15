#!/usr/bin/env python3
'''
Execute multiple coroutines at the same time with async.
'''
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' executes task_wait_random n times. '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
