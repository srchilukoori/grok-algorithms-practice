"""
example of recursion
"""


def countdown(start_num: int):
    if start_num <= 0:
        return
    print(start_num)
    countdown(start_num - 1)


countdown(10)
