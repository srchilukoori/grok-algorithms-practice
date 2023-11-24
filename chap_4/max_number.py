"""
recursive function to find max element in a list of ints
"""

from typing import List


def max_value(inp_list: List[int], max_ele: int | None = None):
    if not inp_list:
        return max_ele

    new_value = inp_list.pop()
    max_ele = max(max_ele, new_value) if max_ele is not None else new_value
    return max_value(inp_list, max_ele)


assert max_value([]) == None
assert max_value([0]) == 0
assert max_value([1, 3, 100]) == 100
