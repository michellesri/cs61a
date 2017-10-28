from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    12321
    1, 1232
    12, 123
    123, 12
    1232, 1
    12321, _

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: (x % 10) + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        while i < n:
            print(i)
            i += 1
        print(n)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    a = min(a, b)
    b = max(a, b)
    a_b_total = 0
    while a > 0:
        a_b_total += b
        a -= 1
    return a_b_total + c


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if n == i:
            return True
        if n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    def helper(i, is_even):
        if is_even:
            current_val = even_term(i)
        else:
            current_val = odd_term(i)

        if i == n:
            return current_val

        return current_val + helper(i + 1, not is_even)

    return helper(1, False)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_digits(num, digit):
        if num == 0:
            return 0
        if num % 10 == digit:
            return 1 + count_digits(num // 10, digit)
        return 0 + count_digits(num // 10, digit)

    if n < 10:
        return 0
    return count_digits(n // 10, 10 - n % 10) + ten_pairs(n // 10)
