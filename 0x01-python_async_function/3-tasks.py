#!/usr/bin/env python3
''' 
Takes an integer and returns an async func.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    ''' Create asyncio task. '''
    task = asyncio.create_task(wait_random(max_delay))
    return task

# asyncio.run(task_wait_random())