#!/usr/bin/env python3
'''
    Calculate the sum of elements in the input list
    using the sum function.

    Parameters:
    - input_list (List[float]): A list of floats.

    Returns:
    float: The sum of the elements in the input list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    return float(sum(input_list))
