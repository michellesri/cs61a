def one(x):
    if x:
        return 'input is true'
    return 'input is false'

def two(x):
    return x == 100

def three(x):
    if x % 6 == 0:
        x += x // 6
    return x

def four(ones_win):
    result = 6 if ones_win else 4

# Write a function summation that adds the first n elements in a sequence.
# The kth element in the sequence can be computed by evaluating term(k).

def summation(n, term):
    """Computes the summation of the first n numbers in the
    sequence defined by the function term.

    >>> square = lambda x: x * x
    >>> summation(5, square)
    55
    """
    if n == 0:
        return 0
    return term(n) + summation(n - 1, term)

# Write a function is_fib that returns
# True if its input is a fibonacci number, and False otherwise.

def is_fib(n):
    """Returns True if n is a fibonacci number,
    else False

    >>> is_fib(8)
    True
    >>> is_fib(9)
    False
    """
    x, y = 0, 1
    total = x + y

    while total < n:
        x = y
        y = total
        total = x + y

    return total == n
