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
    if n == 0:
        return True
    x, y = 0, 1
    total = x + y

    while total < n:
        x = y
        y = total
        total = x + y
    return total == n

# Write a function make_mod that takes a number, n, as an argument, and returns a new function.
# The new function should take a single argument, x, and return the result of x modulo n.

def make_mod(n):
    """Returns a function that takes an argument x.
    That function will return x modulo n.
    >>> mod_7 = make_mod(7)
    >>> mod_7(3)
    3
    >>> mod_7(41)
    6
    """

    def inner(x):
        return x % n
    return inner

# Implement a function geo_sum that takes
# three numbers a and r (as defined above) and n, and
# calculates the sum of the first n elements of the geometric
# series defined by a and r. Use recursion!

def geo_sum(a, r, n):
    """Returns the first n elements of a geometric series.

    >>> geo_sum(1, 1/2, 4)  # 1 + 1/2 + 1/4 + 1/8
    1.875
    >>> geo_sum(2, 2, 3)  # 2 + 4 + 8
    14
    """

    if n == 1:
        return a
    return a + geo_sum(a * r, r, n - 1)

# Implement a function num_primes which takes a number n and returns the
# number of prime numbers less than or equal to n. You can assume there
# is already a function is_prime that takes in a number i and returns
# True if i is prime, and False otherwise. Use recursion!

def is_prime(i):
    m = 2
    while m * m <= i:
        if i % m == 0:
            return False
        m += 1
    return True

def num_primes(n):
    """Returns the number of primes less than or equal to n.

    >>> num_primes(6)   # 2, 3, 5
    3
    >>> num_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    count = 0

    if n <= 1:
        return 0

    if n > 1:
        if is_prime(n):
            count += 1
    return count + num_primes(n - 1)
