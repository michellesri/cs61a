def gcd(a, b):
    while(y):
        x, y = y, x % y

    return x

def lowestCommonMultiple(x, y):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    lcm = x * y / gcd(x, y)
    return lcm

def has_digit(n, k):
    # digits = [int(x) for x in str(n)]
    # print(digits)
    if k in n:
        return True
    else:
        return False

def unique_digits(n):
    counter = 0
    unique_digits_arr = []
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if len(unique_digits_arr) == 0:
            unique_digits_arr.append(digit)
            counter += 1
        elif has_digit(unique_digits_arr, digit):
            continue
        else:
            unique_digits_arr.append(digit)
            counter += 1
    return counter


    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
