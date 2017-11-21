from operator import add, mul

def reduce(f, s, initial):
    """combine elements of s using f starting at initial_balance

    >>>reduce(mul, [2, 4, 8], 1)
    64

    >>>reduce(add, [1, 2, 3, 4], 0)
    """
