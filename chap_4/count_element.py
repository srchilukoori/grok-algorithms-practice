"""
recursive approach to count elements in an array
"""

from typing import List, Any

def count_elements(inp_list: List[Any], size: int = 0) -> int:
    if not inp_list:
        return size

    _ = inp_list.pop()
    size += 1
    return count_elements(inp_list, size)


assert count_elements([]) == 0
assert count_elements([1, 2, 3]) == 3
