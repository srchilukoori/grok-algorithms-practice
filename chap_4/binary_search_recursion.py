"""
recursion approach to binary search
"""

from typing import List


def search(inp_list: List[int], lookup_value: int, start_index: int = 0):
    """
    index of the value if it exists in the list
    """
    if len(inp_list) == 1 and inp_list[0] == lookup_value:
        return start_index
    start = 0
    end = len(inp_list) - 1
    mid = (start + end) // 2
    mid_value = inp_list[mid]
    if mid_value == lookup_value:
        return mid + start_index
    elif mid_value > lookup_value:
        return search(inp_list[:mid], lookup_value, start_index)
    else:
        return search(inp_list[mid + 1:], lookup_value, start_index + mid + 1)


assert search([1, 2, 3], 2) == 1
assert search([0, 1, 2, 3, 4, 5], 5) == 5
assert search([0, 1, 2, 3, 4, 5], 2) == 2
