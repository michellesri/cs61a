# Copy Machine
# (a) Peter wants to print this week’s discussion handouts for
# all the students in CS 61A. However, both printers
# are broken! The first printer only prints multiples of
# n pages, and the second printer only prints multiples
# of m pages. Help Peter figure out whether or not it’s possible
# to print exactly total number of handouts!

def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True

    # can we make 8 or 6 (11 - 3 or 11 - 5) with the other #?
    if possible, then return True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
    if total == 0:
        return True
    elif total < 0:
        return False

    # keep decrementing.
    # if decrement goes evenly to 0 then we printed the exact total
    # otherwise, if it decremented into a negative, then we couldn't
        # print exactly the total
    return has_sum(total - n, m) or has_sum(total - m, n)
