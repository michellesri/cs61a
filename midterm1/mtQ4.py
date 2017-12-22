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
    
    # if the number is a single digit, return.
    if left == 0:
        return last
    
    # if the last is the same as the last digit on the left side
        # then we have a duplicate. recurisvely call the fn
            # with only the left side
    elif last == left % 10:
        return collapse(left)

    #else, the number isn't a duplicate.
        # keep it in the recursive call
    else:
        return collapse(left) * 10 + last