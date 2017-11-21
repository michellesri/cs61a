from operator import add, mul

def reduce(f, s, initial):
    """combine elements of s using f starting at initial_balance

    >>> reduce(mul, [2, 4, 8], 1)
    64

    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """

    for x in s:
        initial = f(initial, x)
    return initial


def reduce_recursive(f, s, initial):
    """combine elements of s using f starting at initial_balance

    >>> reduce(mul, [2, 4, 8], 1)
    64

    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce_recursive(f, rest, f(initial, first))
