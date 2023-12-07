#!/usr/bin/env python3
'''
    Calculate the sum of a mixed list
    using the sum function.

    Parameters:
    - mxd_lst (List[float]): A list.

    Returns:
    float: The sum of the elements in the input list.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
