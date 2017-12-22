# Implement collapse, which takes a non-negative integer, and returns the result of removing all digits
# from it that duplicate the digit immediately to their right.

def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    
    left, last = n // 10, n % 10