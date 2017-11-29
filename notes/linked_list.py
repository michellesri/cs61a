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
