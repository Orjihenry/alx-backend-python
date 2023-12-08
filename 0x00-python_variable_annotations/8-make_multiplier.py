#!/usr/bin/env python3
'''
   Multiply float by multiplier.

   Parameters: multiplier[float]
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda a: a*multiplier
