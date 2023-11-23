"""
selection sort example
"""

from typing import List


def find_smallest(inp_list: List[int]):
    """
    returns index of the smallest value in list
    """
    if not inp_list:
        return

    min_value = inp_list[0]
    min_index = 0

    for idx, val in enumerate(inp_list):
        if val < min_value:
            min_value = val
            min_index = idx
    return min_index


def sorted_list(inp_list: List[int]):
    output = []
    while len(inp_list) > 0:
        smallest_index = find_smallest(inp_list)
        output.append(inp_list.pop(smallest_index))
    return output


assert sorted_list([6, 5, 4]) == [4, 5, 6]
assert sorted_list([1, 2, 3]) == [1, 2, 3]
assert sorted_list([]) == []
