"""
recursion sum of array
"""
from typing import List

def total(inp_list: List[int], total_sum: int = 0) -> int:
    if not inp_list:
        return total_sum
    total_sum = total_sum + inp_list.pop()
    return total(inp_list, total_sum)


assert total([2, 4, 6]) == 12
assert total([]) == 0
assert total([0]) == 0
