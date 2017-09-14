"""Generalization."""

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """

    return summation(n, cube)

def make_adder(n):
    """Return a function that takes one argument K
    and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

def outer(n):
    def inner(m):
        return n - m
    return inner

outer(61)
f = outer(10)
f(4)
outer(5)(4)
#
# Implement a function keep_ints like before, but now it takes in a number n
# and returns a function that has one parameter cond. The returned function
# prints out all numbers from 1 . . . i . . . n where calling cond(i) returns True.
def keep_ints(n):
    """Returns a function which takes one parameter cond and
    prints out all integers 1..i..n where calling cond(i)
    returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """
    def inner(cond):
        counter = 1
        while counter != n:
            if cond(counter):
                print counter
            counter += 1
    return inner


def is_even(x):
    return x % 2 == 0

keep_ints(5)(is_even)
