"""
recursive function to calculate factorial
"""


def factorial(num: int, accum: int = 1):
    """
    factorial
    """
    if num == 0:
        return accum

    if num < 0:
        raise ValueError("Factorial is defined for positive integers")

    return factorial(num - 1, accum * num)


assert factorial(10) == 3628800
