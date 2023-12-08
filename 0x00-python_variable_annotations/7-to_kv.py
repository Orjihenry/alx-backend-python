#!/usr/bin/env python3
'''
    Strings and float to tuple.
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' retuns string and square root of float/int '''
    return k, v**2

