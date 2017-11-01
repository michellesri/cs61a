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
    return has_sum(total - n, n, m) or has_sum(total - m, m, n)

# The next day, the printers break down even more! Each time they
# are used, the first printer prints a random x copies 50 ≤ x ≤ 60,
# and the second printer prints a random y copies 130 ≤ y ≤ 140. Peter
# also relaxes his expectations: he’s satisfied as long as there’s
# at least lower copies so there are enough for
# everyone, but no more than upper copies to prevent waste.

def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between 180 and 200 copies total
    True
    >>> sum_range(135, 150)
    False
    """

    def copies(pmin, pmax):
        if lower <= pmin and pmax <= upper:
            return True
        elif pmax > upper:
            return False
        return copies(pmin + 50, pmax + 60) or copies(pmin + 130, pmax + 140)

    return copies(0, 0)
