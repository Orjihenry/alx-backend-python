#!/usr/bin/env python3
'''
    Strings and float to tuple.

    Parameters: 
        k: str
        v: int or float

    Returns: 
        Tuple[str, float]: a string and a floot
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' retuns string and square root of float/int '''
    return k, v**2

