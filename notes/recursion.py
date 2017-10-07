# mutually recursive is even and odd function
def is_even_mutual(n):
    if n == 0:
        return True
    return is_odd_mutual(n - 1)

def is_odd_mutual(n):
    if n == 0:
        return False
    return is_even_mutual(n - 1)

# turn into one recurisve function
def is_even(n):
    if n == 0:
        return True
    if n-1 == 0:
        return False
    return is_even((n - 1) - 1)

def cascade(n):
    print n
    if n >= 10:
        cascade(n // 10)
        print n
# >>> cascade(2013)
# 2013
# 201
# 20
# 2
# 20
# 201
# 2013

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# inverse_cascade(201)
#   grow(201)
#   f_then_g(grow, print, 20)
#       f(n) -> grow(20)
#           f_then_g(grow, print, 2)
#              f(n) -> grow(2)
#                   grow(2) -> f_then_g(grow, print, 0)
#              g(n) -> print(2)
#       g(n) -> print(20)



# --------------------------------------------------

# As another example of mutual recursion, consider a two-player game in which there are n initial
# pebbles on a table. The players take turns, removing either one or two pebbles from the table,
# and the player who removes the final pebble wins. Suppose that Alice and Bob play this game,
# each using a simple strategy:
#
# Alice always removes a single pebble
# Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
# Given n initial pebbles and Alice starting, who wins the game?

def play_alice(n):
    if n == 0:
        print "Bob wins!"
    play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print "Alice wins!"
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)

# >>> play_alice(20)
# Bob wins!


def multiply(m, n):
"""
>>> multiply(5, 3)
15
"""
    if n == 0:
        return 0
    if n == 1:
        return m
    return m + multiply(m, n - 1)

def recursive_countdown(n):
    """
    Create a recursive countdown function that takes in an integer n and prints out a
    countdown from n to 1.

    >>> countdown(3)
    3
    2
    1
    """

    if n >= 0:
        print n
        recursive_countdown(n - 1)

def recursive_countup(n):
    if n >= 0:
        recursive_countup(n - 1)
        print(n)

def sum_digits(n):
    """
    Write a recursive function that sums the digits of a number n. Assume n is positive.
    You might find the operators // and modulo useful.

    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n < 10:
        return n
    last = n % 10
    all_but_last = n // 10
    return sum_digits(all_but_last) + last

# n = 265
# all_but_last = 26
# last = 5
#
# sum_digits(26) + 5
#
# all_but_last = 2
# last = 6
#
# sum_digits(2)
# return 2

def count_stairways(n):
    """
    I want to go up a flight of stairs that has n steps.
    I can either take 1 or 2 steps each
    time. How many different ways can I go up this flight of stairs?
    Write a function count stair ways that solves this
    problem for me. Assume n is positive.
    """

    if n == 1 or n == 2:
        return n
    elif n < 0:
        return 0

    return count_stairways(n - 1) + count_stairways(n - 2)

# Consider a special version of the count stairways problem,
# where instead of taking 1 or 2 steps, we are able to take up
# to and including k steps at a time.
# Write a function count k that figures out the number
# of paths for this scenario.

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    # if n == 0:
    #     return 1
    if n == 1:
        return n
    total = 0
    for i in range(1, k + 1):
        if i > n:
            break
        if i == n:
            total += 1
        else:
            total += count_k(n - i, k)
    return total
