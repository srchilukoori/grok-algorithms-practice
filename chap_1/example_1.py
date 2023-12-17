"""
binary search example function
"""
from typing import List


def binary_search(ele_list: List[int], item: int):
    if not ele_list:
        raise ValueError("ele_list is empty")

    start = 0
    end = len(ele_list) - 1



    while start <= end:
        mid = (end + start) // 2
        if ele_list[mid] == item:
            return mid
        elif ele_list[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return None

my_list = [1, 2, 3, 4, 5, 6]

assert binary_search(my_list, 5) == 4
assert binary_search(my_list, 8) == None
assert binary_search(my_list, -1) == None
assert binary_search(my_list, 1) == 0
