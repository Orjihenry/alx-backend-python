#!/usr/bin/env python3
'''
Measures the runtime.
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measures the average runtiome of wait_n. '''
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - startTime
    return total_time / n
