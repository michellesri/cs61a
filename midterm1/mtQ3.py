# Triangulate
# It’s easy to see that in any triangle, each side must be shorter than the sum of the other two. Implement
# triangle, which takes three positive numbers, a, b, and c, and returns whether these three numbers could
# possibly be the lengths of the three sides of a triangle.

def triangle(a, b, c):
    """Return whether a, b, and c could be the legs of a triangle.
    >>> triangle(3, 4, 5)
    True
    >>> triangle(3, 4, 6)
    True
    >>> triangle(6, 3, 4)
    True
    >>> triangle(3, 6, 4)
    True
    >>> triangle(9, 2, 2)
    False
    >>> triangle(2, 4, 2)
    False
    """