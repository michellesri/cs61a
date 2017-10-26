HW_SOURCE_FILE = 'hw04.py'


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    if n > 3:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    g_values = [0, 1, 2, 3]
    current_num = 4

    if n <= 3:
        return n

    while current_num <= n:
        g_values.append(g_values[current_num - 1] + 2 \
            * g_values[current_num - 2] + 3 * g_values[current_num - 3])

        current_num += 1

    return g_values[n]


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    # direction = True
    # current_series_val = 0
    # i = 1
    # while i <= n:
    #
    #     if direction:
    #         current_series_val += 1
    #     else:
    #         current_series_val -= 1
    #
    #     if has_seven(i) or i % 7 == 0:
    #         direction = not direction
    #
    #     i += 1
    #
    # return current_series_val
    def recursive(i, current_value, direction):
        if i == n:
            return current_value

        if has_seven(i) or i % 7 == 0:
            if direction:
                return recursive(i + 1, current_value - 1, False)
            return recursive(i + 1, current_value + 1, True)
        else:
            if direction:
                return recursive(i + 1, current_value + 1, True)
            return recursive(i + 1, current_value - 1, False)

    return recursive(1, 1, True)



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    if amount == 0:
        return 0
    elif amount == 1:
        return 1

    total = 0
    power = 1
    n = amount
    while n > 0:
        



###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
