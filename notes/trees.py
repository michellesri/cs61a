# Constructor
def tree(label, branches=[]):
    # for branch in branches:
        # assert is_tree(branch) # is the tree a tree???
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)


t = tree(1,
        [tree(3,
            [tree(4),
            tree(5),
            tree(6)]),
        tree(2)])

simple_tree = tree(3,
    [tree(4), tree(5)])

def tree_max(t):
    """Return the max of a tree (the largest number in a tree)."""
    return max([label(t)] + [branch for branch in branches(t)])

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t"""

    return tree(label(t) ** 2, [square_tree(branch) for branch in branches(t)])


# Define the procedure find path(tree, x) that, given a tree tree and a value
# x, returns a list containing the nodes along the path required to get from the
# root of tree to a node x. If x is not present in tree, return None. Assume
# that the entries of tree are unique.
def find_path(tree, x):
    """
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]

    if is_leaf(tree):
        return None

    for branch in branches(tree):
        find_path_list = find_path(branch, x)
        if find_path_list is not None:
            return [label(tree)] + find_path_list


    # if label(tree) == x:
    #     return [label(tree)]
    #
    # # all of these should be none except for the correct path
    # paths = [find_path(branch, x) for branch in branches(t)]
    # for path in paths:
    #     if path:
    #         # return the label of the correct path along with the rest of it
    #         return [label(tree)] + path
