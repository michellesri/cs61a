def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.

    >>> lines = ['(+ 1', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """


def read_tail(src):
    """Return the remainder of a list in src, starting
    before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))

    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
