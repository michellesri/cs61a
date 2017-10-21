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

    one_count = 0
    num = n

    while num > 0:
        last_digit = num % 10 # last digit
        num = num // 10 # all but last digit
        if last_digit == 1:
            one_count += 1
    return one_count

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

    last_digit = 0
    if n % 10 == 1:
        last_digit = 1
    return last_digit + count_one_recursive(n // 10)

def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    if n < 10:
        return 1

    one_count = 0
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if digit == 1:
            one_count += 1

    return one_count + total_ones(n - 1)

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    if number > 0 and number <= 3:
        return True
    return False




if __name__ == "__main__":
    import doctest
    doctest.testmod()
