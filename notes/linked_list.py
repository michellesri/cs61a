class Link:
    """A linked list with a first element and the rest.
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[1]
    4
    """
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    """Return a string that would evaluate to s. Use this to display a Link.
    >>> link_expression(s)
    'Link(3, Link(4, Link(5)))'
    """
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

def extend_link(s, t):
    """
    builds a linked list containing the elements of one Link instance s
    followed by the elements of another Link instance t.
    >>> extend_link(s, s)
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    >>> Link.__add__ = extend_link
    >>> s + s
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    """
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    """
    applies a function f to each element of a linked list s
    and constructs a linked list containing the results.
    >>> map_link(square, s)
    Link(9, Link(16, Link(25)))

    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """
    returns a linked list containing all elements of a linked list s
    for which f returns a true value
    >>> odd = lambda x: x % 2 == 1
    >>> map_link(square, filter_link(odd, s))
    Link(9, Link(25))
    >>> [square(x) for x in [3, 4, 5] if odd(x)]
    [9, 25]
    """
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator):
    """
    function recursively constructs a string that contains the elements
    of a linked list seperated by some separator string. The result is
    much more compact than the output of link_expression.
    >>> join_link(s, ", ")
    '3, 4, 5'
    """
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)
        return with_m + without_m

def print_partitions(n, m):
    """
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
