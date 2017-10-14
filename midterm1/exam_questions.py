def is_ascending(n):
    """Returns True if the digits of N are in ascending order.
    The digits of the number going from right to left must be in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """

    if n < 10:
        return True

    last_digit = n % 10
    all_but_last = n // 10
    second_to_last = all_but_last % 10

    if second_to_last >= last_digit:
        return is_ascending(all_but_last)
    return False


# Implement a function count_one, which takes in a number n,
# and returns the number of ones in the digits of n.

def count_one(n):
    """Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """

    total_ones = 0
    num = n

    while num > 10:
        last_digit = num % 10 # last digit
        num = num // 10 # all but last digit
        if last_digit == 1:
            total_ones += 1
    if num < 10:
        if num == 1:
            total_ones += 1
    return total_ones

def count_one_recursive(n):
    """Counts the number of 1s in the digits of n

    >>> count_one_recursive(7007)
    0
    >>> count_one_recursive(123)
    1
    >>> count_one_recursive(161)
    2
    >>> count_one_recursive(1)
    1
    """

    if n < 10:
        if n == 1:
            return 1
        return 0

    return count_one_recursive(n % 10) + count_one_recursive(n // 10)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
