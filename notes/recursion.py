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