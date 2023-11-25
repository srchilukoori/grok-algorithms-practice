"""
quick sort implementation using recursion
"""

from typing import List


def qs_recurse(inp_list: List[int]) -> List[int]:
    """
    sort the input list in ascending order
    """
    list_length = len(inp_list)
    if list_length <= 1:
        return inp_list

    if list_length == 2:
        if inp_list[0] <= inp_list[1]:
            return inp_list
        else:
            return inp_list[-1::-1]

    pivot_idx = (list_length - 1) // 2
    pivot_val = inp_list[pivot_idx]
    pivot_list = [pivot_val]

    left = []
    right = []
    for idx, ele in enumerate(inp_list):
        if idx != pivot_idx:
            if ele < pivot_val:
                left.append(ele)
            elif ele > pivot_val:
                right.append(ele)
            elif ele == pivot_val:
                pivot_list.append(ele)
    return qs_recurse(left) + pivot_list + qs_recurse(right)


assert qs_recurse([1]) == [1]
assert qs_recurse([2, 1]) == [1, 2]
assert qs_recurse([1, 1, 1]) == [1, 1, 1]
assert qs_recurse([4, 6, 3, 8, 1, 2, 5, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]
