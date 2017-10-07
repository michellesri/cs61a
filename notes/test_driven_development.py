# from ucb import trace
# @trace
def gcd(m, n):
    """Returns the largest k that divides both m and n.

    k, m, n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(5, 5)
    5
    """

    if m == n:
        return m
    elif m < n: #if n is smaller, switch the two
        return gcd(n, m)
    #euclidean distance -> the gcd if m and n with m > n is the same as:
    return gcd(m - n, n)

# $python3 -m doctests test_driven_development.py to run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
